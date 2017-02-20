import unittest
import json
from todo_api import app

root_url = 'http://localhost:5000/'
class TodoAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def teardown(self):
        # no teardwon required since the database is a python dict
        pass

    #NB: these tests require running the app and don't teardown

    def test_empty_todo_get(self):
        #NB: won't do this testing until later in tutorial
        #NB: so the first time this test fails, then it gives "fetch bone" (below)
        rv = self.app.get('http://localhost:5000/todo/1')
        #NB: my weak way of testing for no response
        #NB: this is caused by a keyword error on the server, so it doesn't respond
        assert  'Remember the milk' in rv.data

    def test_todo_put(self):
        rv = self.app.put(root_url + 'todo/1', data=dict(
            data='fetch bone'))
        assert r'fetch bone' in rv.data
        assert json.loads(rv.data) == {'1' : 'fetch bone'}
        # rv = self.app.get(root_url + 'todo/1')
        # assert rv.data == {'1' : 'fetch bone'}

if __name__ == '__main__':
    unittest.main()
