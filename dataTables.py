"""Handlers for data formats structured around a flat data table, as opposed to
   an object hierarchy, such as CSV and Excel
"""

import csv
import xlrd
import io
import warnings
import sys
import sqlite3
from pyroclast import basic

if sys.version_info.major == 2:
	from io import BytesIO as Str
else:
	from io import StringIO as Str

def getCsv(file, filters={}):
	"""Given a specific CSV file (string) and a set of filters (dictionary
	   key-values pairs), will return a CSV-formatted table of the matching data
	   entries from that file (including a header row).
	"""
	all = []
	with open(file) as f:
		reader = csv.DictReader(f)
		for row in reader:
			for field in row:
				row[field] = basic.parseStrValue(row[field])
			all.append(row)
	dicts = basic.filter(all, filters)
	if len(dicts) > 0:
		return formatCsv(dicts)
	else:
		raise Exception('No matching data entries found')

def getExcel(file, filters={}):
	"""Given a specific Excel file (string) and a set of filters (dictionary
	   key-values pairs), will return a CSV-formatted table of the matching data
	   entries from that file (including a header row). Defaults to the first
	   sheet in the workbook; other sheets can be specified by name or
	   zero-based index using the '_sheet' parameter in the URL's query segment.
	"""
	wb = xlrd.open_workbook(file)
	if '_sheet' not in filters:
		warnings.warn('No worksheet specified (_sheet filter expected); defaulting to first worksheet')
		sheet = 0
	else:
		sheet = filters.pop('_sheet')
	if type(sheet) is type(''):
		ws = wb.sheet_by_name(sheet)
	else:
		ws = wb.sheet_by_index(int(sheet))
	header = [basic.parseStrValue(h.value) for h in ws.row(0)]
	all = []
	for i in range(1,ws.nrows):
		d = {}
		row = ws.row(i)
		for j,h in enumerate(header):
			entry = row[j]
			if entry.ctype == 4:
				value = str(entry.value == 1)
			else:
				value = str(entry.value)
			d[h] = basic.parseStrValue(value)
		all.append(d)
	dicts = basic.filter(all, filters)
	if len(dicts) > 0:
		return formatCsv(dicts)
	else:
		raise Exception('No matching data entries found')
		
def getSqlite(file, filters={}):
	"""Given a specific SQLite file (string) and a set of filters (dictionary
	   key-values pairs), will return a CSV-formatted table of the matching data
	   entries from that file (including a header row). Requres a '_table'
	   parameter in filters to query from the appropriate table.
	"""
	if '_table' not in filters:
		raise Exception('No table specified (_table filter expected)')
	table = filters.pop('_table')
	filtStrs = []
	for key,value in filters.iteritems():
		if type(value) is type(0.):
			filtStrs.append('%s=%s' % (key,str(value)))
		else:
			filtStrs.append("%s='%s'" % (key,str(value)))
	qry = 'SELECT * FROM %s%s' % (table, ' WHERE ' + ' AND '.join(filtStrs) if len(filters) > 0 else '')
	conn = sqlite3.connect(file)
	curs = conn.execute(qry)
	all = [r for r in curs]
	if len(all) > 0:
		dicts = []
		header = [d[0] for d in curs.description]
		for row in all:
			d = {}
			for ndx,h in enumerate(header):
				value = row[ndx]
				if type(value) is type(0.):
					d[h] = value
				else:
					d[h] = basic.parseStrValue(value)
			dicts.append(d)
		return formatCsv(dicts)
	else:
		raise Exception('No matching data entries found')
		
def formatCsv(dicts):
	"""Converts a list of dictionaries into a CSV-formatted flat table
	   (including a header row).
	"""
	dicts = basic.align(dicts)
	output = Str()
	writer = csv.DictWriter(output, dicts[0].keys())
	writer.writeheader()
	for d in dicts:
		writer.writerow(d)
	return output.getvalue()
