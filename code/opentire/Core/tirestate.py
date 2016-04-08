__author__ = 'henningo'

class TireState(dict):

    def __init__(self, *args, **kwargs):
        self['FX'] = 0.0
        self['FY'] = 0.0
        self['FZ'] = 0.0
        self['MX'] = 0.0
        self['MY'] = 0.0
        self['MZ'] = 0.0
        self['SA'] = 0.0
        self['SR'] = 0.0
        self['IA'] = 0.0
