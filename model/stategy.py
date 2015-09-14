import datetime
import numpy as np
import pandas as pd
import Queue

from abc import ABCMeta, abstractmethod
from event import SignalEvent


class Strategy(object):
    """
    Basic strategy.
    """
    __metaclass__ = ABCMeta
    
    def __init__(self, name)
        self.name = name
        self.toggle = False

    def toggle(self):
        """
        """
        if self.toggle:
            self.toggle = False
        else:
            self.toggle = True

    def process(self, marketEvent):
        """
        Process market event.
        """
        pass

    def isopen(self):
        """
        Is strategy already open position.
        """
        pass
        
    def getlastsignal(self):
        """
        Return last raise signalevent
        """
        pass
    
    @abstractmethod
    def calculate_sginals(self):
        raise NotImplementedError("not implemented")
    