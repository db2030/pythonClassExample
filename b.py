from temp import AbstractPrint # if needed
class B(AbstractPrint):
	def __init__(self, input_string):
		self.output_string = input_string
		self.width = len(input_string)

	def open(self):
		print("open")

	def print_input(self):
		print("print_input")

	def close(self):
		print("close")