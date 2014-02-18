semantic-lo
===========

Aplicação para anotação semântica de objetos de aprendizagem


Dependencias

flask
flask-restful
RDFAlchemy


Sesame

https://github.com/dibaunaumh/ikana1010/wiki/RDFAlchemy-&-Sesame-HOWTO
https://github.com/ametaireau/flask-rest

https://github.com/ametaireau

https://github.com/ametaireau/semantic-bookclub/blob/master/app/model.py


Pubby

http://wifo5-03.informatik.uni-mannheim.de/pubby/




Utilização
 
Inserido

curl -X POST http://localhost:5000/add --data "title=SemanticLO"

Acessando informações

curl -X GET http://localhost:5000/control --data 'uri=http://localhost:8080/semanticlo/resource/SemanticLO'
 

Apagando

curl -X DELETE http://localhost:5000/control --data 'uri=http://localhost:8080/semanticlo/resource/SemanticLO'


Buscando 

curl http://localhost:5000/search?title=SemanticLO



Acessando Informações a partir do Pubby

curl --header "Accept: application/rdf+xml" http://localhost:8080/semanticlo/data/SemanticLO



Corrigindo Erro de Codificação na Biblioteca RDFAlchemy

É necessário acrescentar no arquivo /rdfalchemy/sparql/sesame2.py

# -*- coding: utf-8 -*-

E no métido descrito abaixo é necessário codificar a string "data_str" para UTF-8 

def add(self, (s, p, o), context=None):
        """Add a triple with optional context"""
        url = self.url+'/statements'
        ctx = context or self.context
        if ctx:
            url = url+"?"+urlencode(dict(context=ctx))
        req = Request(url)
        data_str = "%s %s %s .\n" % (s.n3(), p.n3(), o.n3())
        ######## PATCH ############  
        req.data = data_str.encode('utf8')
        req.add_header('Content-Type','text/rdf+n3')
        ##########################
        try:
            result = urlopen(req).read()
        except HTTPError, e:
            if e.code == 204:
                return
            else:
                log.error(e)
        return result

