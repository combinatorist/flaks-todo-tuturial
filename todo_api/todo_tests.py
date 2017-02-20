import unittest
from todo_api import app
from requests import get, put
from flask import url_for

root_url = 'http://localhost:5000/'
class TodoAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def teardown(self):
        # no teardwon reuired since the database is a python dict
        pass

    def test_empty_todo_get(self):
        with app.app_context():
            rv = get(root_url + 'not_todo')
            #NB: my weak way of testing for no response
            #NB: this is caused by a keyword error on the server, so it doesn't response
            assert  str(rv) == '<Response [500]>'

    def test_todo_put(self):
        rv = put(root_url + 'todox', data={'data' : 'fetch bone'}).json()
        assert rv == {'todox' : 'fetch bone'}
        assert get(root_url + 'todox').json() == {'todox' : 'fetch bone'}

if __name__ == '__main__':
    unittest.main()
