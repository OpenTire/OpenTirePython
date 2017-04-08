#!/usr/bin/env python

from opentire import OpenTire
from opentire.Core import TireState
from opentire.Core import TIRFile

import numpy as np

if __name__ == "__main__":

    # Initialize the tire model
    openTire = OpenTire()
    myTireModel = openTire.createmodel('PAC2002')

    # Initialize the tire state
    state = TireState()
    state['FZ'] = 1500
    state['IA'] = 0.0
    state['SR'] = 0.0
    state['SA'] = 0.0
    state['FY'] = 0.0
    state['V'] = 10.0
    state['P'] = 260000

    # Define the slip angle range
    slip_angles = np.arange(-12, 13, 1) * 3.14 / 180

    # Print out some pretty formatting
    print('OpenTire Slip Angle Sweep Demo\n')
    print('{0:>10} | {1:>10} | {2:>10} | {3:>10} | {4:>10}'
          .format('SA [deg]',
                  'FZ [N]',
                  'FY [N]',
                  'MZ [Nm]',
                  'MX [Nm]'))
    print('=' * 62)

    # Calculate and print out the tire model outputs
    for sa in slip_angles:
        state['SA'] = sa
        myTireModel.solve(state)
        print('{0:>10.0f} | {1:>10.0f} | {2:>10.1f} | {3:>10.1f} | {4:>10.1f}'
              .format(state['SA'] * 180 / 3.14,
                      state['FZ'],
                      state['FY'],
                      state['MZ'],
                      state['MX']))

