from rply.token import BaseBox
from rply import ParserGenerator
from lex import lexer

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

class Equal(BinaryOp):
    def eval(self):
      temp_list_key = []
      temp_list_value = []
      temp_list_key.append(str(self.left.value))
      temp_list_value.append(str(self.right.eval()))
      for i in temp_list_key:
        for k in temp_list_value:
          symbol_table[i] = k
            #symbol_table[self.left] = self.right.eval() 
      return self.right.eval()
      
pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['NUMBER', 'OPEN_PARENS', 'CLOSE_PARENS',
     'PLUS', 'MINUS', 'MUL', 'DIV', 'IDENTIFIER', 'EQUAL'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['PLUS', 'MINUS', 'EQUAL']),
        ('left', ['MUL', 'DIV'])
    ]
)

#dictionary for values
symbol_table = { }

@pg.production('expression : NUMBER')
def expression_number(p):
    # p is a list of the pieces matched by the right hand side of the
    # rule
    return Number(int(p[0].getstr()))

@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
    return p[1]
  
@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MINUS expression')
@pg.production('expression : expression MUL expression')
@pg.production('expression : expression DIV expression')
@pg.production('expression : IDENTIFIER EQUAL expression')
def expression_binop(p):
    left = p[0]
    right = p[2]
    if p[1].gettokentype() == 'PLUS':
        return Add(left, right)
    elif p[1].gettokentype() == 'MINUS':
        return Sub(left, right)
    elif p[1].gettokentype() == 'MUL':
        return Mul(left, right)
    elif p[1].gettokentype() == 'DIV':
        return Div(left, right)
    elif p[1].gettokentype() == 'EQUAL':
        return Equal(left,right)
    else:
        raise AssertionError('Oops, this should not be possible!')

@pg.error
def error_handler(token):
    raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

parser = pg.build()

def parseText(argFromFile):
        parser.parse(lexer.lex(str(argFromFile))).eval()
        for x in symbol_table:
                print(x + ' = ' + symbol_table[x])
