"""Unit tests for flat data table parsing
"""

import unittest
from pyroclast import data, objectHierarchies

class JsonTests(unittest.TestCase):
	def test_get(self):
		file = data.get_path('test.json')
		content = objectHierarchies.getJson(file)
		
	def test_filter(self):
		file = data.get_path('test.json')
		content = objectHierarchies.getJson(file, {'isPrime': True})

if __name__ == "__main__":
	unittest.main()
