"""Controle pessoal em uma planilha separada; nenhuma integração com Discord."""
import json
import os
from datetime import date, datetime

import gspread
from google.oauth2.service_account import Credentials
from production_core import BRT, initial, fetch, apply_feed
from production_confirmations import prepare, ingest, replay, apply_answers, question_formula

SHEET_ID='1Rq9QIEQIm2MSBVl9SDTRTa8QqpuhGbRQGZ_OnK1pr4E'
STATE_TAB='_Controle'
EVENT_TAB='_Publicacoes'
ANCHORS=[
 ('deMBNYtmA6g','2026-10-17T17:52:27+00:00',1),
 ('YOhSbA3Gw9o','2026-10-15T22:23:34+00:00',2),
 ('Dl2fnGdSaTc','2026-10-18T00:18:16+00:00',1),
 ('C-egSsVTgMY','2026-10-17T12:00:46+00:00',2),
 ('WrCcz2YwtEo','2026-10-17T13:27:40+00:00',2),
]

def bootstrap():
 state=initial()
 for c,(video,published,position) in zip(state['channels'],ANCHORS):
  c.update(position=position,seen=[video],latest=dict(id=video,published=published,
           date=datetime.fromisoformat(published).astimezone(BRT).date().isoformat()))
 return state

def author(c):
 return 'A confirmar' if c['position'] is None else 'Eu' if c['position']==1 else f"Parceiro {c['position']-1}"

def correct_author(c,value):
 """A correção se refere ao vídeo exibido, antes de processar vídeos novos."""
 if not value or value==c.get('displayed_author'):return
 if value=='A confirmar':
  c['position']=None
  return
 options=['Eu']+[f'Parceiro {i}' for i in range(1,c['people'])]
 if value not in options:raise ValueError('Autor inválido: '+c['name'])
 c['position']=options.index(value)+1

def cell(value,formula=False):
 if value is None or value=='':return {}
 typ='formulaValue' if formula else 'boolValue' if isinstance(value,bool) else 'numberValue' if isinstance(value,(int,float)) else 'stringValue'
 return {'userEnteredValue':{typ:value}}

def put(sheet_id,row,col,values,formulas=False):
 return {'updateCells':{'start':{'sheetId':sheet_id,'rowIndex':row,'columnIndex':col},
    'rows':[{'values':[cell(v,formulas) for v in line]} for line in values],
    'fields':'userEnteredValue'}}

