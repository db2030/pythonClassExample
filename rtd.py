from temp import AbstractPrint
class RTD(AbstractPrint):
	def __init__(self, dobot_name):
		self.name = dobot_name
		self.width = len(dobot_name)

	def connect(self):
		print("RTDAgent.exe detected")

	def send(self, cmd):
		print("RTDAgent Run: " + cmd)

	def recieve(self):
		print(f'{self.name}:{self.width}:OK')
