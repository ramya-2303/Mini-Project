import ply.lex as lex

# Reserved keywords
#When the lexer sees "int" or "while", it will produce tokens INT, WHILE, etc.
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'char': 'CHAR',
    'bool': 'BOOL',
    'void': 'VOID',
    'for': 'FOR',
    'while': 'WHILE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'break': 'BREAK',
    'return': 'RETURN',
    'cin': 'CIN',
    'cout': 'COUT',
}

# Token list
tokens = [
    'ID', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'COLON', 'COMMA',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',
    'SHIFT_LEFT', 'SHIFT_RIGHT', 'PLUSPLUS' , 'MINUSMINUS' ,
] + list(reserved.values())

# Regular expressions for tokens  r is in raw formats
t_PLUS      = r'\+'
t_PLUSPLUS  = r'\+\+'
t_MINUS     = r'-'
t_MINUSMINUS = r'--'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUALS    = r'='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_SEMICOLON = r';'
t_COLON     = r':'
t_COMMA     = r','
t_LT        = r'<'
t_GT        = r'>'
t_LE        = r'<='
t_GE        = r'>='
t_EQ        = r'=='
t_NE        = r'!='
t_SHIFT_LEFT  = r'<<'
t_SHIFT_RIGHT = r'>>'
t_STRING    = r'\".*?\"'

t_ignore = ' \t'

#identifier rule
def t_ID(t):
    r'[A-Za-z_][A-Za-z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    #if the word is keyword change it to token type to keyword token else keep it as ID
    return t

# identify number (integer or decimal)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)        #If number contains . → convert to floatIf not → convert to int
    return t

def t_newline(t):      #t is the token object
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
