__author__ = 'henningo'
import pylab as plt

import numpy as np

from opentire import OpenTire
from opentire.Core import TireState
from opentire.Core import TIRFile

OpenTire = OpenTire()

myTiremodel = OpenTire.createmodel('PAC2002')

##Or you can load in a tir file
#tir_file = TIRFile()
#fname = 'C:/myfile.tir'
#myTiremodel = tir_file.load(fname)

state = TireState()

state['FZ'] = 1500
state['IA'] = 0.0
state['SR'] = 0.0
state['SA'] = 0.0
state['FY'] = 0.0
state['V'] = 10.0
state['P'] = 260000


xchan = 'SA'
ychan = 'FY'

loads = [500, 1000, 1500]

slip_angles = np.arange(-12, 12, 0.1) * 0.01


i = 1

for fz in loads:

    yvals = []

    for  in slip_angles:
        state[xchan] = float(sa_val)
        state['FZ'] = float(fz)
        resultstate = myTiremodel.solve(state)
        sa_val = resultstate[xchan]
        yval = resultstate[ychan]

        yvals = np.append(yvals, yval)

    plt.plot(xvals*180/3.14, yvals, label=fz)

plt.show()




