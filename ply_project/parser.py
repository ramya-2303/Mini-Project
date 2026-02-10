import ply.yacc as yacc    #yacc is basically a parser generator
from lexer import tokens

#program structure
def p_program(p):
    '''program : program element    
               | element'''         #Triple quotes allow multi-line grammar.
    pass
#The function name must start with p_ PLY uses this to identify grammar rules

def p_element(p):
    '''element : function_def
               | declaration
               | statement'''
    pass
#pass: no action — purely syntactic validation.

# Construct 1: Variable declaration
# syntax : data_type variable_name;
def p_declaration(p):
    '''declaration : type var_list SEMICOLON
                   | type ID EQUALS expression SEMICOLON'''
    print("Valid variable Declaration")

def p_type(p):
    '''type : INT
            | FLOAT
            | DOUBLE
            | CHAR
            | BOOL
            | VOID'''
    pass

#handles comma seperated identifiers  /
def p_var_list(p):
    '''var_list : ID
                | ID COMMA var_list'''
    pass


# Construct 2: Function definition
# Syntax: 
# return_type function_name(parameter_list) {
#           // Function body (statements to be executed)
#           return;
# }

def p_function_def(p):
    '''function_def : type ID LPAREN param_list RPAREN LBRACE body RBRACE'''
    print("Valid Function Definition")

#  ex: parameters for the function ex: int a, float b
def p_param_list(p):
    '''param_list : param
                  | param COMMA param_list
                  | empty'''  # No parameters
    pass

def p_param(p):
    '''param : type ID'''
    pass


# Body inside functions, loops(for,while), switch
def p_body(p):
    '''body : body statement
            | expression
            | statement
            | empty'''
    pass


# Statements
def p_statement(p):
    '''statement : io_stmt
                 | loop_stmt
                 | switch_stmt
                 | declaration
                 | RETURN expression SEMICOLON'''
    pass


# Construct 3: Input/Output statement
#syntax:
#input statement: cin >> variable_name;
#output statement: cout << statements/variable_name;
def p_io_stmt(p):
    '''io_stmt : CIN shift_rexpr SEMICOLON
               | COUT shift_lexpr SEMICOLON'''
    print("Valid I/O Statement")

def p_shift_rexpr(p):
    '''shift_rexpr : SHIFT_RIGHT ID
                   | SHIFT_RIGHT ID shift_rexpr''' #multiple inputs
    pass
def p_shift_lexpr(p):
    '''shift_lexpr : SHIFT_LEFT expression  
                   | SHIFT_LEFT expression shift_lexpr'''  # multiple outputs
    pass


# Expressions
def p_expression(p):
    '''expression : ID
                  | NUMBER
                  | STRING
                  | expression EQUALS expression
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression
                  | LPAREN expression RPAREN
                  | SEMICOLON
                  | empty'''
    pass


# Construct 4: Loop statements (for & while)
#syntax:
#   for (initialization; condition; update) {
#        // code block to be executed
#   }
#   while (condition) {
#        // code block to be executed as long as the condition is true
#   }

def p_assignment(p):
    '''assignment : ID EQUALS arithmetic_expr
                  | ID PLUSPLUS
                  | ID MINUSMINUS'''
    pass

# Arithmetic expressions
def p_arithmetic_expr(p):
    '''arithmetic_expr : arithmetic_expr PLUS arithmetic_expr
                       | arithmetic_expr MINUS arithmetic_expr
                       | arithmetic_expr TIMES arithmetic_expr
                       | arithmetic_expr DIVIDE arithmetic_expr
                       | arithmetic_expr EQUALS arithmetic_expr
                       | arithmetic_expr LT arithmetic_expr
                       | arithmetic_expr GT arithmetic_expr
                       | arithmetic_expr LE arithmetic_expr
                       | arithmetic_expr GE arithmetic_expr
                       | LPAREN arithmetic_expr RPAREN
                       | ID
                       | NUMBER'''
    pass


def p_loop_stmt(p):
    '''loop_stmt : FOR LPAREN for_init SEMICOLON for_condition SEMICOLON for_update RPAREN LBRACE body SEMICOLON RBRACE
                 | WHILE LPAREN expression RPAREN LBRACE body SEMICOLON RBRACE'''
    print("Valid Loop Statement")

# For loop initialization: can be declaration or assignment
def p_for_init(p):
    '''for_init : declaration_no_semi
                | assignment
                | empty'''
    pass

# Declaration without semicolon (for 'for' loops)
def p_declaration_no_semi(p):
    '''declaration_no_semi : type ID opt_assign'''
    pass

# Optional assignment in declaration
def p_opt_assign(p):
    '''opt_assign : EQUALS expression
                  | empty'''
    pass

# Loop condition: any expression
def p_for_condition(p):
    '''for_condition : arithmetic_expr
                     | empty'''
    pass


# Loop update: any assignment
def p_for_update(p):
    '''for_update : assignment
                  | empty'''
    pass





# Construct 5: Switch case
# Syntax:
#    switch (expression) {
#        case constant_value_1: // Code to be executed if expression matches constant_value_1
#                                break; 
#        case constant_value_2:  // Code to be executed if expression matches constant_value_2
#                                break;
#        // ... other cases
#       default(optional):  // Code to be executed if no case matches the expression
#                           break; 
#    }

def p_switch_stmt(p):
    '''switch_stmt : SWITCH LPAREN ID RPAREN LBRACE case_blocks RBRACE'''
    print("Valid Switch Case")

def p_case_blocks(p):
    '''case_blocks : case_blocks case_block
                   | case_block
                   | empty'''
    pass

def p_case_block(p):
    '''case_block : CASE NUMBER COLON body opt_break
                  | DEFAULT COLON body'''
    pass

def p_opt_break(p):
    '''opt_break : BREAK SEMICOLON
                 | empty'''
    pass


def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (line {p.lineno})")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
