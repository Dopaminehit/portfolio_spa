portfolio_spa - Portfolio Website Repository
==========================================

Brewing beer, stay tuned. Await time directly proportional to taste (not true for beer though)

Development Instructions
==========================

As best practice, it is recommended to use virtual environment for python.
It can be setup and activated using the following commands:

::

    python3 -m venv .venv
    source .venv/bin/activate


Install flit in activated venv:

::
    
    pip install flit

Using flit, install necessary dependencies. Below command does install
dependencies mentioned in pyproject.toml file.

::

    flit install -s

Checks to be made before every Push (will be moved to CI part at later point of time)

::

    black mmcore/
    isort mmcore/
    flake8 mmcore/
    mypy mmcore/
