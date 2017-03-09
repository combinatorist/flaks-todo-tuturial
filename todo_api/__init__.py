from collections import OrderedDict
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, fields, marshal_with

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello' : 'world'}

api.add_resource(HelloWorld, '/', '/hello')

todos = {}

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to charge for this resource')
parser.add_argument('data', type=str, help='Data to define this resource')

class TodoSimple(Resource):
    """HTPP for my todos"""
    def get(self, todo_id):
        try:
            return {todo_id: todos[todo_id]}
        except KeyError as e:
            return 'Internal Error'

    def put(self, todo_id):
        #NB: strict=True will return an error if request contains extra args
        args = parser.parse_args(strict=True)
        todos[todo_id] = args
        return {todo_id: todos[todo_id]}

resource_fields = {
    'task': fields.String,
    'uri': fields.Url('todo_ep')
}

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        #NB: This field will not be sent in the response, but why?
        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my todo', task='Remember the milk')


#NB: how do we make sure these never overlap -?
#NB: should I namespace this: 'todo/<string:todo_id>'?
api.add_resource(TodoSimple, '/todo/<int:todo_id>',
  endpoint='todo_ep_simple')

api.add_resource(Todo, '/todoDao',
  endpoint='todo_ep')

if __name__ == '__main__':
    app.run(debug=True)
