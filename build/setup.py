from setuptools import setup, find_packages
import pypandoc

setup(
	name='pyroclast',
	version='1.0.0',
	packages=find_packages(),
	install_requires=['xlrd>=0.9.4','unqlite>=0.4.1'],
	package_data={
		'': ['*.html','*.txt','*.md','*.json','*.csv','*.sql','*.unq','*.xlsx','*.xls','*.xml']
	},
	author='Brian Kirkpatrick',
	author_email='code@tythos.net',
	description='Basic Python-based data server for exposing flat table and object hierarchy files via REST-ful queries',
	long_description=pypandoc.convert('pyroclast/README.md', 'rst'),
	license='MIT',
	keywords='rest server json csv sqlite unqlite excel xml',
	url='https://github.com/Tythos/pyroclast',
	test_suite='pyroclast.test.suite',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
		'Intended Audience :: Science/Research',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Topic :: Database :: Database Engines/Servers',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Scientific/Engineering :: Information Analysis',
		'Programming Language :: Python :: 2',
	],
)
