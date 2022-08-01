========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/PyGko/badge/?style=flat
    :target: https://PyGko.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/hpsim/PyGko/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/hpsim/PyGko/actions

.. |requires| image:: https://requires.io/github/hpsim/PyGko/requirements.svg?branch=develop
    :alt: Requirements Status
    :target: https://requires.io/github/hpsim/PyGko/requirements/?branch=develop

.. |codecov| image:: https://codecov.io/gh/hpsim/PyGko/branch/develop/graphs/badge.svg?branch=develop
    :alt: Coverage Status
    :target: https://codecov.io/github/hpsim/PyGko

.. |version| image:: https://img.shields.io/pypi/v/pygko.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pygko

.. |wheel| image:: https://img.shields.io/pypi/wheel/pygko.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pygko

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pygko.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pygko

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pygko.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pygko

.. |commits-since| image:: https://img.shields.io/github/commits-since/hpsim/PyGko/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/hpsim/PyGko/compare/v0.0.0...develop



.. end-badges

A package bringing Ginkgo functionalities to python

* Free software: BSD 3-Clause License

Installation
============

::

    pip install pygko

You can also install the in-development version with::

    pip install https://github.com/hpsim/PyGko/archive/develop.zip


Documentation
=============


https://PyGko.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
