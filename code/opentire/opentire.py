__author__ = 'henningo'

from TireModel import *


class OpenTire:

    ModelTypes = dict()

    def createmodel(self, modelname):

        tm = None

        if modelname == 'Harty':
            print 'Harty not implemented'

        elif modelname == 'Simple':
            tm = SimpleModel()
            tm.createmodel()

        return tm


    def __init__(self):
        self.ModelTypes = \
            {'Simple': 'Simple Tire Model Implementation',
             'Harty': 'Harty Tire Model Implementation',
             'Pacejka96': 'Pacejka 96 Implementation'}

    def getmodellist(self):
        return self.ModelTypes