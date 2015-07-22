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
 

class PortfolioAgent(object):
    """
    Basic agent.
    """
    def __init__(self):
        pass