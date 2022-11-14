from temp import AbstractPrint # if needed
class A(AbstractPrint):
	def __init__(self, input_string):
		self.output_string = input_string
		self.width = len(input_string)

	def open(self):
		self.printLine()

	def print_input(self):
		print("|" + self.output_string + "|")

	def close(self):
		self.printLine()

	def printLine(self): # 상속/concrete 에서 detail 설정
		result = "+"
		for i in range(0, self.width):
			result += "-"
		result += "+"
		print(result, end="\n")