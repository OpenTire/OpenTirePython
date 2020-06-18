__author__ = 'henningo'
from ..tiremodelbase import TireModelBase
from ..solvermode import SolverMode
import math
import numpy as np
from opentire.TireModel.PAC2002.PAC2002_Core import PAC2002_Core

class PAC2002(TireModelBase):

    def createmodel(self):
        self.ModelInfo = dict()
        self.Coefficients = dict()

        self.ModelInfo['Name'] = 'PAC2002'
        self.ModelInfo['Description'] = 'An implementation of Pacejka 2002 as described in the First Editions of Tire and Vehicle Dynamics'

        # Create an instance for internal calcs
        # These are typically called multiple times in the code
        self.Core = PAC2002_Core()

        # General Coefficients
        self.Coefficients['FNOMIN'] = 4850
        self.Coefficients['UNLOADED_RADIUS'] = 0.344
        self.Coefficients['LONGVL'] = 16.6

        # General Scaling Factors
        self.Coefficients['LFZ0'] = 1.0
        self.Coefficients['LCZ'] = 1.0

        # Pure Longitudinal Scaling Factors
        self.Coefficients['LCX'] = 1.0
        self.Coefficients['LMUX'] = 1.0
        self.Coefficients['LEX'] = 1.0
        self.Coefficients['LKX'] = 1.0
        self.Coefficients['LHX'] = 1.0
        self.Coefficients['LVX'] = 1.0
        self.Coefficients['LGAX'] = 1.0

        # Pure Lateral Scaling Factors
        self.Coefficients['LCY'] = 1.0
        self.Coefficients['LMUY'] = 1.0
        self.Coefficients['LEY'] = 1.0
        self.Coefficients['LKY'] = 1.0
        self.Coefficients['LHY'] = 1.0
        self.Coefficients['LVY'] = 1.0
        self.Coefficients['LGAY'] = 1.0

        # Pure Aligning Moment Scaling Factors
        self.Coefficients['LTR'] = 1.0
        self.Coefficients['LRES'] = 1.0
        self.Coefficients['LGAZ'] = 1.0

        # Combined Scaling Factors
        self.Coefficients['LXAL'] = 1.0
        self.Coefficients['LYKA'] = 1.0
        self.Coefficients['LVYKA'] = 1.0
        self.Coefficients['LS'] = 1.0

        # Overturning Scaling Factors
        self.Coefficients['LMX'] = 1.0
        self.Coefficients['LVMX'] = 1.0

        # Rolling Resistance Factors
        self.Coefficients['LMY'] = 1.0

        #Relaxation Scaling Factors
        self.Coefficients['LSGKP'] = 1.0
        self.Coefficients['LSGAL'] = 1.0

        # Pure Lateral Coefficients
        self.Coefficients['PCY1'] = 1.3507
        self.Coefficients['PDY1'] = 1.0489
        self.Coefficients['PDY2'] = -0.18033
        self.Coefficients['PDY3'] = -2.8821
        self.Coefficients['PEY1'] = -0.0074722
        self.Coefficients['PEY2'] = -0.0063208
        self.Coefficients['PEY3'] = -9.9935
        self.Coefficients['PEY4'] = -760.14
        self.Coefficients['PKY1'] = -21.92
        self.Coefficients['PKY2'] = 2.0012
        self.Coefficients['PKY3'] = -0.024778
        self.Coefficients['PHY1'] = 0.0026747
        self.Coefficients['PHY2'] = 8.9094e-005
        self.Coefficients['PHY3'] = 0.031415
        self.Coefficients['PVY1'] = 0.037318
        self.Coefficients['PVY2'] = -0.010049
        self.Coefficients['PVY3'] = -0.32931
        self.Coefficients['PVY4'] = -0.69553

        # Combined Lateral Coefficients
        self.Coefficients['RBY1'] = 7.1433
        self.Coefficients['RBY2'] = 9.1916
        self.Coefficients['RBY3'] = -0.027856
        self.Coefficients['RCY1'] = 1.0719
        self.Coefficients['REY1'] = -0.27572
        self.Coefficients['REY2'] = 0.32802
        self.Coefficients['RHY1'] = 5.7448e-006
        self.Coefficients['RHY2'] = -3.1368e-005
        self.Coefficients['RVY1'] = -0.027825
        self.Coefficients['RVY2'] = 0.053604
        self.Coefficients['RVY3'] = -0.27568
        self.Coefficients['RVY4'] = 12.12
        self.Coefficients['RVY5'] = 1.9
        self.Coefficients['RVY6'] = -10.704

        # Pure Aligning Torque Coefficients
        self.Coefficients['QBZ1'] = 10.904
        self.Coefficients['QBZ2'] = -1.8412
        self.Coefficients['QBZ3'] = -0.52041
        self.Coefficients['QBZ4'] = 0.039211
        self.Coefficients['QBZ5'] = 0.41511
        self.Coefficients['QBZ9'] = 8.9846
        self.Coefficients['QBZ10'] = 0.0
        self.Coefficients['QCZ1'] = 1.2136
        self.Coefficients['QDZ1'] = 0.093509
        self.Coefficients['QDZ2'] = -0.009218
        self.Coefficients['QDZ3'] = -0.057061
        self.Coefficients['QDZ4'] = 0.73954
        self.Coefficients['QDZ6'] = -0.0067783
        self.Coefficients['QDZ7'] = 0.0052254
        self.Coefficients['QDZ8'] = -0.18175
        self.Coefficients['QDZ9'] = 0.029952
        self.Coefficients['QEZ1'] = -1.5697
        self.Coefficients['QEZ2'] = 0.33394
        self.Coefficients['QEZ3'] = 0.0
        self.Coefficients['QEZ4'] = 0.26711
        self.Coefficients['QEZ5'] = -3.594
        self.Coefficients['QHZ1'] = 0.0047326
        self.Coefficients['QHZ2'] = 0.0026687
        self.Coefficients['QHZ3'] = 0.11998
        self.Coefficients['QHZ4'] = 0.059083

        # Combined Aligning Coefficients
        self.Coefficients['SSZ1'] = 0.033372
        self.Coefficients['SSZ2'] = 0.0043624
        self.Coefficients['SSZ3'] = 0.56742
        self.Coefficients['SSZ4'] = -0.24116

        # Pure longitudinal coefficients
        self.Coefficients['PCX1'] = 1.6411
        self.Coefficients['PDX1'] = 1.1739
        self.Coefficients['PDX2'] = -0.16395
        self.Coefficients['PDX3'] = 5.0
        self.Coefficients['PEX1'] = 0.46403
        self.Coefficients['PEX2'] = 0.25022
        self.Coefficients['PEX3'] = 0.067842
        self.Coefficients['PEX4'] = -3.7604e-005
        self.Coefficients['PKX1'] = 22.303
        self.Coefficients['PKX2'] = 0.48896
        self.Coefficients['PKX3'] = 0.21253
        self.Coefficients['PHX1'] = 0.0012297 #TODO: There is something funky with these params. Should be zero? To have no offset at SR=0
        self.Coefficients['PHX2'] = 0.0004318
        self.Coefficients['PVX1'] = -8.8098e-006
        self.Coefficients['PVX2'] = 1.862e-005

        # Combined longitudinal coefficients
        self.Coefficients['RBX1'] = 13.276
        self.Coefficients['RBX2'] = -13.778
        self.Coefficients['RCX1'] = 1.2568
        self.Coefficients['REX1'] = 0.65225
        self.Coefficients['REX2'] = -0.24948
        self.Coefficients['RHX1'] = 0.0050722

        # Overturning Moment Coefficients
        self.Coefficients['QSX1'] = 2.3155e-04
        self.Coefficients['QSX2'] = 0.51574
        self.Coefficients['QSX3'] = 0.046399

        # Rolling Resistance Coefficients
        self.Coefficients['QSY1'] = 0.01
        self.Coefficients['QSY2'] = 0.0
        self.Coefficients['QSY3'] = 0.0
        self.Coefficients['QSY4'] = 0.0

        # Loaded Radius
        self.Coefficients['QV1'] = 7.15073791e-005
        self.Coefficients['QV2'] = 0.14892
        self.Coefficients['QFCX'] = 0
        self.Coefficients['QFCY'] = 0
        self.Coefficients['QFCG'] = -3.0
        self.Coefficients['QFZ1'] = 28.0249
        self.Coefficients['QFZ2'] = 29.2

        # Rolling Radius
        self.Coefficients['BREFF'] = 8.4
        self.Coefficients['DREFF'] = 0.27
        self.Coefficients['FREFF'] = 0.07

        # Lateral Relaxation
        self.Coefficients['PTY1'] = 2.1439
        self.Coefficients['PTY2'] = 1.9829

        # Longitudinal Relaxation
        self.Coefficients['PTX1'] = 2.3657
        self.Coefficients['PTX2'] = 1.4112
        self.Coefficients['PTX3'] = 0.56626

        # Turn-slip and parking calculated values.
        # Note that turn slip isn't implemented yet
        # Therefore all these reduction factors are set to 1
        # For future versions these needs to be calcualted for every time
        self.ZETA0 = 1
        self.ZETA1 = 1
        self.ZETA2 = 1
        self.ZETA3 = 1
        self.ZETA4 = 1
        self.ZETA5 = 1
        self.ZETA6 = 1
        self.ZETA7 = 1
        self.ZETA8 = 1

    def save(self, fname, data):
        return 'saving'

    def load(self, fname):
        return 'loading'

    def solve(self, state, mode=SolverMode.All):

        if mode is SolverMode.PureFy or mode is SolverMode.PureMz:
            state['FY'] = self.calculate_pure_fy(state)

        if mode is SolverMode.Fy or mode is SolverMode.All:
            state['FY'] = self.calculate_fy(state)

        if mode is SolverMode.PureFx:
            state['FX'] = self.calculate_pure_fx(state)

        if mode is SolverMode.Fx or mode is SolverMode.All:
            state['FX'] = self.calculate_fx(state)

        if mode is SolverMode.PureMz:
            state['MZ'] = self.calculate_mz(state)

        if mode is SolverMode.Mz or mode is SolverMode.All:
            state['MZ'] = self.calculate_mz(state)

        if mode is SolverMode.Mx or mode is SolverMode.All:
            state['MX'] = self.calculate_mx(state)

        if mode is SolverMode.Mz or mode is SolverMode.All:
            state['MY'] = self.calculate_my(state)

        if mode is SolverMode.Radius or mode is SolverMode.All:
            state['RL'], state['RE'] = self.calculate_radius(state)

        if mode is SolverMode.Relaxation or mode is SolverMode.All:
            state['SIGMA_ALPHA'] = self.calculate_lateral_relaxation_length(state)
            state['SIGMA_KAPPA'] = self.calculate_longitudinal_relaxation_length(state)


        return state

    def getparameters(self):
        return self.Coefficients

    def setparameters(self, params):
        #TODO: Must check that params keys actually match the models coefs.
        self.Coefficients = params

        return True  # should return False if the parameter structure doesn't match required one

    def getmodelinfo(self):
        return self.ModelInfo

    ###Private properties

    def calculate_common_values(self, state):
        # First we calculate some standard values used in multiple locations
        dfz = (state['FZ'] - self.Coefficients['FNOMIN']) / self.Coefficients['FNOMIN']
        alpha_star = math.tan(state['SA']) * np.sign(state['V'])
        gamma_star = math.sin(state['IA'])
        kappa = state['SR']

        return dfz, alpha_star, gamma_star, kappa

    def calculate_fx(self, state):
        p = self.Coefficients
        dfz, alpha_star, gamma_star, kappa = self.calculate_common_values(state)


        F_x0 = self.calculate_pure_fx(state)

        S_Hxa = self.Core.calculate_S_Hxa(p)

        #60
        alpha_s = alpha_star + S_Hxa

        B_xa = self.Core.calculate_B_xa(p, kappa)
        C_xa = self.Core.calculate_C_xa(p)
        E_xa = self.Core.calculate_E_xa(p, dfz)

        # 66
        G_xa_numerator = math.cos(C_xa * math.atan(B_xa * alpha_s - E_xa * (B_xa * alpha_s - math.atan(B_xa * alpha_s))))
        G_xa_denominator = math.cos(C_xa * math.atan(B_xa * S_Hxa - E_xa * (B_xa * S_Hxa - math.atan(B_xa * S_Hxa))))
        G_xa = G_xa_numerator / G_xa_denominator

        return F_x0 * G_xa

    def calculate_pure_fx(self, state):
        p = self.Coefficients
        dfz, alpha_star, gamma_star, kappa = self.calculate_common_values(state)

        C_x = self.Core.calculate_C_x(p)
        D_x = self.Core.calculate_D_x(p, state, dfz, gamma_star, self.ZETA1)
        S_Hx = self.Core.calculate_S_Hx(p, dfz)

        # 19
        kappa_x = kappa + S_Hx

        E_x = self.Core.calculate_E_x(p, dfz, kappa_x)
        K_x = self.Core.calculate_K_x(p, state, dfz)
        B_x = self.Core.calculate_B_x(C_x, D_x, K_x)
        S_Vx = self.Core.calculate_S_Vx(p, state, dfz, self.ZETA1)

        # 18
        fx_pure = D_x * math.sin((C_x * math.atan(B_x * kappa_x - E_x * (B_x * kappa_x - math.atan(B_x * kappa_x))))) + S_Vx

        return fx_pure

    def calculate_fy(self, state):
        p = self.Coefficients
        dfz, alpha_star, gamma_star, kappa = self.calculate_common_values(state)

        F_y0 = self.calculate_pure_fy(state)

        gamma_y = self.Core.calculate_gamma_y(p, gamma_star)
        B_yk = self.Core.calculate_B_yk(p, alpha_star)
        C_yk = self.Core.calculate_C_yk(p)
        E_yk = self.Core.calculate_E_yk(p, dfz)

        D_Vyk = self.Core.calculate_D_Vyk(p, state, dfz, gamma_y, alpha_star, gamma_star)
        S_Vyk = self.Core.calculate_S_Vyk(p, kappa, D_Vyk)

        # 69
        S_Hyk = self.Core.calculate_S_Hyk(p, dfz)
        kappa_s = kappa + S_Hyk

        # 77
        G_yk_numerator = math.cos(C_yk * math.atan(B_yk * kappa_s - E_yk * (B_yk * kappa_s - math.atan(B_yk * kappa_s))))
        G_yk_denominator = math.cos(C_yk * math.atan(B_yk * S_Hyk - E_yk * (B_yk * S_Hyk - math.atan(B_yk * S_Hyk))))
        G_yk = G_yk_numerator/G_yk_denominator

        return G_yk * F_y0 + S_Vyk

    def calculate_pure_fy(self, state):
        p = self.Coefficients
        dfz, alpha_star, gamma_star, kappa = self.calculate_common_values(state)

        gamma_y = self.Core.calculate_gamma_y(p, gamma_star)

        C_y = self.Core.calculate_C_y(p)
        D_y = self.Core.calculate_D_y(p, state, dfz, gamma_y, self.ZETA1)
        S_Hy = self.Core.calculate_S_Hy(p, dfz, gamma_y, self.ZETA0, self.ZETA4)

        # 31
        alpha_y = alpha_star + S_Hy

        E_y = self.Core.calculate_E_y(p, dfz, gamma_y, alpha_y)
        K_y = self.Core.calculate_K_y(p, state, gamma_y, self.ZETA3)
        B_y = self.Core.calculate_B_y(C_y, D_y, K_y)
        S_Vy = self.Core.calculate_S_Vy(p, state, dfz, gamma_y, self.ZETA4)

        # 30
        fy_pure = D_y * math.sin(C_y * math.atan(B_y * alpha_y - E_y * (B_y * alpha_y - math.atan(B_y * alpha_y)))) + S_Vy

        return fy_pure

    def calculate_mz(self, state):
        p = self.Coefficients
        dfz, alpha_star, gamma_star, kappa = self.calculate_common_values(state)

        # 32
        gamma_y = self.Core.calculate_gamma_y(p, gamma_star)
        gamma_z = self.Core.calculate_gamma_z(p, gamma_star)

        # Combined Trail Calcs
        S_Ht = self.Core.calculate_S_Ht(p, dfz, gamma_z)

        # 47
        alpha_t = alpha_star + S_Ht
        K_x = self.Core.calculate_K_x(p, state, dfz)
        K_y = self.Core.calculate_K_y(p, state, gamma_y, self.ZETA3)

        # 84
        alpha_teq = math.atan(math.sqrt(math.tan(alpha_t)**2 + (K_x/K_y)**2 * kappa**2) * np.sign(alpha_t))
        B_t = self.Core.calculate_B_t(p, dfz, gamma_z)
        C_t = self.Core.calculate_C_t(p)
        D_t = self.Core.calculate_D_t(p, state, dfz, gamma_z, self.ZETA5)
        E_t = self.Core.calculate_E_t(p, dfz, gamma_z, alpha_t, B_t, C_t)

        # Combined Trail Calc, here we are using alpha_teq instead of alpha_t
        t = self.Core.calculate_t(p, B_t, C_t, D_t, E_t, alpha_teq, alpha_star)

        # Combined Residual Torque Calcs
        S_Hy = self.Core.calculate_S_Hy(p, dfz, gamma_y, self.ZETA0, self.ZETA4)
        S_Vy = self.Core.calculate_S_Vy(p, state, dfz, gamma_y, self.ZETA4)
        K_y = self.Core.calculate_K_y(p, state, gamma_y, self.ZETA3)
        S_Hf = self.Core.calculate_S_Hf(S_Hy, S_Vy, K_y)

        # 47
        alpha_r = alpha_star + S_Hf

        # 85
        alpha_req = math.atan(math.sqrt(math.tan(alpha_r)**2 + (K_x/K_y)**2 * kappa**2) * np.sign(alpha_r))

        C_y = self.Core.calculate_C_y(p)
        D_y = self.Core.calculate_D_y(p, state, dfz, gamma_y, self.ZETA1)
        B_y = self.Core.calculate_B_y(C_y, D_y, K_y)
        B_r = self.Core.calculate_B_r(p, B_y, C_y, self.ZETA6)
        C_r = self.Core.calculate_C_r(self.ZETA7)
        D_r = self.Core.calculate_D_r(p, state, dfz, gamma_z, self.ZETA8)

        M_zr = self.Core.calculate_M_zr(B_r, C_r, D_r, alpha_req, alpha_star)

        # FY Prime Calcs
        D_Vyk = self.Core.calculate_D_Vyk(p, state, dfz, gamma_y, alpha_star, gamma_star)
        S_Vyk = self.Core.calculate_S_Vyk(p, kappa, D_Vyk)

        Fy_prime = state['FY'] - S_Vyk  # This is the combined lateral force without Fx induced Fy

        # Pneumatic scrub (s) calcs
        s = p['UNLOADED_RADIUS'] * (p['SSZ1'] + p['SSZ2'] * (state['FY'] / (p['FNOMIN'] * p['LFZ0'])) + (p['SSZ3'] + p['SSZ4'] * dfz) * gamma_star) * p['LS']

        M_prime = -t * Fy_prime + M_zr + s * state['FX']

        return M_prime

    def calculate_pure_mz(self, state):
        p = self.Coefficients
        dfz, alpha_star, gamma_star, kappa = self.calculate_common_values(state)

        gamma_z = self.Core.calculate_gamma_z(p, gamma_star)
        gamma_y = self.Core.calculate_gamma_y(p, gamma_star)

        # Trail calculations (D_t, C_t, B_t, E_t)
        S_Ht = self.Core.calculate_S_Ht(p, dfz, gamma_z)

        # 47
        alpha_t = alpha_star + S_Ht

        B_t = self.Core.calculate_B_t(p, dfz, gamma_z)
        C_t = self.Core.calculate_C_t(p)
        D_t = self.Core.calculate_D_t(p, state, dfz, gamma_z, self.ZETA5)
        E_t = self.Core.calculate_E_t(p, dfz, gamma_z, alpha_t, B_t, C_t)

        # Trail Calculation
        t = self.Core.calculate_t(p, B_t, C_t, D_t, E_t, alpha_t, alpha_star)

        # Residual Moment Calculations (C_r, D_r, B_r)
        # These calcs uses Pure Fy calculations, so they are repeated here (such as K_y and D_y)
        S_Hy = self.Core.calculate_S_Hy(p, dfz, gamma_y, self.ZETA0, self.ZETA4)
        S_Vy = self.Core.calculate_S_Vy(p, state, dfz, gamma_y, self.ZETA4)
        K_y = self.Core.calculate_K_y(p, state, gamma_y, self.ZETA3)
        C_y = self.Core.calculate_C_y(p)
        D_y = self.Core.calculate_D_y(p, state, dfz, gamma_y, self.ZETA1)
        B_y = self.Core.calculate_B_y(C_y, D_y, K_y)

        B_r = self.Core.calculate_B_r(p, B_y, C_y, self.ZETA6)
        C_r = self.Core.calculate_C_r(self.ZETA7)
        D_r = self.Core.calculate_D_r(p, state, dfz, gamma_z, self.ZETA8)
        S_Hf = self.Core.calculate_S_Hf(S_Hy, S_Vy, K_y)

        # 47
        alpha_r = alpha_star + S_Hf

        # Residual Moment Calculation
        M_zr = self.Core.calculate_M_zr(B_r, C_r, D_r, alpha_r, alpha_star)

        fy_pure = state['FY']  # This requires that FY have been calculated already

        mz_pure = -t * fy_pure + M_zr

        return mz_pure

    def calculate_mx(self, state):

        p = self.Coefficients
        dfz, alpha_star, gamma_star, kappa = self.calculate_common_values(state)

        # 86
        M_x = p['UNLOADED_RADIUS'] * state['FZ'] * (p['QSX1'] * p['LVMX'] - p['QSX2'] * gamma_star + p['QSX3'] * state['FY'] / p['FNOMIN']) * p['LMX']

        return M_x

    def calculate_my(self, state):

        p = self.Coefficients
        dfz, alpha_star, gamma_star, kappa = self.calculate_common_values(state)

        # 87
        M_y = p['UNLOADED_RADIUS'] * state['FZ'] * (p['QSY1'] + p['QSY2'] * state['FX']/p['FNOMIN'] + p['QSY3'] * abs(state['V'] / p['LONGVL']) + p['QSY4'] * (state['V'] / p['LONGVL'])**4) * p['LMY']

        return M_y

    def calculate_radius(self, state):

        p = self.Coefficients
        dfz, alpha_star, gamma_star, kappa = self.calculate_common_values(state)

        # If we don't have omega, we use an approximation
        omega = state['V'] / (p['UNLOADED_RADIUS'] * 0.98)

        # First we solve for dynamic displacement
        # External Effects
        speed_effect = p['QV2'] * abs(omega) * p['UNLOADED_RADIUS'] / p['LONGVL']
        fx_effect = (p['QFCX'] * state['FX'] / p['FNOMIN'])**2
        fy_effect = (p['QFCY'] * state['FY'] / p['FNOMIN'])**2
        camber_effect = p['QFCG'] * gamma_star**2
        external_effects = 1.0 + speed_effect - fx_effect - fy_effect + camber_effect

        # Fz/(external_effects * Fz0) = a*x2 + b*x
        # 0 = a*x2 + b*x + c

        a = (p['QFZ2'] / p['UNLOADED_RADIUS'])**2
        b = p['QFZ1'] / p['UNLOADED_RADIUS']
        c = -(state['FZ'] / (external_effects * p['FNOMIN']))

        if b**2 - 4*a*c > 0:
            rho = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
        else:
            rho = 999999

        # Then we calculate free-spinning radius
        R_omega = p['UNLOADED_RADIUS'] + p['QV1'] * p['UNLOADED_RADIUS'] * (omega * p['UNLOADED_RADIUS'] / p['LONGVL'])**2

        # The loaded radius is the free-spinning radius minus the deflection
        R_l = R_omega - rho

        # Effective Rolling Radius

        # Nominal stiffness
        C_z0 = p['FNOMIN'] / p['UNLOADED_RADIUS'] * math.sqrt(p['QFZ1']**2 + 4.0 * p['QFZ2'])
        if C_z0 == 0.0:
            return 0.0, 0.0

        # Eff. Roll. Radius #This is a newer version
        R_e_old = R_omega - (p['FNOMIN'] / C_z0) * (p['DREFF'] * math.atan(p['BREFF'] * state['FZ'] / p['FNOMIN']) + p['FREFF'] * state['FZ'] / p['FNOMIN'])


        # Eff. Roll. Radius Pac 2002
        C_z = p['QFZ1'] * p['FNOMIN'] / p['UNLOADED_RADIUS']
        rho_Fz0 = p['FNOMIN'] / (C_z0 * p['LCZ'])
        rho_d = rho/rho_Fz0

        R_e = R_omega - rho_Fz0 * (p['DREFF'] * math.atan(p['BREFF'] * rho_d) + p['FREFF'] * rho_d)

        return R_l, R_e

    def calculate_lateral_relaxation_length(self, state):


        p = self.Coefficients

        if p['PTY2'] == 0:
            return 0

        dfz, alpha_star, gamma_star, kappa = self.calculate_common_values(state)
        gamma_y = self.Core.calculate_gamma_y(p, gamma_star)

        # 93
        sigma_alpha = p['PTY1'] * math.sin(2.0 * math.atan(state['FZ'] / (p['PTY2'] * p['FNOMIN'] * p['LFZ0']))) * (1 - p['PKY3'] * abs(gamma_y)) * p['UNLOADED_RADIUS'] * p['LFZ0'] * p['LSGAL']

        return sigma_alpha

    def calculate_longitudinal_relaxation_length(self, state):

        p = self.Coefficients
        dfz, alpha_star, gamma_star, kappa = self.calculate_common_values(state)

        # 92
        sigma_kappa = state['FZ'] * (p['PTX1'] + p['PTX2'] * dfz) * math.exp(-p['PTX3'] * dfz) * (p['UNLOADED_RADIUS'] / p['FNOMIN']) * p['LSGKP']

        return sigma_kappa
