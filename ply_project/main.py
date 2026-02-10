from lexer import lexer
from parser import parser

print("Enter your code (Press Ctrl+Z and enter ):")
data = ''       #creates an empty string
try:
    while True:     #infinite loop
        line = input()
        data += line + '\n'
except EOFError:
    pass

print("\nSyntax Parsing")
parser.parse(data)        #reads token from a lexer


#imports the lexer and parser
#reads multi-line input
#sends it to the parser
#prints errors or results