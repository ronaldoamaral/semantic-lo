from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

from core.LO import *
from core.utils import repository_lo

app = Flask(__name__)
api = Api(app)


#def abort_if_todo_doesnt_exist(resource_id):
#    if resource_id not in TODOS:
#        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('uri', type=str)
parser.add_argument('title', type=str)



class Add(Resource):
    def post(self):        
        args = parser.parse_args()
        uri = args['uri']
        title = args['title']
        obj = LO(repository_lo[str(uri)])
        obj.title = title
        return obj.resUri, 201
        
#    def get(self):
#        args = parser.parse_args()
#        uri = args['uri']
#        title = args['title']
#        obj = LO(repository_lo[str(uri)])
#        obj.title = title
#        return obj.resUri


class Control(Resource):
    def get(self, uri):
        #abort_if_todo_doesnt_exist(uri)
        obj = LO.filter_by()
        return obj.title

    def delete(self, uri):
        #abort_if_todo_doesnt_exist(uri)
        #del [uri]
        return 'Funcionou', 204

    def put(self, uri):
        args = parser.parse_args()
        title = {'title': args['title']}
        #TODOS[uri] = title
        return 'Funcionou', 201




api.add_resource(Add, '/add')
api.add_resource(Control, '/repository/<string:uri>')


if __name__ == '__main__':
    app.run(debug=True)
