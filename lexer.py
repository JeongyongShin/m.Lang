import re

class Lexer(object):
	def __init__ (self, source_code):
		self.source_code = source_code

	def tokenize(self):
		#print('test')
		# where all the tokens created by lexer will be stored
		tokens = []


		# Create a word list of the source code
		source_code = self.source_code.split()

		# this will keep track of the word index we are at in the source code
		source_index = 0

		# loop through each word in source code to generate tokens
		while source_index < len(source_code):
			
			#print (source_code[source_index])
			word = source_code[source_index]
			# this will recognise a variable and create a token for it
			if word == "var": tokens.append(["VAR_DECLERATION", word])
			# this will recognise a word and create an identifier token for it
			elif re.match('[a-z]', word) or re.match('[A-Z]', word):
				if word[len(word) -1] == ";":
					tokens.append(['IDENTIFIER', word[0:len(word)-1]])
				else:
					tokens.append(['IDENTIFIER', word])

			# this will recognise an integer and create an INTEGER token for it
			elif re.match('[0-9]', word):
				if word[len(word) -1] == ";":
					tokens.append(['INTEGER', word[0:len(word)-1]])
				else:
					tokens.append(['INTEGER', word])

			# this will recognise operators and create an OPERATOR token for it
			elif word in "=/*=-+":
				tokens.append(['OPERATOR', word])

			# if a STATEMENT_END (;) is found at the last character in a word add a STATEMENT_END token
			if word[len(word) - 1] == ";":
				tokens.append(['STATEMENT_END', ';'])
			# Increases word index after checking it
			source_index += 1

		print(tokens)

		# 
		return tokens


