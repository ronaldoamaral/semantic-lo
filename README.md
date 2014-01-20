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
 

Apagando

curl -X DELETE http://localhost:5000/control --data 'uri=<http://localhost:8080/resource/Moodle>'


Buscando 

curl http://localhost:5000/search?title=SemanticLO



Acessando Informações a partir do Pubby

curl --header "Accept: application/rdf+xml" http://localhost:8080/semanticlo/data/SemanticLO

