import os
import unittest
from datetime import datetime, timezone
from unittest.mock import patch

import yt_dlp
from collect_evidence import collect, select_recent_missing


class EvidenceTests(unittest.TestCase):
    def test_recent_selection_ignores_old_named_and_invalid_rows(self):
        header = ['quero_postar', 'obra', 'canal', 'data_postado', 'viewers', 'duracao', 'link']
        rows = [header,
            ['', '', '', '01/01/2026 - 10:00', '', '', 'https://youtu.be/aaaaaaaaaaa'],
            ['', '', '', '10/10/2026 - 10:00', '', '', 'https://youtu.be/bbbbbbbbbbb'],
            ['', 'Known', '', '11/10/2026 - 10:00', '', '', 'https://youtu.be/ccccccccccc'],
            ['', '', '', 'invalid', '', '', 'https://youtu.be/ddddddddddd'],
            ['', '', '', '11/10/2026 - 09:00', '', '', 'https://youtu.be/eeeeeeeeeee']]
        now = datetime(2026, 10, 11, 18, tzinfo=timezone.utc)
        self.assertEqual(select_recent_missing(rows, now), 'eeeeeeeeeee')
        with self.assertRaises(ValueError):
            select_recent_missing(rows[:2], now)

    def test_download_failure_uses_api_without_claiming_frames(self):
        fallback = {'collection_method': 'youtube_api', 'frames': [], 'transcript': ''}
        with patch.dict(os.environ, {'YOUTUBE_API_KEY': 'test-only'}), \
             patch('collect_evidence.collect_ytdlp', side_effect=yt_dlp.utils.DownloadError('blocked')), \
             patch('collect_evidence.collect_api', return_value=fallback) as api:
            self.assertEqual(collect('bbbbbbbbbbb', None), fallback)
            api.assert_called_once_with('bbbbbbbbbbb')

    def test_download_failure_without_api_key_still_fails(self):
        with patch.dict(os.environ, {}, clear=True), \
             patch('collect_evidence.collect_ytdlp', side_effect=yt_dlp.utils.DownloadError('blocked')):
            with self.assertRaises(yt_dlp.utils.DownloadError):
                collect('bbbbbbbbbbb', None)
