from adaptor import Adaptor
from tcpip import TCPIP


if __name__ == "__main__":

    Adaptor().run("Click")
    print("=============\n")
    Adaptor(TCPIP).run("Fold")