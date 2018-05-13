import lexer
import mparser

def main():

# read the current main source code in test.lang and store it in variable
	content = ""
	with open('m.Lang', 'r') as file:
		content = file.read()

		# print(content)

		##################     Lexar    ########################
		# we call the lexer class and initialize it with the source code

		lex = lexer.Lexer(content)
		# we now call the tokenize method
		tokens = lex.tokenize()

		###################     Parse     ######################

		parse = mparser.Parser(tokens)
		parse.parse()


main()
