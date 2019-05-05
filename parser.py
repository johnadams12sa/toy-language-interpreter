from rply import ParserGenerator
from rply.token import BaseBox

#PARSER
class Number(BaseBox):
  def __init__(self, value):
    self.value = value
  def eval(self):
    return self.value
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
class Eq(BinaryOp):
  def eval(self):
    return self.lhs.eval() = self.rhs.eval()

pg = ParserGenerator(
["PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LPAREN", "RPAREN", "NUMBER", "EQUAL", "IDENTIFIER"],
    precedence = [("left", ['MULTIPLY', 'DIVIDE']), ("left", ['PLUS', 'MINUS'])], cache_id="aaron_parser")

def NUMBER(p):
  p.value = int(p.value)
  return p

def p_newline(p):
  r'\n'
  p.lexer.lineno += (p.value)

@pg.production('main : stmt')
def main(p):
	return p[0]

@pg.production('stmt : expr')
def stmt_expr(state,p):
   return p[0]
  
@pg.production('expr : fact')
def expr_fact(state,p):
    return p[0]
  
@pg.production('fact : IDENTIFIER')
def fact_ID(state,p):
    return p[0]

@pg.production('stmt : IDENTIFIER = expr')
def stmt_assign(state, p):
   return Assignment(Variable(p[1].getstr()),p[3])

@pg.production("expr : expr PLUS expr")
@pg.production("expr : expr MINUS expr")
@pg.production("expr : expr MULTIPLY expr")
@pg.production("expr : expr DIVIDE expr")
@pg.production("expr : expr EQUAL expr")

def expr_op(p):
	lhs = p[0].getint()
	rhs = p[2].getint()
	if p[1].gettokentype() == "PLUS":
		return BoxInt(lhs + rhs)
	elif p[1].gettokentype() == "MINUS":
		return BoxInt(lhs - rhs)
	elif p[1].gettokentype() == "MULTIPLY":
		return BoxInt(lhs * rhs)
	elif p[1].gettokentype() == "DIVIDE":
		return BoxInt(lhs / rhs)
  #elif p[1].gettokentype () == "EQUAL":
    #return BoxInt(lhs = rhs)
	else:
		raise AssertionError("Possible missing operator")

#@pg.production("expr : IF expr COLON stmt END")
#def expr_if(state, p):
#    return If(condition=p[1], body=p[3])

def p_error(p):
  print("Illegal character found: '%s'" % p.value[0])
  p.lexer.skip(1)

class Variable(BaseBox):
  def init(self,name):
    self.name=str(name)
    self.value=None 
  def getname(self):
    return str(self.name)
  def eval(self,env):
        #if env.variables.get(self.name, None) is not None:
            #self.value = env.variables[self.name].eval(env)
    return self.value
        #raise LogicError("Not defined yet")
  def to_string(self):
    return str(self.name)
      
class Boolean(BaseBox):
  def init(self, value):
    self.value = bool(value)
  def eval(self,env):
    return self
  def to_string(self):
    return str(self.value).lower()
    
class BoxInt(BaseBox):
	def __init__(self, value):
		self.value = value
	def getint(self):
		return self.value

parser = pg.build()

#parser.parse(lexer.lex("let a = 5"), Environment()).to_string()
list(lexer.lex("005+4"))

lexer.input(data)

while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok.type, tok.value, tok.lineno, tok.lexpos)
