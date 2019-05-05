!pip install rply
from rply import LexerGenerator

#LEXICAL ANALYZER
lg = LexerGenerator()

#LIST OF TOKENS
lg.add("PLUS", r"\+")
lg.add("MINUS", r"\-")
lg.add("MULTIPLY", r"\*")
lg.add("DIVIDE", r"\/")
lg.add("LPAREN", r"\(")
lg.add("RPAREN", r"\)")
lg.add("NUMBER", r"[[0-9]|[1-9][0-9]*]")
lg.add("=", r"=")
lg.add("IDENTIFIER", r"[a-zA-z_][a-zA-Z0-9_]*")
lg.ignore(r"[\t\s]+")

lexer=lg.build()
#list(lexer.lex("let a = 5"))
