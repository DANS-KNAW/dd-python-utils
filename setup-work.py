import os
import shutil

# create work dir (not in version control) if it does not exist
local_path = os.path.dirname(__file__)
work_path = os.path.join(local_path, 'work')
if os.path.isdir(work_path):
    print("Skipping dir creation, because it already exists: %s" % work_path)
else:
    print("Creating work dir: " + work_path)
    os.makedirs(work_path)

# create initial config.yml if it does not exist
