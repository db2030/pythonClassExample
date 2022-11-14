# Abstract Class
import abc

class AbstractPrint:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def print_input(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    def display(self): # 여기서 이미 큰 흐름을 모두 만듦
        self.open()
        for i in range(0, 5):
            self.print_input()
        self.close()