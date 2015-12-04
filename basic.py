"""Basic data handling mechanisms for lists of dictionaries, including alignment
   (i.e., given all dictionaries in a list uniform keysets), filtering, and
   string value parsing.
"""

def filter(dicts, filters):
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
	s = set()
	for d in dicts:
		s = s.union(set(d.keys()))
	for d in dicts:
		for f in s:
			if f not in d:
				d[f] = None
	return dicts
	
def parseStrValue(strValue):
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
