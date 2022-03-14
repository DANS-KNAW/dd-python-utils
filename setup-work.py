import os
import shutil

# create work dir (not in version control) if it does not exist
local_path = os.path.dirname(__file__)
work_path = os.path.join(local_path, 'work')
if os.path.isdir(work_path):
    print("Skipping dir creation, because it already exists: " + work_path)
else:
    print("Creating work dir: " + work_path)
    os.makedirs(work_path)

# create initial config.ini if it does not exist
config_file_path = os.path.join(work_path, 'config.ini')
if os.path.isfile(config_file_path):
    print("Skipping config file copy, because it already exists: " ++ config_file_path)
else:
    print("Copying initial config file: " + config_file_path)
    empty_config_path = os.path.join(local_path, 'config.ini.empty')
    shutil.copy(empty_config_path, config_file_path)