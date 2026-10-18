"""Controle pessoal em uma planilha separada; nenhuma integração com Discord."""
import json
import os
from datetime import date, datetime

import gspread
from google.oauth2.service_account import Credentials
from production_core import BRT, initial, fetch, apply_feed

SHEET_ID='1Rq9QIEQIm2MSBVl9SDTRTa8QqpuhGbRQGZ_OnK1pr4E'
STATE_TAB='_Controle'
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
 # Coletar antes de ler comandos reduz a janela de concorrência com edições humanas.
 feeds={}
 for c in state['channels']:
  try:feeds[c['handle']]=fetch(c['channel_id'])
  except Exception as exc:
   print(f"[produção] {c['name']}: {type(exc).__name__}")
 corrections=book.worksheet('Painel').get('J11:J15')
 requests=[]
 for i,c in enumerate(state['channels']):
  correction=corrections[i][0] if i<len(corrections) and corrections[i] else ''
  if raw:correct_author(c,correction)
  c['error']=None
  if c['handle'] in feeds:
   apply_feed(c,feeds[c['handle']])
   c['last_checked']=datetime.now(BRT).isoformat(timespec='seconds')
  else:c['error']='Falha na consulta. Dados anteriores preservados.'
  r=6+i;t=10+i
  latest=c['latest']
  serial=(date.fromisoformat(latest['date'])-date(1899,12,30)).days if latest else None
  requests.append(put(sheets['Cadastro'],r,2,[[serial,c['minimum'],c['people'],c['position']]]))
  requests.append(put(sheets['Cadastro'],r,9,[[c['maximum']]]))
  requests.append(put(sheets['Painel'],t,9,[[author(c)]]))
  c['displayed_author']=author(c)
  requests.append(put(sheets['Painel'],25+i,0,[[c['name'],c['last_checked'][8:10]+'/'+c['last_checked'][5:7]+' '+c['last_checked'][11:16] if c['last_checked'] else 'Não consultado',latest['id'] if latest else '',c['error'] or 'Atualizado']]))
  if latest:
   requests.append(put(sheets['Painel'],25+i,2,[[f'=HYPERLINK("https://www.youtube.com/watch?v={latest["id"]}";"Abrir vídeo")']],True))
  # Os vídeos mais antigos que a âncora não avançam o rodízio; limita tamanho do estado.
  if len(c['seen'])>1000:c['seen']=[e['id'] for e in feeds.get(c['handle'],[])]+[latest['id']]
 # Estado e células são gravados juntos: uma falha não avança só metade do controle.
 requests.append(put(sheets[STATE_TAB],0,0,[[json.dumps(state,ensure_ascii=False,separators=(',',':'))]]))
 book.batch_update({'requests':requests})
 print('[produção] 5 canais atualizados; datas em Brasília e estado persistido no Sheets.')

def main():
 creds=Credentials.from_service_account_info(json.loads(os.environ['GOOGLE_CREDENTIALS_JSON']),scopes=['https://www.googleapis.com/auth/spreadsheets'])
 sync(gspread.authorize(creds).open_by_key(SHEET_ID))

if __name__=='__main__':main()
