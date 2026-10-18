"""Controle pessoal: RSS público, rodízio por ID de vídeo e Excel compacto."""
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from urllib.request import Request, urlopen

BRT=timezone(timedelta(hours=-3))
CHANNELS=[
 ('SaikoManhwaa','Saiko Manhwa','UCHk4joypx43Nq6saxqpfnoQ',2,2,1),
 ('MamoruManhwa','Mamoru Manhwa','UCjtG_KmctknonQtG5M_RUDg',3,3,2),
 ('JuicyMangas','Juicy Mangas','UCUnLH9qyXBI8ijs9Kmbt9Ng',2,3,4),
 ('MalfoidManhwa','Malfoid Manhwa','UCBn1Z7j1_cm0UTQjIdOTsXg',3,3,2),
 ('StopwatchStories1','Stopwatch Stories','UCo0ymi41VW8Uw8yphn_40eA',3,3,2),
]
def initial():
 return {'channels':[dict(handle=h,name=n,channel_id=i,minimum=lo,maximum=hi,people=k,
     position=1 if k==1 else None,seen=[],latest=None,last_checked=None,error=None)
     for h,n,i,lo,hi,k in CHANNELS]}

def fetch(channel_id):
 url='https://www.youtube.com/feeds/videos.xml?channel_id='+channel_id
 with urlopen(Request(url,headers={'User-Agent':'PersonalChannelTracker/1.0'}),timeout=25) as r:
  root=ET.fromstring(r.read())
 ns={'a':'http://www.w3.org/2005/Atom','yt':'http://www.youtube.com/xml/schemas/2015'}
 entries=[]
 for e in root.findall('a:entry',ns):
  published=e.findtext('a:published',namespaces=ns)
  dt=datetime.fromisoformat(published.replace('Z','+00:00'))
  if dt>datetime.now(timezone.utc):continue
  entries.append(dict(id=e.findtext('yt:videoId',namespaces=ns),published=published,
                      date=dt.astimezone(BRT).date().isoformat(),title=e.findtext('a:title',namespaces=ns)))
 if not entries:raise ValueError('Feed sem vídeos publicados; mantendo o último estado.')
 return sorted(entries,key=lambda x:(datetime.fromisoformat(x['published']),x['id']))

def apply_feed(c,entries):
 """Primeira consulta só estabelece a base. ID repetido nunca avança a fila."""
 seen=set(c['seen'])
 latest=c['latest']
 if latest is None:
  c['latest']=entries[-1]
  c['seen']=list(dict.fromkeys(e['id'] for e in entries))
  return
 if latest['id'] not in {e['id'] for e in entries}:
  # Feed limitado: não adivinhar quantas publicações ficaram fora da janela.
  c['position']=1 if c['people']==1 else None
  c['error']='Último vídeo conhecido saiu do feed. Confirme novamente o rodízio.'
 old_time=datetime.fromisoformat(latest['published'])
 for entry in entries:
  if entry['id'] in seen:continue
  seen.add(entry['id'])
  if datetime.fromisoformat(entry['published'])<old_time:continue
  if c['position'] is not None:c['position']=c['position']%c['people']+1
  c['latest']=entry
 c['seen']=sorted(seen)
