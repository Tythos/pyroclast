"""Defines documentation management behaviors for the Pyroclast package
"""

import pydoc
import pyroclast
import os
import importlib

def getDocDir():
	"""Returns the absolute path to the documentation directory of the pyroclast
	   package (where this file is located).
	"""
	return os.path.dirname(os.path.realpath(__file__)) + os.sep

def buildAllDocs(symbol='pyroclast'):
	"""Recursively constructs HTML pages of documentation the given module
	   contents, beginning with pyroclast itself, which are subsequently written
	   to the package's 'docs/' folder.
	"""
	dd = getDocDir()
	obj, name = pydoc.resolve(symbol)
	page = pydoc.html.page(pydoc.describe(obj), pydoc.html.document(obj,name))
	with open(dd + name + '.html', 'w') as f:
		f.write(page)
	if hasattr(obj, '__all__'):
		for a in obj.__all__:
			identifier = name + '.' + a
			child = importlib.import_module(identifier)
			buildAllDocs(child)

if __name__ == '__main__':
	buildAllDocs()
