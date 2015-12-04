"""Basic data handling mechanisms for lists of dictionaries, including alignment
   (i.e., given all dictionaries in a list uniform keysets), filtering, and
   string value parsing.
"""

def filter(dicts, filters):
	"""Returns a subset of the given entries in dicts (a list of dictionaries)
	   for which the fields specified in the filters dictionary have the
	   corresponding values.
	"""
	toKeep = []
	for d in dicts:
		isSatisfied = True
		for f in filters:
			if f not in d:
				isSatisfied = False
			elif d[f] != filters[f]:
				isSatisfied = False
		if isSatisfied:
			toKeep.append(d)
	return toKeep

def align(dicts):
	"""Returns a transformation of the given list of dictionaries in which all
	   dictionary entries have identical fields (with None values assigned for
	   those fields that did not previously exist).
	"""
	s = set()
	for d in dicts:
		s = s.union(set(d.keys()))
	for d in dicts:
		for f in s:
			if f not in d:
				d[f] = None
	return dicts

def parseStrValue(strValue):
	"""Returns a parsed version of the given string respresentation of a
	   primitive value into a logical, numeric, or string value.
	"""   
	if strValue.lower() == 'true':
		return True
	elif strValue.lower() == 'false':
		return False
	else:
		try:
			f = float(strValue)
		except:
			return strValue
		else:
			return f
