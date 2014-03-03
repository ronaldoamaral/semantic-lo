 # -*- coding: utf-8 -*-

from utils import *
from rdfalchemy.descriptors import *
from rdfalchemy.orm import mapper

class LO(rdfSubject):
  """ Representacao de Objeto de Aprendizagem """
  
  rdf_type = lom.LearningObject
  #learning_resource_type = rdfMultiple(lom.)
  title = rdfSingle(dcterms.title)
  identifier = rdfSingle(dcterms.identifier)
  description = rdfSingle(dcterms.description)
  subject = rdfMultiple(dcterms.subject)

mapper(LO)
