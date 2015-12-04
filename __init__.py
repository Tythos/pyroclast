"""Pyroclast is a easy-to-use REST-ful data server that lets you drag-and-drop
   files for instant sharing. It supports multiple formats, paradigms (i.e.,
   flat tables vs. object hierarchies), and query key-value fields. There are
   also format-specific arguments supported for table/sheet selection, etc.
"""

from pyroclast import docs, test, server

__all__ = [
	'basic',
	'dataTables',
	'objectHierarchies',
	'server',
	'data',
	'docs',
	'test'
]

def runAllTests():
	"""Invokes the runAllTests function from the pyroclast.test module
	"""
	test.runAllTests()
	
def buildAllDocs():
	"""Invokes the buildAllDocs function from the pyroclast.docs module
	"""
	docs.buildAllDocs()

if __name__ == '__main__':
	"""By default, invoking this file will start the pyroclast server
	"""
	server.start()
