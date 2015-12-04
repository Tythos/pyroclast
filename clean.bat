@echo off
del /F /Q /S *.pyc > NUL
rmdir __pycache__
rmdir data\__pycache__
rmdir docs\__pycache__
rmdir test\__pycache__
