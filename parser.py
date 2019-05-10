from rply import ParserGenerator
from rply.token import BaseBox

#PARSER
class Number(BaseBox):
  def __init__(self, value):
    self.value = value
  def eval(self):
    return self.value

#Binary Operators
class BinaryOp(BaseBox):
  def __init__(self, lhs, rhs):
    self.lhs = lhs
    self.rhs = rhs
class Add(BinaryOp):
  def eval(self):
    return self.lhs.eval() + self.right.eval()
class Sub(BinaryOp):
  def eval(self):
    return self.lhs.eval() - self.rhs.eval()
class Mul(BinaryOp):
  def eval(self):
    return self.lhs.eval() * self.rhs.eval()
class Div(BinaryOp):
  def eval(self):
    return self.lhs.eval() / self.rhs.eval()
#Unary Operators  
class UnaryOp(BaseBox):
  def __init__(self, lhs, rhs):
    self.lhs = lhs
    self.rhs = rhs
class Positive(UnaryOp):
  def eval(self):
    return +(self.lhs.eval())
class Negate(UnaryOp):
  def eval(self):
    return -(self.lhs.eval())
#Assignment Operator
class Assignment():
  def ():
    return 

#class Equal(BinaryOp):
 #   return self.rhs.eval()

pg = ParserGenerator(
["POSITIVE", "NEGATE","PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LPAREN", "RPAREN", "NUMBER", "EQUAL", "IDENTIFIER"],
    precedence = [("left", ['POSITIVE', 'NEGATE']), ("left", ['MULTIPLY', 'DIVIDE']), ("left", ['PLUS', 'MINUS'])], cache_id="aaron_parser")

@pg.production('main : expr')
def main(p):
  return p[0]

@pg.production('expr : expr PLUS term')
@pg.production('expr : expr MINUS term')
def expr_binop(p):
  left = p[1]
  right = p[3]
  if p[2].gettokentype()=='PLUS':
    return Add(left,right)
  elif p[2].getttokentype() == 'MINUS':
    return Sub(left,right)
  else:
    raise AssertionError('Operation not defined %d', token.gettokentype())

@pg.production(' expr : term ')
def expr_term(p):
  return p[0]

@pg.production('term : term MULTIPLY fact')
@pg.production('term : term DIVIDE fact')
def term_mul(p):
  left = p[1]
  right = p[3]
  if p[2].gettokentype()=="MULTIPLY":
    return Mul(left,right)
  elif p[2].gettokentype()=="DIVIDE":
    return Div(left,right)
  else:
    raise AssertionError('Binary Operation not defined %d', token.gettokentype())
  
@pg.production('term : fact')
def term_fact(p):
  return p[0]

@pg.production('fact : LPAREN expr RPAREN')
def parenthesis(p):
  return p[2]

@pg.production('fact : NEGATE fact ')
@pg.production('fact : POSITIVE fact')
def fact_unaryop(p):
  left = p[0]
  right = p[1]
  if p[0].gettokentype()=="POSITIVE":
    return Positive(left,right)
  elif p[0].gettokentype()=="NEGATE":
    return Negate(left,right)
  else:
    raise AssertionError('Unary Operation not defined %d', token.gettokentype())
    
@pg.production('fact : NUMBER')
def fact_number(p):
  return Number(int(p[0].getstr()))

@pg.production('fact : IDENTIFIER')
def fact_ID(p):
  return p[0]
  
@pg.production('expr : IDENTIFIER EQUAL expr')
def expr_assign(p):
  return p[0]
  #return Assignment(Variable(p[1].getstr()),p[3])
  
class BoxInt(BaseBox):
  def __init__(self, value):
    self.value = value
  def getint(self):
    return self.value

class ParserState(object):
  def __init__(self, filename):
    self.filename = filename
    
parser = pg.build()

parser.parse(lexer.lex('x = 1'))
#myparser.parse(lexer.lex(source), state=ParserState('foo.py'))
