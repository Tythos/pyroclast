"""Interface for package data stored in the "data" folder
"""

import os
import shutil

def get_path(data_path):
	return os.path.dirname(os.path.realpath(__file__)) + os.sep + data_path
	
def get_text(data_path):
	p = get_full_path(data_path)
	f = open(p, 'r')
	content = f.read()
	f.close()
	return content

def serve(file_path):
	file_path = os.path.abspath(file_path)
	if os.path.exists(file_path):
		dest_path = get_path(os.path.basename(file_path))
		shutil.copyfile(file_path, dest_path)
	else:
		raise Exception('File could not be located')