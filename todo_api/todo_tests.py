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
        # self.assertRaises(Exception,
        rv = self.app.get('http://localhost:5000/todo/1')
        # )
        #NB: this is caused by a keyword error on the server, so it doesn't respond
        #NB: my weak way of testing for no response
        assert 'Internal Error' in rv.data 

    def test_todo_put(self):
        rv = self.app.put(root_url + 'todo/2', data=dict(
            data='fetch bone'))
        assert r'fetch bone' in rv.data
        assert json.loads(rv.data)['2']['data'] == 'fetch bone'
        assert json.loads(rv.data) == {'2' : {
            'rate' : None, 'data' : 'fetch bone'
        }}
        # rv = self.app.get(root_url + 'todo/1')
        # assert rv.data == {'1' : 'fetch bone'}

    def test_todo_put_extra_arg(self):
        rv = self.app.put(root_url + 'todo/3', data=dict(
            data='drop the beat',
            rate=5,
            pet='dragon',
        ))
        assert r'message' in rv.data
        assert r'"Unknown arguments: pet"' in rv.data


if __name__ == '__main__':
    unittest.main()
