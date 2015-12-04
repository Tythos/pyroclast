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

class XmlTests(unittest.TestCase):
	def test_get(self):
		file = data.get_path('test.xml')
		content = objectHierarchies.getXml(file)
		
	def test_filter(self):
		file = data.get_path('test.xml')
		content = objectHierarchies.getXml(file, {'isPrime': True})
		
class UnqliteTests(unittest.TestCase):
	def test_get(self):
		file = data.get_path('test.unq')
		content = objectHierarchies.getUnqlite(file)

	def test_key(self):
		file = data.get_path('test.unq')
		content = objectHierarchies.getUnqlite(file, {'_key':'myKey'})

	def test_collection(self):
		file = data.get_path('test.unq')
		content = objectHierarchies.getUnqlite(file, {'_collection':'entries', 'isPrime':True})

if __name__ == "__main__":
	unittest.main()
