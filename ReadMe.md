File2Package.backend.dpkg [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=========================
[![GitLab Build Status](https://gitlab.com/File2Package.py/File2Package.backend.dpkg/badges/master/pipeline.svg)](https://gitlab.com/File2Package.py/File2Package.backend.dpkg/pipelines/master/latest)
![GitLab Coverage](https://gitlab.com/File2Package.py/File2Package.backend.dpkg/badges/master/coverage.svg)
[![Coveralls Coverage](https://img.shields.io/coveralls/KOLANICH/File2Package.backend.dpkg.svg)](https://coveralls.io/r/KOLANICH/File2Package.backend.dpkg)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/File2Package.backend.dpkg.svg)](https://libraries.io/github/KOLANICH/File2Package.backend.dpkg)

A backend to fetch the data from dpkg database.

See [`tests/tests.py`](./tests/tests.py) for the examples.

Requirements
------------
* [`Python >=3.4`](https://www.python.org/downloads/). [`Python 2` is dead, stop raping its corpse.](https://python3statement.org/) Use `2to3` with manual postprocessing to migrate incompatible code to `3`. It shouldn't take so much time. For unit-testing you need Python 3.6+ or PyPy3 because their `dict` is ordered and deterministic. Python 3 is also semi-dead, 3.7 is the last minor release in 3.
* [`datrie`](https://github.com/pytries/datrie) for a prefix tree.
* [`debparse` fork](https://github.com/KOLANICH/python-debparse)
