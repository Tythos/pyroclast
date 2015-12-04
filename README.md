# pyroclast
Basic Python-based data server for exposing flat table and object hierarchy files via REST-ful queries

You know what's awesome? Setting up a REST-ful server you can start with a single command, out-of-the-box.

You know what's even cooler? Adding file resources to that server just by dragging and dropping said files into a folder.

Welcome to pyroclast.

# Get Started

To start a Pyroclast instance, simply point the Python interpreter to the server.py file:
> python server.py

Alternatively, you can import server and start an instance manually from within Python:
>>> from pyroclast import server
>>> server.start()

Once the server is started, you will see a blank HTTP response for 127.0.0.1:1337. This means it's working!

# Get Served

Within the Pyroclast package, the 'data/' folder contains all files your server will host. This can include:
* JavaScript Object Notation files (.JSON)
* Comma-Seperated Value files (.CSV)
* Excel files (.XLS, .XLSX)
* SQLite database files (.SQL)
* UnQLite database files (.UNQ)
* eXtensible Markup Language files (.XML)

To add a file, simply copy it into the Pyroclast package's 'data/' folder and the Pyroclast server will do the rest.

Alternatively, you can serve a file procedurally using the data module's serve() function, which will copy directory contents into 'data/':
>>> from pyroclast import data
>>> data.serve('/path/to/my/file.xlsx')

# Get Your Data

Once your server is up and running, you can query files from a URL based on the file path relative to 'data/'--i.e., if 'test.xlsx' is in 'data/', it is accessed by the URL 'http://127.0.0.1:1337/test.xlsx'.

All data queried will be returned in one of two formats:
* A CSV-formatted text table (for flat data table formats, like .CSV, .XLS/.XLSX, and .SQL)
* A JSON-formatted text tree (for object hierarchy formats, like .JSON, .XML, and .UNQ)

Specific subsets of data from a source can be selected using the query segment of the URL (i.e., ?key=value&key2=value2). In addition to down-selecting the returned data set based on attribute key-value pairs, there are several format-specific keys that can be used. (Note that there are no format-specific keys for .JSON, .XML, and .CSV formats).

## .XLS/.XLSX

Excel spreadsheets can contain multiple sheets. Pyroclast assumes each queried sheet is a flat table starting from the first row (a header) and first column. Specific sheets can be selected in one of two ways:
* Passing the name of the desired sheet as the value of the '_sheet' key
* Passing the index of the desired sheet (starting with 0) as the value of the '_sheet' key

In cases where no '_sheet' value is given, Pyroclast will default to the first sheet in the file.

In cases where sheets are given integer values as names, Pyroclast will default to the string interpretation.

## .SQL

SQLite database files require a query indicate a specific table. This is done by passing the desired table name as a value of the '_table' key. If the '_table' key is not specified, an error will be raised.

## .UNQ

UnQLite is a funny beast. .UNQ database files can contain both key-value pairs AND collections of related object hierarchies.
* The '_collection' key can be used to indicate a specific collection.
* The '_key' key can be used to indicate the key of a specific key-value pair.

If neither '_collection' or '_key' is indicated, Pyroclast will return all contents of the database. Key-value pairs will be included in the response twice:
* Once as single-entry dictionaries at the root level of the response
* Once as entries to a dictionary assigned to the '_root' key
