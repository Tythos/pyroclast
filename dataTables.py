"""Handlers for data formats structured around a flat data table, as opposed to an object hierarchy, such as CSV and Excel
"""

import csv
import io
from pyroclast import basic
import sys

if sys.version_info.major == 2:
	from io import BytesIO as Str
else:
	from io import StringIO as Str

def getCsv(file, filters={}):
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
	
def formatCsv(dicts):
	dicts = basic.align(dicts)
	output = Str()
	writer = csv.DictWriter(output, dicts[0].keys())
	writer.writeheader()
	for d in dicts:
		writer.writerow(d)
	return output.getvalue()
