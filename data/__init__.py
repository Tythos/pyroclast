"""Interface for package data stored in the "data" folder
"""

import os

def get_path(data_path):
	return os.path.dirname(os.path.realpath(__file__)) + os.sep + data_path
	
def get_text(data_path):
	p = get_full_path(data_path)
	f = open(p, 'r')
	content = f.read()
	f.close()
	return content
