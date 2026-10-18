import json,re,unittest
from types import SimpleNamespace
from unittest.mock import patch
from production import bootstrap,sync

class FakeSheet:
 def __init__(self,book,name):self.book=book;self.name=name
 def acell(self,a):return SimpleNamespace(value=self.book.cells.get((self.name,0,0)))
 def get(self,address):
  m=re.fullmatch(r'([A-Z]+)(\d+):([A-Z]+)(\d+)',address)
  def col(s):
   n=0
   for char in s:n=n*26+ord(char)-64
   return n-1
  a,r,b,t=m.groups();out=[]
  for row in range(int(r)-1,int(t)):
   vals=[self.book.cells.get((self.name,row,c),'') for c in range(col(a),col(b)+1)]
   while vals and vals[-1]=='':vals.pop()
   out.append(vals)
  while out and not out[-1]:out.pop()
  return out

class FakeBook:
 def __init__(self):
  self.ids={'Painel':1,'Cadastro':2,'_Controle':3,'_Publicacoes':4}
  self.named=[]
  self.cells={('_Controle',0,0):json.dumps(bootstrap())}
 def worksheet(self,n):return FakeSheet(self,n)
 def fetch_sheet_metadata(self):
  return {'namedRanges':self.named,'sheets':[{'properties':{'title':n,'sheetId':i,'gridProperties':{'rowCount':1000}}} for n,i in self.ids.items()]}
 def batch_update(self,body):
  names={i:n for n,i in self.ids.items()}
  for req in body['requests']:
   if 'deleteDimension' in req:
    d=req['deleteDimension']['range'];name=names[d['sheetId']];start=d['startIndex'];end=d['endIndex'];size=end-start
    self.cells={(n,r-size if n==name and r>=end else r,c):v for (n,r,c),v in self.cells.items() if not (n==name and start<=r<end)}
    for item in self.named:
     if item['range']['startRowIndex']>=end:item['range']['startRowIndex']-=size
   if 'insertDimension' in req:
    d=req['insertDimension']['range'];name=names[d['sheetId']];start=d['startIndex'];size=d['endIndex']-start
    self.cells={(n,r+size if n==name and r>=start else r,c):v for (n,r,c),v in self.cells.items()}
    for item in self.named:
     if item['range']['startRowIndex']>=start:item['range']['startRowIndex']+=size
   if 'updateCells' not in req:continue
   d=req['updateCells'];start=d['start'];name=names[start['sheetId']]
   for ri,row in enumerate(d['rows']):
    for ci,cell in enumerate(row['values']):
     value=next(iter(cell.get('userEnteredValue',{}).values()),'')
     self.cells[name,start['rowIndex']+ri,start['columnIndex']+ci]=value
  return {}

class SyncTests(unittest.TestCase):
 def test_empty_queue_shrinks_without_erasing_channel_header(self):
  book=FakeBook();book.named=[{'name':'Confirmacoes','range':{'startRowIndex':12}}, {'name':'TabelaCanais','range':{'startRowIndex':20}}]
  book.cells['Painel',20,0]='Canal'
  feeds={c['channel_id']:[c['latest']] for c in bootstrap()['channels']}
  with patch('production.fetch',side_effect=lambda cid:feeds[cid]):sync(book)
  self.assertEqual(book.cells['Painel',15,0],'Canal')
  self.assertEqual(book.named[1]['range']['startRowIndex'],15)

 def test_top_confirmations_grow_and_keep_answers(self):
  book=FakeBook()
  book.named=[{'name':'Confirmacoes','range':{'startRowIndex':12}}, {'name':'TabelaCanais','range':{'startRowIndex':14}}]
  book.cells['Painel',14,0]='Canal'
  base=bootstrap();feeds={c['channel_id']:[c['latest']] for c in base['channels']}
  feeds[base['channels'][1]['channel_id']].append({'id':'new-video','published':'2026-10-18T10:00:00+00:00','date':'2026-10-18','title':'Video'})
  with patch('production.fetch',side_effect=lambda cid:feeds[cid]):
   feeds[base['channels'][3]['channel_id']].append({'id':'another-video','published':'2026-10-18T10:00:00+00:00','date':'2026-10-18','title':'Video'})
   sync(book)
   self.assertEqual(book.cells['Painel',12,10],'new-video')
   self.assertEqual(book.cells['Painel',15,0],'Canal')
   self.assertEqual(book.cells['Painel',17,8],'A confirmar')
   book.cells['Painel',12,4]='Sim'
   sync(book)
   self.assertEqual(book.cells['Painel',12,10],'another-video')
   self.assertEqual(json.loads(book.cells['_Controle',0,0])['queue_count'],1)
   self.assertEqual(book.cells['Painel',17,8],'Eu')

 def test_detect_save_reload_and_confirm_no_without_duplicate(self):
  book=FakeBook();base=bootstrap();feeds={c['channel_id']:[c['latest']] for c in base['channels']}
  feeds[base['channels'][1]['channel_id']].append({'id':'new-video','published':'2026-10-18T10:00:00+00:00','date':'2026-10-18','title':'Novo vídeo'})
  with patch('production.fetch',side_effect=lambda cid:feeds[cid]):
   sync(book)
   self.assertEqual(book.cells['Painel',21,4],'Pendente')
   self.assertEqual(book.cells['Painel',21,10],'new-video')
   self.assertEqual(book.cells['Cadastro',7,5],1)
   self.assertEqual(book.cells['Painel',11,8],'A confirmar')
   book.cells['Painel',21,4]='Não'
   sync(book)
   self.assertEqual(book.cells['Cadastro',7,5],2)
   self.assertEqual(book.cells['Painel',21,4],'')
   self.assertEqual(book.cells['Painel',21,10],'')
   state=json.loads(book.cells['_Controle',0,0]);self.assertEqual(state['queue_count'],0)
   self.assertNotIn('events',state['channels'][1])
   sync(book)
   self.assertEqual(book.cells['Cadastro',7,5],2)
   self.assertEqual(json.loads(book.cells['_Controle',0,0])['queue_count'],0)

if __name__=='__main__':unittest.main()
