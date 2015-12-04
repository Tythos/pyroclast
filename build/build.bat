@echo off
echo Building package... (you have updated setup.py parameters, right?)

rem Copy all package contents (except build/) into this directory
mkdir pyroclast
xcopy .. pyroclast > NUL
xcopy ..\data pyroclast\data\ /e > NUL
xcopy ..\docs pyroclast\docs\ /e > NUL
xcopy ..\test pyroclast\test\ /e > NUL
copy ..\README.md . > NUL

rem Run test suite
python setup.py test

rem Build, register, and publish package
python setup.py register sdist upload

rem Remove build artifacts
rmdir dist /S /Q
rmdir pyroclast /S /Q
rmdir pyroclast.egg-info /S /Q
del README.md
