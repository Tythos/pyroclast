"""Handlers for data formats structured around an object hierarchy, as opposed to a flat data table, such as JSON and XML
"""

from pyroclast import basic
import json
from xml.etree import ElementTree as xet
from unqlite import UnQLite as unq
import re

def getJson(file, filters={}):
	with open(file, 'r') as f:
		j = json.loads(f.read())
	all = j['']
	dicts = basic.filter(all, filters)
	if len(dicts) > 0:
		return formatJson(dicts)
	else:
		raise Exception('No matching data entries found')
	
def getXml(file, filters={}):
	root = xet.parse(file).getroot()
	all = [parseElement(el) for el in root]
	dicts = basic.filter(all, filters)
	if len(dicts) > 0:
		return formatJson(dicts,root.tag)
	else:
		raise Exception('No matching data entries found')
		
def getUnqlite(file, filters={}):
	db = unq(file)
	if '_collection' in filters:
		c = filters.pop('_collection')
		coll = db.collection(c)
		all = coll.all()
	elif '_key' in filters:
		key = filters.pop('_key')
		all = [{key: db[key]}]
	else:
		all = [{'_root':{}}]
		for key,value in db:
			c = db.collection(key)
			if c.exists():
				all.append({key: c.all()})
			else:
				isKey = True
				if re.search('_\d+$', key):
					c = db.collection(re.sub('_\d+$', '', key))
					isKey = not c.exists()
				if isKey:
					all.append({key:value})
					all[0]['_root'][key] = value
	dicts = basic.filter(all, filters)
	if len(dicts) > 0:
		return formatJson(dicts)
	else:
		raise Exception('No matching data entries found')
			
def parseElement(el):
	"""Recursively converts an XML element to a dictionary object. After the
	   initial pass, children are checked for single-value elements that are
	   duplicated as element attributes. Meta-attributes include:
	      _tag, the tag name of the element
		  _children, a list of dictionaries defining child elements
		  _text, the parsed value of any element text content
	   All attribute and text values are parsed for boolean and numeric values.
	"""
	d = el.attrib
	for k in d.keys():
		d[k] = basic.parseStrValue(d[k])
	d['_tag'] = el.tag
	d['_children'] = [parseElement(child) for child in el]
	if el.text is not None:
		d['_text'] = basic.parseStrValue(el.text.strip())
	if len(d['_children']) > 0:
		for ch in d['_children']:
			if ch.keys() == ['_text','_tag']:
				d[ch['_tag']] = ch['_text']
	else:
		d.pop('_children')
	return d
	
def formatJson(dicts, key=""):
	return json.dumps({key:dicts})
