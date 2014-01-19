from rdflib import Namespace, BNode, URIRef, RDF

from rdfalchemy import rdfSubject
from rdfalchemy.sparql.sesame2 import SesameGraph

#Definindo Namespaces
repository_lo = Namespace ('http://localhost:5000/repository/')

rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema')
xsd = Namespace('<http://www.w3.org/2001/XMLSchema#>')
dcterms = Namespace('http://purl.org/dc/terms/')    
lom= Namespace("http://ltsc.ieee.org/rdf/lomv1p0/lom#")
lomvoc = Namespace('http://ltsc.ieee.org/rdf/lomv1p0/vocabulary#')
lomterms = Namespace('http://ltsc.ieee.org/rdf/lomv1p0/terms#')
foaf = Namespace('http://xmlns.com/foaf/0.1/')

# Configurando Base de Dados Sesame
sesame_server_repository = 'http://localhost:8080/openrdf-sesame/repositories/teste'

rdfSubject.db = SesameGraph(sesame_server_repository)

def convert_to_uri(title=''):
    uri = title
    return str(uri)