def sync(book):
 meta=book.fetch_sheet_metadata()
 sheets={s['properties']['title']:s['properties']['sheetId'] for s in meta['sheets']}
 if STATE_TAB not in sheets:
  result=book.batch_update({'requests':[{'addSheet':{'properties':{'title':STATE_TAB,'hidden':True,'gridProperties':{'rowCount':10,'columnCount':2}}}}]})
  sheets[STATE_TAB]=result['replies'][0]['addSheet']['properties']['sheetId']
 raw=book.worksheet(STATE_TAB).acell('A1').value
 state=json.loads(raw) if raw else bootstrap()
 if EVENT_TAB not in sheets:
  result=book.batch_update({'requests':[{'addSheet':{'properties':{'title':EVENT_TAB,'hidden':True,'gridProperties':{'rowCount':1000,'columnCount':2}}}}]})
  sheets[EVENT_TAB]=result['replies'][0]['addSheet']['properties']['sheetId']
 for channel in state['channels']:prepare(channel)
 by_handle={c['handle']:c for c in state['channels']}
 event_row_count=next((s['properties']['gridProperties']['rowCount'] for s in meta['sheets'] if s['properties']['title']==EVENT_TAB),1000)
 for row in book.worksheet(EVENT_TAB).get(f'A1:B{event_row_count}'):
  if len(row)>1 and row[0] in by_handle:by_handle[row[0]]['events'].append(json.loads(row[1]))
 # Coletar antes de ler comandos reduz a janela de concorrência com edições humanas.
 feeds={}
 for c in state['channels']:
  try:feeds[c['handle']]=fetch(c['channel_id'])
  except Exception as exc:
   print(f"[produção] {c['name']}: {type(exc).__name__}")
 queue_count=state.get('queue_count',0)
 answers={}
 if queue_count:
  for row in book.worksheet('Painel').get(f'E22:K{21+queue_count}'):
   if len(row)>=7 and row[6]:answers[row[6]]=row[0] if row else 'Pendente'
 apply_answers(state['channels'],answers)
 requests=[]
 for i,c in enumerate(state['channels']):
  c['error']=None
  if c['handle'] in feeds:
   ingest(c,feeds[c['handle']])
   c['last_checked']=datetime.now(BRT).isoformat(timespec='seconds')
  else:c['error']='Falha na consulta. Dados anteriores preservados.'
  r=6+i;t=10+i
  latest=c['latest']
  serial=(date.fromisoformat(latest['date'])-date(1899,12,30)).days if latest else None
  requests.append(put(sheets['Cadastro'],r,2,[[serial,c['minimum'],c['people'],c['position']]]))
  requests.append(put(sheets['Cadastro'],r,9,[[c['maximum']]]))
  requests.append(put(sheets['Painel'],t,8,[[author(c)]]))
  c['displayed_author']=author(c)
  requests.append(put(sheets['Cadastro'],28+i,0,[[c['name'],c['last_checked'][8:10]+'/'+c['last_checked'][5:7]+' '+c['last_checked'][11:16] if c['last_checked'] else 'Não consultado',latest['id'] if latest else '',c['error'] or 'Atualizado']]))
  if latest:
   requests.append(put(sheets['Cadastro'],28+i,2,[[f'=HYPERLINK("https://www.youtube.com/watch?v={latest["id"]}";"Abrir vídeo")']],True))
 # Linhas estáveis: respostas sempre vinculadas ao ID, nunca ao dia de abertura.
 ledger=[]
 for c in state['channels']:
  for event in c['events']:
   if event['asked']:
    fresh='queue_row' not in event
    if fresh:
     event['queue_row']=22+queue_count
     queue_count+=1
    row=event['queue_row'];serial=(date.fromisoformat(event['date'])-date(1899,12,30)).days
    requests.append(put(sheets['Painel'],row-1,0,[[c['name'],serial]]))
    title=(event.get('title') or 'Abrir vídeo').replace('"','""')
    requests.append(put(sheets['Painel'],row-1,2,[[f'=HYPERLINK("https://www.youtube.com/watch?v={event["id"]}";"{title}")',question_formula(row)]],True))
    if fresh:requests.append(put(sheets['Painel'],row-1,4,[['Pendente']]))
    requests.append(put(sheets['Painel'],row-1,5,[[f'=IF(E{row}="Pendente";"Aguardando resposta";IF(E{row}=J{row};"Confirmado";"Aplicando resposta"))']],True))
    requests.append(put(sheets['Painel'],row-1,9,[[event.get('answer','Pendente'),event['id']]]))
   ledger.append([c['handle'],json.dumps(event,ensure_ascii=False,separators=(',',':'))])
 # Crescer sem descartar pendências nem históricos antigos.
 panel_rows=next(s['properties']['gridProperties']['rowCount'] for s in meta['sheets'] if s['properties']['title']=='Painel')
 if 22+queue_count>panel_rows:
  requests.insert(0,{'appendDimension':{'sheetId':sheets['Painel'],'dimension':'ROWS','length':max(100,22+queue_count-panel_rows)}})
 ledger_rows=next((s['properties']['gridProperties']['rowCount'] for s in meta['sheets'] if s['properties']['title']==EVENT_TAB),1000)
 if len(ledger)>ledger_rows:requests.insert(0,{'appendDimension':{'sheetId':sheets[EVENT_TAB],'dimension':'ROWS','length':max(100,len(ledger)-ledger_rows)}})
 if ledger:requests.append(put(sheets[EVENT_TAB],0,0,ledger))
 state['queue_count']=queue_count
 if not queue_count:requests.append(put(sheets['Painel'],21,0,[['Nenhuma confirmação pendente.']]))
 if queue_count:
  grid={'sheetId':sheets['Painel'],'startRowIndex':21,'endRowIndex':21+queue_count,'startColumnIndex':0,'endColumnIndex':6}
  requests.extend([
   {'repeatCell':{'range':grid,'cell':{'userEnteredFormat':{'horizontalAlignment':'CENTER','verticalAlignment':'MIDDLE','wrapStrategy':'WRAP'}},'fields':'userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment,userEnteredFormat.wrapStrategy'}},
   {'repeatCell':{'range':dict(grid,startColumnIndex=1,endColumnIndex=2),'cell':{'userEnteredFormat':{'numberFormat':{'type':'DATE','pattern':'dd/mm/yyyy'}}},'fields':'userEnteredFormat.numberFormat'}},
   {'repeatCell':{'range':dict(grid,startColumnIndex=4,endColumnIndex=5),'cell':{'userEnteredFormat':{'backgroundColor':{'red':1,'green':.96,'blue':.8}}},'fields':'userEnteredFormat.backgroundColor'}},
   {'setDataValidation':{'range':dict(grid,startColumnIndex=4,endColumnIndex=5),'rule':{'condition':{'type':'ONE_OF_LIST','values':[{'userEnteredValue':a} for a in ['Pendente','Sim','Não']]},'strict':True,'showCustomUi':True}}},
   {'updateDimensionProperties':{'range':{'sheetId':sheets['Painel'],'dimension':'ROWS','startIndex':21,'endIndex':21+queue_count},'properties':{'pixelSize':80},'fields':'pixelSize'}}])
 for c in state['channels']:c.pop('events',None)
 # Estado e células são gravados juntos: uma falha não avança só metade do controle.
 requests.append(put(sheets[STATE_TAB],0,0,[[json.dumps(state,ensure_ascii=False,separators=(',',':'))]]))
 book.batch_update({'requests':requests})
 print('[produção] 5 canais atualizados; datas em Brasília e estado persistido no Sheets.')

def main():
 creds=Credentials.from_service_account_info(json.loads(os.environ['GOOGLE_CREDENTIALS_JSON']),scopes=['https://www.googleapis.com/auth/spreadsheets'])
 sync(gspread.authorize(creds).open_by_key(SHEET_ID))

if __name__=='__main__':main()
