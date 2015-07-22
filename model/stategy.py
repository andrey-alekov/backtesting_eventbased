class Strategy(object):
    """
    Basic strategy.
    """
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