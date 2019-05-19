#!/usr/bin/python3

from parser import parser
from parser import parseText
import io

def main():
	path = '/Users/aaronyam/CISC3160/toy-language-interpreter/test.py'
	path_file = open(path , "r")
	for x in path_file:
		try:
			parseText(x)
		except:
			raise Exception ("Error while parsing")
	path_file.close()
main()
