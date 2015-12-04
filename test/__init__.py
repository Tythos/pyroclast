"""Defines test module contents and, when invoked directly, executes all tests.
"""

import unittest
import sys
import importlib
import types

if sys.version_info.major == 2:
	def is_test_case(c):
		return type(c) == types.TypeType and issubclass(c, unittest.TestCase)
else:
	def is_test_case(c):
		return isinstance(c, type) and issubclass(c, unittest.TestCase)

__all__ = [
	'basic',
	'dataTables',
	'objectHierarchies'
]

def suite():
	"""Constructs and returns a test suite of cases from all test modules
	   defined in this module's __all__ variable.
	"""
	ts = unittest.TestSuite()
	for test_module in __all__:
		m = importlib.import_module("pyroclast.test." + test_module)
		for n in dir(m):
			c = getattr(m, n)
			if is_test_case(c):
				s = unittest.TestLoader().loadTestsFromTestCase(c)
				ts.addTests(s)
	return ts
				
def runAllTests():
	"""Executes the test suite constructed in suite() using a text test runner
	   and prints the resulting statistics.
	"""
	ttr = unittest.TextTestRunner(verbosity=3).run(suite())
	nTests = ttr.testsRun + len(ttr.skipped)
	print("Report:")
	print("\t" + str(len(ttr.failures)) + "/" + str(nTests) + " failed")
	print("\t" + str(len(ttr.errors)) + "/" + str(nTests) + " errors")
	print("\t" + str(len(ttr.skipped)) + "/" + str(nTests) + " skipped")

if __name__ == '__main__':
	runAllTests()
	