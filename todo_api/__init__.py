from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello' : 'world'}

api.add_resource(HelloWorld, '/', '/hello')

todos = {}

class TodoSimple(Resource):
    """HTPP for my todos"""
    def get(self, todo_id):
        try:
            return {todo_id: todos[todo_id]}
        except KeywordError as e:
            return 'Internal Error'

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

#NB: how do we make sure these never overlap -?
#NB: should I namespace this: 'todo/<string:todo_id>'?
api.add_resource(TodoSimple, '/todo/<int:todo_id>', endpoint='todo_ep')

if __name__ == '__main__':
    app.run(debug=True)
