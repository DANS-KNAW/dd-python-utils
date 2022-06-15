import os
from os.path import exists
from shutil import copyfile
import yaml


def ensure_config_yml_exists(config_yml, example_config_yml):
    if not exists(config_yml):
        print("No config.yml found; copying example-config.yml to config.yml")
        copyfile(example_config_yml, config_yml)


def init():
    """
    Initialization function to run by each script. It creates the work directory if it doesn't exist yet and it reads
    config.yml. If config.yml does not exist yet then it is first created from example-config.yml

    :return: a dictionary
    """
    local_path = os.path.dirname(__file__)
    work_path = os.path.join(local_path, '../../work')
    if os.path.isdir(work_path):
        print("Skipping dir creation, because it already exists: %s" % work_path)
    else:
        print("Creating work dir: " + work_path)
        os.makedirs(work_path)

    filepath = os.path.realpath(__file__)
    example_config_yml = os.path.normpath(os.path.join(filepath, "../../../example-config.yml"))
    config_yml = os.path.normpath(os.path.join(filepath, "../../../config.yml"))
    ensure_config_yml_exists(config_yml, example_config_yml)
    with open(config_yml, 'r') as stream:
        config = yaml.safe_load(stream)
        return config
