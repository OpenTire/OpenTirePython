__author__ = 'henningo'
import abc

class TireModelBase(object):
    __metaclass__ = abc.ABCMeta

    Coefficients = None
    ModelInfo = None

    @abc.abstractmethod
    def getmodelinfo(self):
        """Return information about the model"""
        return

    @abc.abstractmethod
    def createmodel(self):
        """Create a default model"""

    @abc.abstractmethod
    def load(self, fname):
        """Retrieve data from the input source and return an object."""
        return

    @abc.abstractmethod
    def save(self, fname, data):
        """Save the data object to the output."""
        return

    @abc.abstractmethod
    def solve(self, state, mode=0):
        """Calculate steady state force"""
        return

    @abc.abstractmethod
    def getparameters(self):
        """Return the parameters dictionary"""
        return

    @abc.abstractmethod
    def setparameters(self, params):
        """Set the parameters"""
