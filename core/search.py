import pycurl
import cStringIO

from rdfalchemy.sparql.sesame2 import SesameGraph
from rdfalchemy import Literal
from rdflib import Namespace 

from utils import sesame_server_repository, repository_lo, dcterms


class SearchRepository():

    db = SesameGraph(sesame_server_repository)

    def uri(self, uri):
        """ """
        query = sesame_server_repository + '?query=describe<%s>' % (uri)
        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, query)
        c.setopt(c.WRITEFUNCTION, buf.write)
        c.setopt(c.HTTPHEADER, ['Accept: application/rdf+xml', 'Accept-Charset: UTF-8'])
        #c.setopt(c.HTTPHEADER, ['application/sparql-results+json', 'Accept-Charset: UTF-8'])
        c.perform()
        return buf.getvalue()

    def title(self, title):
        """ """
        query_string = 'PREFIX dcterms: <http://purl.org/dc/terms/> SELECT * WHERE { ?subject dcterms:title ?title FILTER regex(?title, "%s")}' % (title)
        result = self.db.query(query_string,  resultMethod="json", rawResults=True)
        return result

