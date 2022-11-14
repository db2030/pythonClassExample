from a import A
class C():
    def __init__(self, cls = A):
        self.mine = cls("hey")
    
    def display(self):
        self.mine.display()