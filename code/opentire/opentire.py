__author__ = 'henningo'

from opentire.TireModel import *


class OpenTire:

    ModelTypes = dict()

    def createmodel(self, modelname):

        tm = None

        if modelname == 'Harty':
            tm = None #Change to address print functionaility issues in Py2/Py3

        elif modelname == 'PAC2002':
            tm = PAC2002()

        else:
            return None  # Of we cam

        tm.createmodel()
        return tm

    def __init__(self):
        self.ModelTypes = \
            {'PAC2002': 'Pacejka 2002',
             'Fiala': 'Fiala Tire Model Implementation'}

    def getmodellist(self):
        return self.ModelTypes
