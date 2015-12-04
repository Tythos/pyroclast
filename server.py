"""Defines the primary entry point for starting a Pyroclast REST-ful server
   based on CherryPy's WSGI webserver implementation. File extensions determine
   how requests are routed to different parsers, defined in either the
   dataTables module or the objectHierarchies module (depending on the format).
"""

import cherrypy
from os import path
import sys
from pyroclast import dataTables, objectHierarchies, basic

if sys.version_info.major == 2:
	from urlparse import parse_qs
else:
	from urllib.parse import parse_qs
	
def null(file, filters):
	return ''
	
mimeTypes = {
	'.csv': 'text/plain',
	'.xls': 'text/plain',
	'.xlsx': 'text/plain',
	'.sql': 'text/plain',
	'.json': 'text/plain',
	'.xml': 'text/plain',
	'.unq': 'text/plain'
}

parsers = {
	'.csv': dataTables.getCsv,
	'.xls': dataTables.getExcel,
	'.xlsx': dataTables.getExcel,
	'.sql': dataTables.getSqlite,
	'.json': objectHierarchies.getJson,
	'.xml': objectHierarchies.getXml,
	'.unq': objectHierarchies.getUnqlite,
	'.ico': null
}

def parseQueryValues(query):
	"""Returns a copy of the query dictionary for which values in key-value
	   pairs have been parsed from string representations into primitives.
	"""
	for q in query:
		query[q] = basic.parseStrValue(query[q][0])
	return query
	
def application(env, start_response):
	"""Defines the WSGI-based server application that routes queries to the
	   appropriate parser based on file extension.
	"""
	f, x = path.splitext(env['PATH_INFO'])
	q = parse_qs(env['QUERY_STRING'])
	filters = parseQueryValues(q)
	file = path.dirname(path.realpath(__file__)) + '/data/' + env['PATH_INFO']
	if x in mimeTypes:
		start_response('200 OK', [('Content-Type', mimeTypes[x])])
	else:
		start_response('200 OK', [('Content-Type', 'text/html')])
	if x in parsers:
		return [parsers[x](file, filters)]
	else:
		raise Exception('Unable to determine parser for extension %s' % x)
		
def start(host='127.0.0.1', port=1337):
	"""Initializes a pyroclast server using CherryPy's WSGI webserver. Defaults
	   to hosting on 127.0.0.1 at port 1337, which can be changed using this
	   function's parameters.
	"""
	cherrypy.tree.graft(application, '/')
	cherrypy.server.unsubscribe()
	server = cherrypy._cpserver.Server()
	server.socket_host = host
	server.socket_port = port
	server.threat_pool = 30
	server.subscribe()
	cherrypy.engine.start()
	cherrypy.engine.block()
	
if __name__ == '__main__':
	start()
