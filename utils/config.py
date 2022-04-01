import configparser
import os

filepath = os.path.realpath(__file__)
# Config

# Note: You should have something similar to a VM (with Vagrant or Docker) running Dataverse
# for doing (integration) tests, which you MUST do before running anything on production!

# the file defaults to inside work dir, but maybe have it overidden by environment or commandline params?
CONFIG_FILE = os.path.normpath(os.path.join(filepath, "../../work/config.ini"))

# read the ini file from the work dir
# remember to create this 'work' dir and not add it to Git!
config = configparser.ConfigParser()
files_read = config.read(CONFIG_FILE)

# Could use dynaconf instead of the configparser
# https: // dynaconf.readthedocs.io / en / docs_223 / guides / usage.html
# poetry add dynaconf

if not files_read:
    print("No config files read, please check: " + CONFIG_FILE)
    exit()

# for now, use global vars but might be placed in Settings class tha we can pass around
DATAVERSE_API_TOKEN = config.get('DATAVERSE', 'API_TOKEN')
SERVER_URL = config.get('DATAVERSE', 'SERVER_URL')
PIDS_INPUT_FILE = config.get('FILES', 'PIDS_INPUT_FILE')
OUTPUT_DIR = config.get('FILES', 'OUTPUT_DIR')
