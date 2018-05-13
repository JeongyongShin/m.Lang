from Objects.varObject import VariableObject

class Parser(object):
	def __init__(self, tokens):
		# This will hold all the tokens that have been created by the lexer
		self.tokens = tokens
		# this will hold the token index we are parsing at
		self.tokens_index =0
		self.transpiled_code = " "

	def parse(self):
		while self.tokens_index < len(self.tokens):

			# Holds the type of tokens e.g. INDENTIFIER
			token_type = self.tokens[self.tokens_index][0]
			# Holds the value of tokens e.g. VAR
			token_value = self.tokens[self.tokens_index][1]

			# print(token_type, token_value)
			# This will trigger when a variable declertion token is found
			if token_type == "VAR_DECLERATION" and token_value == "var":
				self.parse_variable_decleration(self.tokens[self.tokens_index:len(self.tokens)])

				# print(token_type, token_value )


			# Increment token index by 1 so we can loop through next token
			self.tokens_index += 1

		print(self.transpiled_code)

	def parse_variable_decleration(self, token_stream):
		tokens_checked = 0

		name = ""
		operator = ""
		value = ""

		for token in range(0, len(token_stream)):

			token_type  = token_stream[tokens_checked][0]
			token_value = token_stream[tokens_checked][1]

			# if the statement end is found break out of loop as we have pasrsed the variable decleration
			if token == 4 and token_type == "STATEMENT_END": break



			# this will get the variable name and also perform error validation for invalid names
			elif token == 1 and token_type == "IDENTIFIER":
				name = token_value
			elif token == 1 and token_type != "IDENTIFIER":
				print("ERROR: Invalid variable name '" + token_value + "'")
				quit()

			# This will get variable assignment operator e.g. = or in the future += and also does error validation
			elif token == 2 and token_type == "OPERATOR":
				operator = token_value
			elif token == 2 and token_type == "OPERATOR":
				print("ERROR: Assignment Operator is missing or invalid it should be '='")
				quit()

			# this will get the variable value assigned
			elif token == 3 and token_type in ['STRING', 'INTEGER', 'IDENTIFIER']:
				value = token_value
			elif token == 3 and token_type not in ['STRING', 'INTEGER', 'IDENTIFIER']:
				print("Invalid variable assignment value '" + token_value + "'")
				quit()
			tokens_checked += 1

		varObj = VariableObject()
		self.transpiled_code += varObj.transpile(name, operator, value)

		# Increment token index by the amount of tokens we checked so we dont check them again
		self.tokens_index += tokens_checked



		# print(token_stream)
