import unittest
from production import bootstrap
from production_confirmations import prepare,ingest,replay,apply_answers,question_formula

def video(key,day):
 return {'id':key,'published':f'2026-10-{day:02}T18:00:00+00:00','date':f'2026-10-{day:02}','title':key}

class ConfirmationTests(unittest.TestCase):
 def channel(self,index=1):
  c=bootstrap()['channels'][index];prepare(c);return c
 def test_only_my_turn_asks_and_duplicate_feed_does_not_duplicate(self):
  c=self.channel();feed=[c['latest'],video('mine',18),video('partner',21)]
  ingest(c,feed);ingest(c,feed)
  self.assertEqual(len(c['events']),2)
  self.assertEqual([e['asked'] for e in c['events']],[True,False])
 def test_unanswered_survives_days_and_more_videos(self):
  c=self.channel();feed=[c['latest'],video('mine',18)]
  ingest(c,feed);feed+=[video('partner',21),video('mine2',24)];ingest(c,feed)
  self.assertEqual([e['id'] for e in c['events'] if e['asked']],['mine','mine2'])
  self.assertEqual(c['events'][0]['answer'],'Pendente')
 def test_late_no_replays_following_publications(self):
  c=self.channel();ingest(c,[c['latest'],video('first',18),video('second',21)])
  self.assertEqual(c['position'],2)
  apply_answers([c],{'first':'Não'})
  self.assertEqual(c['events'][0]['position'],2)
  self.assertEqual(c['events'][1]['expected'],1)
  self.assertTrue(c['events'][1]['asked'])
  self.assertEqual(c['position'],1)
 def test_no_keeps_my_turn_and_preserves_real_date(self):
  c=self.channel();ingest(c,[c['latest'],video('notmine',20)])
  apply_answers([c],{'notmine':'Não'})
  self.assertEqual(c['position'],2);self.assertEqual(c['latest']['date'],'2026-10-20')
 def test_yes_resets_juicy_then_waits_three(self):
  c=self.channel(2);feed=[c['latest']]+[video(str(i),18+i) for i in range(1,5)]
  ingest(c,feed);self.assertEqual([e['asked'] for e in c['events']],[False,False,False,True])
  apply_answers([c],{'4':'Sim'});self.assertEqual(c['position'],1)
 def test_answer_id_not_row_order(self):
  c=self.channel();ingest(c,[c['latest'],video('a',18),video('b',21),video('c',24)])
  apply_answers([c],{'c':'Sim','a':'Não'})
  self.assertEqual(c['events'][0]['answer'],'Não');self.assertEqual(c['events'][2]['answer'],'Sim')
 def test_question_uses_publication_date_and_current_day(self):
  formula=question_formula(22)
  self.assertIn('B22=TODAY()',formula);self.assertIn('B22=TODAY()-1',formula)
  self.assertIn('TEXT(B22;"dd/mm/yyyy")',formula)

if __name__=='__main__':unittest.main()
