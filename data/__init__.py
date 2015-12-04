"""Interface for package data stored in the "data" folder, providing methods to
   both resolve and load data. For Pyroclast servers, this module supports
   importing and serving data files contained in (or under) this directory.
"""

import os
import shutil

def get_path(data_path):
	"""Returns the absolute path to the indicated data file stored under the
	   'data/' folder co-located with this module.
	"""
	return os.path.dirname(os.path.realpath(__file__)) + os.sep + data_path
	
def get_text(data_path):
	"""Returns the text contents (as a string) of the given file stored under
	   the 'data/' folder co-located with this module.
	"""
	p = get_full_path(data_path)
	f = open(p, 'r')
	content = f.read()
	f.close()
	return content

def serve(file_path):
	"""Copies the given file to the 'data/' folder co-located with this module
	   so that it may be served by the Pyroclast REST-ful server.
	"""
	file_path = os.path.abspath(file_path)
	if os.path.exists(file_path):
		dest_path = get_path(os.path.basename(file_path))
		shutil.copyfile(file_path, dest_path)
	else:
		raise Exception('File could not be located')