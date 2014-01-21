import unicodedata
import re

from rdflib import Namespace, BNode, URIRef, RDF

from rdfalchemy import rdfSubject
from rdfalchemy.sparql.sesame2 import SesameGraph

#Definindo Namespaces
repository_lo = Namespace ('http://localhost:8080/semanticlo/resource/')

rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema')
xsd = Namespace('<http://www.w3.org/2001/XMLSchema#>')
dcterms = Namespace('http://purl.org/dc/terms/')    
lom= Namespace("http://ltsc.ieee.org/rdf/lomv1p0/lom#")
lomvoc = Namespace('http://ltsc.ieee.org/rdf/lomv1p0/vocabulary#')
lomterms = Namespace('http://ltsc.ieee.org/rdf/lomv1p0/terms#')
foaf = Namespace('http://xmlns.com/foaf/0.1/')

# Configurando Base de Dados Sesame
sesame_server_repository = 'http://localhost:8080/openrdf-sesame/repositories/semanticlo'

rdfSubject.db = SesameGraph(sesame_server_repository)
    
def convert_to_uri(title=''):
    unicode_title = unicode(title)
    r = unicodedata.normalize('NFKD',unicode_title).encode('ascii','ignore')
    r = unicode(re.sub('[^\w\s-]','',unicode_title).strip().lower())
    return re.sub('[-\s]+','-',r)

