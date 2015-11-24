"""Unit tests for flat data table parsing
"""

import unittest
from pyroclast import basic

class FilterTests(unittest.TestCase):
	def test_basic(self):
		dicts = [{'one': 1}, {'two': 2}]
		dicts = basic.filter(dicts, {})
		
	def test_filter(self):
		dicts = [{'one': 1}, {'two': 2}]
		dicts = basic.filter(dicts, {'one': 1})

class AlignTests(unittest.TestCase):
	def test_basic(self):
		d1 = {'one': 1, 'two': 2}
		d2 = {'one': 1, 'three': 3}
		d = basic.align([d1,d2])

class ParseTests(unittest.TestCase):
	def test_string(self):
		s = 'testing'
		self.assertEqual(basic.parseStrValue(s), s)
		
	def test_numeric(self):
		n = -3.14e-19
		self.assertEqual(basic.parseStrValue(str(n)), n)
		
	def test_logical(self):
		self.assertEqual(basic.parseStrValue('true'), True)
		self.assertEqual(basic.parseStrValue('TRUE'), True)
		self.assertEqual(basic.parseStrValue('FALSE'), False)
		self.assertEqual(basic.parseStrValue('false'), False)
		
if __name__ == "__main__":
	unittest.main()
