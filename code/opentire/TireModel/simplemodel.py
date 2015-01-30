__author__ = 'henningo'
from tiremodelbase import TireModelBase
import math

class SimpleModel(TireModelBase):

    def createmodel(self):
        self.ModelInfo = dict()
        self.Parameters = dict()

        self.ModelInfo['Name'] = 'SimpleModel'
        self.ModelInfo['Description'] = 'A simple tire model with load-sensitive cornering stiffness and grip levels'

        self.Parameters['csc'] = -0.45
        self.Parameters['csc_fz'] = -0.000001
        self.Parameters['mu'] = 1.4
        self.Parameters['mu_fz'] = -0.00002
        self.Parameters['mu_sa'] = -0.04

        self.Parameters['peak_range'] = 1.0

    def save(self, fname, data):
        return 'saving'

    def load(self, fname):
        return 'loading'

    def solve(self, state):
        fy = 0

        for i in xrange(-9,10):
            fy += self.calculateforce(state.SA - self.Parameters['peak_range'] * (i/10.0), state.FZ)

        state.FY = fy/len(xrange(-9,10))

        return state

    def getparameters(self):
        return self.Parameters

    def setparameters(self, params):
        """Must check that the keys are the same"""
        self.Parameters = params

        return True  # should return False if the parameter structure doesn't match required one

    def getmodelinfo(self):
        return self.ModelInfo

    def calculateforce(self, sa, fz):

        csc = self.Parameters['csc'] + self.Parameters['csc_fz'] * fz
        force = csc * fz * sa

        mu = self.Parameters['mu'] + self.Parameters['mu_fz'] * fz + self.Parameters['mu_sa'] * abs(sa)

        if abs(force) > abs(fz * mu):
            force = fz * mu * -math.copysign(1, sa)

        return force







