dd-python-utils
===============

Utility scripts for Data Station application management

SYNOPSIS
--------

    # Set-up
    git clone https://github.com/DANS-KNAW/dd-python-utils.git
    cd dd-python-utils
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    
    # Running scripts
    ./scripts/publish-dataset.py --help
    
    # stop using the environment 
    # (logging out of the server or your computer will also deactivate the env)
    deactivate

    # (Re-)generate docs
    ./generate-docs.sh

DESCRIPTION
-----------
This project contains several scripts to automate tasks for Data Station application managers. The scripts should be run
in a Python virtual environment. See the SYNOPSIS above for how to set this up.

### Development

This project was setup with Poetry, a dependency management tool for Python: [Poetry](https://python-poetry.org/docs/).
Poetry is not required to run the scripts. The current use is mainly to generate or update the `requirement.txt` file:

    poetry export -f requirements.txt --output requirements.txt

In the future we may use poetry to build installable packages.

The docstrings in the code must be compatible with what `pdoc3` expects, as that is what we are using to generate the
html pages from the docstrings.


INSTALLATION & CONFIGURATION
----------------------------

See the [SYNOPSIS](#synopsis). To generate html doc pages from the code call `./generate-docs.sh` inside the active
virtual environment. The docs will be output/refreshed under `html/`.

