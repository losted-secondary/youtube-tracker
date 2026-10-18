import unittest
from datetime import datetime,timedelta,date
from production import bootstrap,correct_author,author
from production_core import apply_feed,BRT

def entry(i,published):
 return dict(id=i,published=published,date=datetime.fromisoformat(published).astimezone(BRT).date().isoformat())

class ProductionTests(unittest.TestCase):
 def test_initial_turns(self):
  self.assertEqual([c['position'] for c in bootstrap()['channels']],[1,2,1,2,2])
 def test_late_post_resets_from_actual_day(self):
  c=bootstrap()['channels'][0]
  old=c['latest'];new=entry('late','2026-10-21T02:59:00+00:00')
  apply_feed(c,[old,new])
  self.assertEqual(c['latest']['date'],'2026-10-20')
  self.assertEqual(date.fromisoformat(c['latest']['date'])+timedelta(days=2),date(2026,10,22))
 def test_correct_old_author_before_new_video(self):
  c=bootstrap()['channels'][1];c['displayed_author']='Parceiro 1'
  correct_author(c,'Eu');apply_feed(c,[c['latest'],entry('new','2026-10-18T10:00:00+00:00')])
  self.assertEqual(c['position'],2)
 def test_correction_does_not_change_publication_date(self):
  c=bootstrap()['channels'][1];c['displayed_author']='Parceiro 1'
  original=c['latest'].copy();correct_author(c,'Eu')
  self.assertEqual(c['latest'],original)
 def test_juicy_three_partners_then_me(self):
  c=bootstrap()['channels'][2];feed=[c['latest']]
  for i in range(3):feed.append(entry(str(i),f'2026-10-{20+i*3}T18:00:00+00:00'))
  apply_feed(c,feed);self.assertEqual(c['position'],4)
  apply_feed(c,feed);self.assertEqual(c['position'],4)
  feed.append(entry('mine','2026-10-29T20:00:00+00:00'));apply_feed(c,feed)
  self.assertEqual(c['position'],1)
if __name__=='__main__':unittest.main()
