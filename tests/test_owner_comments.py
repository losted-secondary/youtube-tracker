import ast
from pathlib import Path
import re
import unicodedata
import unittest

# Carrega apenas as funções puras/consulta em teste sem exigir credenciais ou SDKs.
tree = ast.parse(Path('main.py').read_text(encoding='utf-8'))
names = {'OBRA_PATTERN', 'OBRA_BLACKLIST', 'extract_obra_from_text', 'fetch_owner_comment', 'extract_obra', 'extract_obra_fonte'}
selected = [node for node in tree.body if
            isinstance(node, ast.FunctionDef) and node.name in names or
            isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in names for t in node.targets)]
namespace = {'re': re, 'unicodedata': unicodedata, 'HttpError': RuntimeError}
exec(compile(ast.Module(body=selected, type_ignores=[]), 'main.py', 'exec'), namespace)


class FakeYoutube:
    def __init__(self, pages):
        self.pages = iter(pages)
        self.calls = 0

    def commentThreads(self):
        return self

    def list(self, **kwargs):
        self.calls += 1
        return self

    def execute(self):
        return next(self.pages)


def comment(author, text):
    return {'snippet': {'topLevelComment': {'snippet': {
        'authorChannelId': {'value': author}, 'textOriginal': text}}}}


class OwnerCommentTests(unittest.TestCase):
    def test_skips_owner_links_and_viewer_guess_then_finds_owner_title_next_page(self):
        yt = FakeYoutube([
            {'items': [comment('owner', 'Part 1: https://youtu.be/6mJUJjuzGcs'),
                       comment('viewer', 'Name: Wrong guess')], 'nextPageToken': 'next'},
            {'items': [comment('owner', 'Novel name: Real title')]},
        ])
        title = namespace['extract_obra'](yt, 'ycKWC4EEz6c', 'owner', "Manhwa name: It's in the comments")
        self.assertEqual(title, 'Real title')
        self.assertEqual(yt.calls, 2)

    def test_fonte_diz_de_onde_veio_o_nome(self):
        f = namespace['extract_obra_fonte']
        self.assertEqual(f(FakeYoutube([]), 'x', 'owner', 'Manhwa name: Shadow Slave'),
                         ('Shadow Slave', 'nome na descrição do vídeo'))
        yt = FakeYoutube([{'items': [comment('owner', 'Name: Shadow Slave')]}])
        self.assertEqual(f(yt, 'x', 'owner', 'sem nome'),
                         ('Shadow Slave', 'nome em comentário do próprio canal'))
        yt = FakeYoutube([{'items': [comment('viewer', 'Name: Palpite')]}])
        self.assertEqual(f(yt, 'x', 'owner', 'sem nome'), (None, None))

    def test_missing_owner_id_does_not_query_or_accept_viewers(self):
        yt = FakeYoutube([])
        self.assertIsNone(namespace['fetch_owner_comment'](yt, 'ycKWC4EEz6c', None))
        self.assertEqual(yt.calls, 0)


if __name__ == '__main__':
    unittest.main()
