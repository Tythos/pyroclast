"""Handlers for data formats structured around an object hierarchy, as opposed to a flat data table, such as JSON and XML
"""

from pyroclast import basic
import json

def getJson(file, filters={}):
	with open(file, 'r') as f:
		j = json.loads(f.read())
	all = j['']
	dicts = basic.filter(all, filters)
	if len(dicts) > 0:
		return formatJson(dicts)
	else:
		raise Exception('No matching data entries found')
	
def formatJson(dicts):
	return json.dumps({"":dicts})
