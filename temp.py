# Abstract Class
import abc

class AbstractPrint:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def send(self):
        pass

    @abc.abstractmethod
    def recieve(self):
        pass

    def run(self, cmd): # 여기서 이미 큰 흐름을 모두 만듦
        self.connect()
        self.send(cmd)
        self.recieve()
    