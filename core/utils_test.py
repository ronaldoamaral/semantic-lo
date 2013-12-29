from utils import *
from LO import *

# lo e um namespace e ronaldo e o final da uri
#lo1 = LO(repository_lo.Teste)
#lo1.title = "Teste de Titulo"

# No em branco com Titulo
#lo2 = LO(title='Teste de Titulo2')

# Teste com hifen
#lo3 = LO(repository_lo['teste-3'], title='Teste de Titulo2')

# Passando URI explicitamente
#lo4 = LO(URIRef('http://example.com/lo#TestepassandoString'))

#Adicionando de sem mapeamento
#rdfSubject.db.add((URIRef("http://example.com/lo#Teste2"), RDF.type, lom.LearningObject))

#Adicionando No em Branco
#node = BNode()
#rdfSubject.db.add((node, RDF.type, lom.LearningObject))
import pdb;pdb.set_trace()
objects = LO.filter_by()

for item in objects:
 print item

#obj_set = set([item for item in objects])
