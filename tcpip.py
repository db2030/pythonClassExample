from temp import AbstractPrint
class TCPIP(AbstractPrint):
    def __init__(self, dobot_name):
        self.name = dobot_name
        self.width = len(dobot_name)

    def connect(self):
        self.initiate()
        print("TCPIP detected")

    def send(self, cmd):
        print("TCPIP Run: " + cmd)

    def recieve(self):
        print(f'{self.name}:{self.width}:OK')

    def initiate(self):
        print(f"detecting open port on dobot: {self.name}")
        