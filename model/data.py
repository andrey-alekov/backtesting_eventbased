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
    def get_latest_timeframes(self, symbol, N=1):
        raise NotImplementedError("Must be overridden")
    
    @abstractmethod
    def update_timeframes(self):
        raise NotImplementedError("Must be overridden")


class CSVHandler(DataHandler):
    """
    CSV file data handler.
    """
    default_format = ['TICKER', 'PER', 'DATE', 'TIME', 'OPEN', 'HIGH', 'LOW',
                      'CLOSE', 'VOL']
    def __init__(self, events, filename, formater):
        self.events = events
        self.filename = filename
        self.data = {}
        if (formater is None or format == ""):
            self.formater = default_format
        else:
            self.formater = formater
        self._open_csv(filename)
    
    def _open_csv(self, filename):
        self.data = pd.io.parsers.read_csv(self.filename, header=0, index_col=0,
                                           names=self.formater)
    
    def _get_new_timeframe(self):
        raise NotImplementedError("not implemented")
    
    def get_latest_timeframes(N=1):
        return self.data[-N:]
    
    def update_timeframes():
        self.events.put(MarketEvent())