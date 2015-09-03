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


class CSVHandler(DataHandler):
    """
    CSV file data handler.
    """
    def __init__(self, events, filename):
        self.events = events
        self.filename = filename
        self._open_csv(filename)
    
    def _open_csv(self, filename):
        pass
    
    def _get_new_candle(self):
        pass