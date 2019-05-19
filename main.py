#!/usr/bin/python3

from parser import parser
from parser import parseText
import io

def main():
	path = 'EDIT_PATH_TO_FILE_HERE'
	path_file = open(path , "r")
	for x in path_file:
		try:
			parseText(x)
		except:
			raise Exception ("Error while parsing")
	path_file.close()
main()
