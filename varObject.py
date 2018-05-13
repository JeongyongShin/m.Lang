class VariableObject(object):
	def __init__(self):
		# this will hold the python exec string for the varialbe decleration
		self.exec_string =""

	def transpile(self, name, operator, value):
		# Appends the python executable string converted using our parser
		self.exec_string += name + " " + operator + " " + value + "\n"
		return self.exec_string


