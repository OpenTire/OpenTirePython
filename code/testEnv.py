__author__ = 'henningo'

from opentire import OpenTire
from opentire.Core import TireState



state = TireState()
OpenTire = OpenTire()

myTiremodel = OpenTire.createmodel('Simple')


for sa in xrange(-50, 50):
    state.FZ = 5000
    state.SA = sa/10.0

    print myTiremodel.solve(state).FY
