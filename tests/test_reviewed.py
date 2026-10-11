import unittest

from reviewed_identifications import REVIEWED, plan_updates

HEADER = ['quero_postar', 'obra', 'canal', 'data_postado', 'viewers', 'duracao', 'link', 'nomes_variantes']


class ReviewedTests(unittest.TestCase):
    def test_matches_video_after_rows_move_and_preserves_existing_values(self):
        rows = [HEADER,
                ['TRUE', 'Nome corrigido pelo usuário', 'Canal', '', '99', '', 'https://youtu.be/hNIp0R12Ujk', 'Manual'],
                ['FALSE', '', 'Outro', '', '', '', 'https://youtu.be/notknown123'],
                ['TRUE', '', 'Canal', '', '42', '', 'https://www.youtube.com/watch?v=xDfmMGD1mk4&feature=share', 'Alias manual']]
        before = [r[:] for r in rows]
        updates, notes = plan_updates(rows)
        self.assertEqual(updates, [{'range': 'B4', 'values': [['Earthen Keyboard Immortal']]}])
        self.assertEqual(notes[0][0], 4)
        self.assertEqual(rows, before)

    def test_handles_all_reviewed_ids_and_is_idempotent(self):
        rows = [HEADER] + [['FALSE', '', 'Canal', '', '', '', 'https://youtu.be/' + e['video_id'], ''] for e in REVIEWED]
        updates, notes = plan_updates(rows)
        self.assertEqual(len(notes), 10)
        for i, e in enumerate(REVIEWED, 1):
            rows[i][1] = e['title']
        self.assertEqual(plan_updates(rows), ([], []))

    def test_refuses_wrong_sheet_structure(self):
        with self.assertRaises(ValueError):
            plan_updates([['link', 'obra']])


if __name__ == '__main__':
    unittest.main()
