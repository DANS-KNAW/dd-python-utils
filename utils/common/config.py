import os
from os.path import exists
from shutil import copyfile
import yaml


def ensure_config_yml_exists(config_yml, example_config_yml):
    if not exists(config_yml):
        print("No config.yml found; copying example-config.yml to config.yml")
        copyfile(example_config_yml, config_yml)


def read_config_file():
    """
    Reads the settings from a yaml file into a dictionary. This yaml file must be located in the cfg subdirectory of
    this project.

    :param config_file_name: the base name of the yaml file
    :return: a dictionary
    """
    filepath = os.path.realpath(__file__)
    example_config_yml = os.path.normpath(os.path.join(filepath, "../../../example-config.yml"))
    config_yml = os.path.normpath(os.path.join(filepath, "../../../config.yml"))
    ensure_config_yml_exists(config_yml, example_config_yml)
    with open(config_yml, 'r') as stream:
        config = yaml.safe_load(stream)
        return config
