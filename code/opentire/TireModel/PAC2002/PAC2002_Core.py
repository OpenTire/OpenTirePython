__author__ = 'henningo'

import math
import numpy as np

# TODO: Use underscore to make it indicate "private" methods
 
class PAC2002_Core():

    #Region "Pure Fy"
    def calculate_gamma_y(self, p, gamma_star):

        # 32
        gamma_y = gamma_star * p['LGAY']  # Lambda Gamma Y

        return gamma_y

    def calculate_B_y(self, C_y, D_y, K_y):
        # Note: This method could call C_y, D_y and K_y internally, but for clarity they are sent as arguments

        # 39
        # We need to avoid division by zero
        if C_y * D_y == 0.0:
            #print 'Division by zero detected in B_Y calculation'
            B_y = K_y / 0.000000001
        else:
            B_y = K_y / (C_y * D_y)  # This could cause a divide by zero issue

        return B_y

    def calculate_C_y(self, p):

        # 33
        C_y = p['PCY1'] * p['LCY']

        return C_y

    def calculate_D_y(self, p, state, dfz, gamma_y, zeta1):

        # 34
        mu_y = self.calculate_mu_y(p, dfz, gamma_y)
        D_y = mu_y * state['FZ'] * zeta1

        return D_y

    def calculate_E_y(self, p, dfz, gamma_y, alpha_y):


        # 36
        # TODO: Sign function difference between Python and equations?
        # Note: First virsion had math.copysign, but it acts as an abs(), causing issues. Switched this to np.sign()
        E_y = (p['PEY1'] + p['PEY2'] * dfz) * (1 - (p['PEY3'] + p['PEY4'] * gamma_y)*np.sign(alpha_y)) * p['LEY']
        if E_y > 1.0:
            E_y = 1.0

        return E_y

    def calculate_K_y(self, p, state, gamma_y, zeta3):

        # 37
        denom = (p['PKY2'] * p['FNOMIN'] * p['LFZ0'])
        if denom == 0.0:
            #print 'Division by zero detected in K_Y calculation'
            denom = 0.000000001

        K_y0 = p['PKY1'] * p['FNOMIN'] * math.sin(2.0 * math.atan(state['FZ'] / denom)) * p['LFZ0'] * p['LKY']

        # 38
        K_y = K_y0 * (1-p['PKY3'] * abs(gamma_y)) * zeta3

        return K_y

    def calculate_mu_y(self, p, dfz, gamma_y):

        # 35
        mu_y = (p['PDY1'] + p['PDY2'] * dfz) * (1 - p['PDY3'] * gamma_y * gamma_y) * p['LMUY']  # Performance is better with gamma_y * gamma_y instead of gamma_y**2

        return mu_y

    def calculate_S_Hy(self, p, dfz, gamma_y, zeta0, zeta4):

        # 40
        S_Hy = (p['PHY1'] + p['PHY2'] * dfz) * p['LHY'] + p['PHY3'] * gamma_y * zeta0 + zeta4 - 1

        return S_Hy

    def calculate_S_Vy(self, p, state, dfz, gamma_y, zeta4):

        # 41 - Moved parenthesis to sit "behind" gamma_y
        S_Vy = state['FZ'] * ((p['PVY1'] + p['PVY2'] * dfz) * p['LVY'] + (p['PVY3'] + p['PVY4'] * dfz) * gamma_y) * p['LMUY'] * zeta4

        return S_Vy

    #Region "Combined Fy"
    def calculate_B_yk(self, p, alpha):

        # 70
        B_yk = p['RBY1'] * math.cos(math.atan(p['RBY2'] * (alpha - p['RBY3']))) * p['LYKA']

        return B_yk

    def calculate_C_yk(self, p):

        # 71
        C_yk = p['RCY1']

        return C_yk

    def calculate_E_yk(self, p, dfz):

        # 73
        E_yk = p['REY1'] + p['REY2'] * dfz
        if E_yk > 1.0:
            E_yk = 1.0
        return E_yk

    def calculate_S_Hyk(self, p, dfz):

        # 74
        S_Hyk = p['RHY1'] + p['RHY2'] * dfz

        return S_Hyk

    def calculate_D_Vyk(self, p, state, dfz, gamma_y, alpha, gamma):

        #TODO: Should this be here, or should we pass mu_y instead? What's cleaner?
        mu_y = self.calculate_mu_y(p, dfz, gamma_y)

        # 76
        D_Vyk = mu_y * state['FZ'] * (p['RVY1'] + p['RVY2'] * dfz + p['RVY3'] * gamma) * math.cos(math.atan(p['RVY4'] * alpha))

        return D_Vyk

    def calculate_S_Vyk(self, p, kappa, D_Vyk):

        # 75
        S_Vyk = D_Vyk * math.sin(p['RVY5'] * math.atan(p['RVY6'] * kappa)) * p['LVYKA']

        return S_Vyk

    #Region "Pure Fx"

    def calculate_B_x(self, C_x, D_x, K_x):

        # 26
        if (C_x * D_x) == 0.0:
            B_x = 0.0

        else:
            B_x = K_x / (C_x * D_x)

        return B_x

    def calculate_C_x(self, p):

        # 21
        C_x = p['PCX1'] * p['LCX']

        return C_x

    def calculate_D_x(self, p, state, dfz, gamma_star, zeta1):

        mu_x = self.calculate_mu_x(p, dfz, gamma_star)

        # 22
        D_x = mu_x * state['FZ'] * zeta1

        return D_x

    def calculate_E_x(self, p, dfz, kappa_x):

        # 24
        E_x = (p['PEX1'] + p['PEX2'] * dfz + p['PEX3'] * dfz * dfz) * (1.0 - p['PEX4'] * np.sign(kappa_x)) * p['LEX']
        if E_x > 1.0:
            E_x = 1.0

        return E_x

    def calculate_K_x(self, p, state, dfz):

        # 25
        K_x = state['FZ'] * (p['PKX1'] + p['PKX2'] * dfz) * math.exp(p['PKX3'] * dfz) * p['LKX']
        # TODO: Check the "exp" function

        return K_x

    def calculate_mu_x(self, p, dfz, gamma_star):

        # 20
        gamma_x = gamma_star * p['LGAX']

        # 23
        mu_x = (p['PDX1'] + p['PDX2'] * dfz) * (1.0 - p['PDX3'] * gamma_x ** 2.0) * p['LMUX'] # Note that it is using gamma_x here

        return mu_x

    def calculate_S_Hx(self, p, dfz):

        # 27
        S_Hx = (p['PHX1'] + p['PHX2'] * dfz) * p['LHX']

        return S_Hx

    def calculate_S_Vx(self, p, state, dfz, zeta1):

        # 28
        S_Vx = state['FZ'] * (p['PVX1'] + p['PVX2'] * dfz) * p['LVX'] * p['LMUX'] * zeta1

        return S_Vx

    #Region "Combined Fx"
    def calculate_S_Hxa(self, p):

        # 65
        S_Hxa = p['RHX1']

        return S_Hxa

    def calculate_B_xa(self, p, kappa):

        # 61
        B_xa = p['RBX1'] * math.cos(math.atan(p['RBX2'] * kappa)) * p['LXAL']

        return B_xa

    def calculate_C_xa(self, p):

        # 62
        C_xa = p['RCX1']

        return C_xa

    def calculate_E_xa(self, p, dfz):

        # 64
        E_xa = p['REX1'] + p['REX2'] * dfz
        if E_xa > 1.0:
            E_xa = 1.0

        return E_xa



    #Region "Pure Mz"

    def calculate_gamma_z(self, p, gamma_star):

        # 49
        gamma_z = gamma_star * p['LGAZ']

        return gamma_z

    #Trail Calcs

    def calculate_B_t(self, p, dfz, gamma_z):

        # 50
        B_t = (p['QBZ1'] + p['QBZ2'] * dfz + p['QBZ3'] * dfz ** 2) * (1 + p['QBZ4'] * gamma_z + p['QBZ5'] * abs(gamma_z)) * p['LKY'] / p['LMUY']

        return B_t

    def calculate_C_t(self, p):

         # 51
        C_t = p['QCZ1']

        return C_t

    def calculate_D_t(self,p, state, dfz, gamma_z, zeta5):

        # 52
        D_t = state['FZ'] * (p['QDZ1'] + p['QDZ2'] * dfz) * (1 + p['QDZ3'] * gamma_z + p['QDZ4'] * gamma_z ** 2) * p['UNLOADED_RADIUS'] / p['FNOMIN'] * p['LTR'] * zeta5

        return D_t

    def calculate_E_t(self, p, dfz, gamma_z, alpha_t, B_t, C_t):

        # 53
        E_t = (p['QEZ1'] + p['QEZ2'] * dfz + p['QEZ3'] * dfz ** 2) * (1 + (p['QEZ4'] + p['QEZ5'] * gamma_z) * ((2/math.pi) * math.atan(B_t * C_t * alpha_t)))
        if E_t > 1.0:
            E_t = 1.0

        return E_t

    def calculate_S_Ht(self, p, dfz, gamma_z):

        # 54
        S_Ht = p['QHZ1'] + p['QHZ2'] * dfz + (p['QHZ3'] + p['QHZ4'] * dfz) * gamma_z

        return S_Ht

    def calculate_t(self,p, B_t, C_t, D_t, E_t, alpha_t, alpha_star):

         # 44 - Trail
        t = D_t * math.cos(C_t * math.atan(B_t * alpha_t - E_t * (B_t * alpha_t - math.atan(B_t * alpha_t)))) * math.cos(alpha_star)

        return t

    #Residual Moment Calcs

    def calculate_B_r(self, p, B_y, C_y, zeta6):

        # 55
        B_r = (p['QBZ9'] * p['LKY'] / p['LMUY'] + p['QBZ10'] * B_y * C_y) * zeta6

        return B_r

    def calculate_C_r(self, zeta7):

        # after 55
        C_r = zeta7

        return C_r

    def calculate_D_r(self, p, state, dfz, gamma_z, zeta8):

        # 56
        D_r = state['FZ'] * ((p['QDZ6'] + p['QDZ7'] * dfz) * p['LRES'] + (p['QDZ8'] + p['QDZ9'] * dfz) * gamma_z) * p['UNLOADED_RADIUS'] * p['LMUY'] + zeta8 - 1.0

        return D_r

    def calculate_S_Hf(self, S_Hy, S_Vy, K_y):

        # 48
        S_Hf = S_Hy + S_Vy / K_y

        return S_Hf

    def calculate_M_zr(self, B_r, C_r, D_r, alpha_r, alpha_star ):

        # 46 - Residual Moment
        M_zr = D_r * math.cos(C_r * math.atan(B_r * alpha_r)) * math.cos(alpha_star)

        return M_zr
