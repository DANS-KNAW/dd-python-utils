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
    
    # stop using
    deactivate

DESCRIPTION
-----------
This project contains several scripts to automate tasks for Data Station application managers. The scripts should be run
in a Python virtual environment. See the SYNOPSIS above for how to set this up.

### Development

This project was setup with Poetry, a dependency management tool for
Python: [Poetry docs](https://python-poetry.org/docs/). Poetry is not required to run the scripts. 


