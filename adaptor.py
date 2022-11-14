from rtd import RTD
class Adaptor():
    def __init__(self, cls = RTD):
        self.mine = cls("hey")
    
    def run(self, cmd):
        self.mine.run(cmd)