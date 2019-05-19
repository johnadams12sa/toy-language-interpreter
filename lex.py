#!/usr/bin/python3
from rply import LexerGenerator

#LEXICAL ANALYZER
lg = LexerGenerator()

#LIST OF TOKENS

#Unary Operators
#lg.add("NEGATE", r"\-")
#lg.add("POSITIVE", r"\+")

#Binary Operators
lg.add("PLUS", r"\+")
lg.add("MINUS", r"\-")
lg.add("MUL", r"\*")
lg.add("DIV", r'/')

#Parenthesis
lg.add("LPAREN", r"\(")
lg.add("RPAREN", r"\)")
#lg.add("NUMBER", r"^[0-9] | [1-9][0-9]*")
lg.add('NUMBER', r'\d+')
lg.add("EQUAL", r"=")
lg.add("SEMICOLON", r";")
lg.add("IDENTIFIER", r"[a-zA-z_][a-zA-Z0-9_]*")
lg.ignore(r"[\t\s]+")

lexer = lg.build()
