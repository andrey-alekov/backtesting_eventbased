class Event(object):
    """
    Basic class for any event. 
    """
    def __init__(self, event_type):
        self.type = event_type
        self.timestamp = 0 # generate timestamp in nanos
        self.toggle = False
    
    def get_type(self):
        return self.type
      
    def toggle(self):
        if self.toggle:
            self.toggle = False
        else:
            self.toggle = True
    
    def get_toggle(self):
        return self.toggle


class MarketEvent(Event):
    """
    Event from market data. For backtesting used only candle data
    """
    def __init__(self, candle):
        super(MarketEvent, self).__init__('MARKET')
        self.marketdata = candle


class SignalEvent(Event):
    """
    Basic signal from Strategy.
    """
    def __init__(self, symbol, sigtype):
        super(SignalEvent, self).__init__('SIGNAL')
        self.symbol = symbol
        self.sigtype = sigtype


class OrderEvent(Event):
    """
    Basic order event. Generates by executor and passes to Risk and Portfolio
    engines.
    """
    def __init__(self, symbol, order_type, quantity, side):
        super(SignalEvent, self).__init__('SIGNAL')
        self.symbol = symbol
        self.order_type = order_type
        self.quantity = quantity
        self.side = side


class ExecutionEvent(Event):
    """
    Order execution event. Rejected, filled, partially filled, active
    """
    def __init__(self, src_order, status):
        super(SignalEvent, self).__init__('EXECUTION')
        self.src_odrer = src_odrer
        self.status = status


class PortoflioEvent(Event):
    """
    Event from portfolio management.
    """
    def __init__(self):
        super(PortfolioEvent, self).__init__('PORTFOLIO')


class RiskEvent(Event):
    """
    Event from risk management.
    """
    def __init__(self):
        super(RiskEvent, self).__init__('RISK')