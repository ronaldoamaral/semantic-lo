import simplejson as json

from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource, request
from flask import make_response
from flask import render_template
from flask import redirect, url_for

from core.LO import *
from core.search import SearchRepository
from core.utils import repository_lo, convert_to_uri

app = Flask(__name__)
api = Api(app)

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(data, code)
    resp.headers.extend(headers or {})
    return resp

@api.representation('text/html')
def output_html(data, code, headers=None):
    resp = make_response(data, code)
    resp.headers.extend(headers or {})
    return resp

# Instanciando a maquina de Busca
search = SearchRepository()

def abort_if_doesnt_exist(result, uri):
    if result:
        return result, 200
    else:
        abort(404, message="Resource doesn't exist".format(uri))

parser = reqparse.RequestParser()
parser.add_argument('uri', type=str)
parser.add_argument('title', type=str)
parser.add_argument('identifier', type=str)
parser.add_argument('callback', type=str)


class Add(Resource):
    def post(self):        
        args = parser.parse_args()
        title = args['title']
        identifier = args['identifier']
        obj = LO(repository_lo[convert_to_uri(title)])
        obj.title = title
        obj.identifier = identifier
        return '{"status": "success", "data": {"uri": "' + obj.resUri +'" }, "message": "null" }', 201
        
class Control(Resource):
    def get(self):
        args = parser.parse_args()
        uri = args['uri']
        result = search.uri(uri)
        return abort_if_doesnt_exist(result, uri)
        
#    Apagar Objeto [NECESSARIO IMPLEMENTAR]
    def delete(self):
        args = parser.parse_args()
        uri = args['uri']
#        #abort_if_todo_doesnt_exist(uri)
#        #del [uri]
        return 'Funcionou'

    def post(self): 
        uri = request.json['uri']
        description = request.json['description']        
        obj = LO('<'+uri+'>')
        obj.description =  description
        # Adicionar os outros metadados.
        return '{"status": "success", "data": { }, "message": "null" }', 202

class Search(Resource):
    def get(self):
        args = parser.parse_args()
        title = args['title']
        result = search.title(title)
        return result.read(), result.getcode()
        
class AddMetadataView(Resource):
    def get(self):
        args = parser.parse_args()
        uri = args['uri']
        callback = args['callback']
        return render_template('index.html', uri = uri, callback = callback)
        

api.add_resource(Add, '/add')
api.add_resource(Control, '/control')
api.add_resource(Search, '/search')
api.add_resource(AddMetadataView, '/addmetadata')


if __name__ == '__main__':
    app.run(debug=True)
