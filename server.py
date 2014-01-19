from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
from flask import make_response

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
    
@api.representation('application/rdf+xml')
def output_rdf_xml(data, code, headers=None):
    # e necessario implementar a funcao para converter para rdf+xml
    resp = make_response(data, code)
    resp.headers.extend(headers or {})
    return resp
    
#@api.representation('text/html')
#def output_html(data, code, headers=None):
#    # e necessario implementar a funcao para converter para rdf+xml
#    #data = "<html><body><h1>FUNCIONA</h1></body></html>"
#    resp = make_response(data, code)
#    resp.headers.extend(headers or {})
#    return resp


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


#https://github.com/RDFLib/rdflib-web/blob/master/rdflib_web/generic_endpoint.py

class Add(Resource):
    def post(self):        
        args = parser.parse_args()
        title = args['title']
        obj = LO(repository_lo[convert_to_uri(title)])
        obj.title = title
        return obj.resUri, 201
        
#curl http://localhost:5000/add \
#  --data-urlencode "title=Tessssteee 2222" \
#  --data "uri=testeee"
        
#    def get(self):
#        args = parser.parse_args()
#        uri = args['uri']
#        title = args['title']
#        obj = LO(repository_lo[str(uri)])
#        obj.title = title
#        return obj.resUri


class View(Resource):
    def get(self, uri):
        result = search.uri(uri)
        return abort_if_doesnt_exist(result, uri)

#    Apagar Objeto [NECESSARIO IMPLEMENTAR]
#    def delete(self, uri):
#        #abort_if_todo_doesnt_exist(uri)
#        #del [uri]
#        return 'Funcionou', 204

#    Atualizar Objeto [NECESSARIO IMPLEMENTAR]
#    def put(self, uri):
#        args = parser.parse_args()
#        title = {'title': args['title']}
#        #TODOS[uri] = title
#        return 'Funcionou', 201

class Search(Resource):
    def get(self):
        args = parser.parse_args()
        title = args['title']
        result = search.title(title)
        return result.read(), result.getcode()
        #return result.read(), result.getcode(), {'Content-Disposition' : 'attachment; filename=query-result.json'}

api.add_resource(Add, '/add')
api.add_resource(View, '/repository/<string:uri>')
api.add_resource(Search, '/search')


if __name__ == '__main__':
    app.run(debug=True)
