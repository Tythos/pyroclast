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
	'.json': 'text/plain'
}

parsers = {
	'.csv': dataTables.getCsv,
	'.xls': dataTables.getExcel,
	'.xlsx': dataTables.getExcel,
	'.sql': dataTables.getSqlite,
	'.json': objectHierarchies.getJson,
	'.ico': null
}

def parseQueryValues(query):
	for q in query:
		query[q] = basic.parseStrValue(query[q][0])
	return query
	
def application(env, start_response):
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
	
if __name__ == '__main__':
	cherrypy.tree.graft(application, '/')
	cherrypy.server.unsubscribe()

	server = cherrypy._cpserver.Server()
	server.socket_host = '127.0.0.1'
	server.socket_port = 1337
	server.threat_pool = 30
	server.subscribe()
	
	cherrypy.engine.start()
	cherrypy.engine.block()
