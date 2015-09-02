import datatime
import os, os.path
import pandas as pd

from abc import ABCMeta, abstractmethod

from events import MarketEvent

class DataHandler(object):
    """
    Abstract interface for Data handlers.
    """
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_latest_candles(self, symbol, N=1):
        raise NotImplementedError("Must be overridden")
    
    @abstractmethod
    def update_candles(self):
        raise NotImplementedError("Must be overridden")