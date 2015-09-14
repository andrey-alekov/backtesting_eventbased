import datetime
import numpy as np
import pandas as od
import Queue

from abc import ABCMeta, abstractmethod
from math import floor

from event import FillEvent, OrderEvent


class Limit(object):
    def __init__(self, size):
        self.size = size
    
    def set_limit(self, newlimit):
        if newlimit>0:
            self.size = newlimit
    
    def get_limit(self):
        return self.size


class Portfolio(object):
    """
    Basic portfolio.
    """
    __metaclass__ = ABCMeta
    
    def __init__(self, name, limit):
        self.name = name
        self.risk_engine = None
        self.agent_list = None
        self.toggle = False
        self.limit = limit
    
    def toggle(self):
        if self.toggle:
            self.toggle = False
        else:
            self.toggle = True

    @abstractmethod
    def update_signal(self, event):
        raise NotImplementedError("Should implement update_signal()")

    @abstractmethod
    def update_fill(self, event):
        raise NotImplementedError("Should implement update_fill()")


class PortfolioAgent(object):
    """
    Basic agent.
    """
    def __init__(self):
        pass