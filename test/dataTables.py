"""Unit tests for flat data table parsing
"""

import unittest
from pyroclast import data, dataTables

class CsvTests(unittest.TestCase):
	def test_get(self):
		file = data.get_path('test.csv')
		content = dataTables.getCsv(file)
		
	def test_filter(self):
		file = data.get_path('test.csv')
		content = dataTables.getCsv(file, {'isPrime': True})

if __name__ == "__main__":
	unittest.main()
