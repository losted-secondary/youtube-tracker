"""Autoria por vídeo, com respostas tardias e recálculo do rodízio."""
from datetime import datetime

def prepare(channel):
    channel.setdefault('base_position', channel['position'])
    channel.setdefault('events', [])

def ingest(channel, entries):
    prepare(channel)
    known=set(channel['seen']) | {e['id'] for e in channel['events']}
    latest=channel['latest']
    cutoff=datetime.fromisoformat(latest['published']) if latest else None
    gap=bool(latest and latest['id'] not in {e['id'] for e in entries})
    for entry in sorted(entries,key=lambda e:(datetime.fromisoformat(e['published']),e['id'])):
        if entry['id'] in known:continue
        known.add(entry['id'])
        if cutoff and datetime.fromisoformat(entry['published'])<cutoff:continue
        channel['events'].append({**entry,'answer':'Pendente','asked':False,'gap':gap})
        gap=False
        channel['latest']=entry
    channel['seen']=list(dict.fromkeys([e['id'] for e in entries]+[channel['latest']['id']]))
    replay(channel)

def replay(channel):
    prepare(channel)
    position=channel['base_position']
    for event in channel['events']:
        if event.get('gap'):position=None
        expected=position%channel['people']+1 if position is not None else None
        event['expected']=expected
        # Uma pergunta já feita permanece vinculada ao vídeo, mesmo após correções.
        event['asked']=event.get('asked',False) or expected==1 or expected is None
        answer=event.get('answer','Pendente')
        if answer=='Sim':position=1
        elif answer=='Não':
            # Não foi meu vídeo: minha vez continua pendente após o parceiro.
            position=channel['people'] if expected==1 else expected
        else:position=expected
        event['position']=position
    channel['position']=position

def apply_answers(channels, answers):
    for channel in channels:
        for event in channel.get('events',[]):
            answer=answers.get(event['id'])
            if answer in ('Sim','Não','Pendente'):event['answer']=answer
        replay(channel)

def question_formula(row):
    return (f'=IF(B{row}=TODAY();"Postaram hoje. Foi você?";'
            f'IF(B{row}=TODAY()-1;"Postaram ontem. Foi você?";'
            f'"Postaram em "&TEXT(B{row};"dd/mm/yyyy")&". Foi você?"))')
