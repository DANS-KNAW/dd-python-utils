import argparse
import os

import config

from utils.batch_processing import batch_process
from utils.ds_pidsfile import load_pids
from utils.dv_api import publish_dataset


def publish_dataset_command(pids_file, type):
    # look for inputfile in configured OUTPUT_DIR
    full_name = os.path.join(config.OUTPUT_DIR, pids_file)
    pids = load_pids(full_name)

    # Long delay because publish is doing a lot after the async. request is returning... and sometimes datasets get locked
    batch_process(pids, lambda pid: publish_dataset(config.SERVER_URL, pid, type), delay=5.0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Published datasets with the pids in the given inputfile')
    parser.add_argument('-p', '--pids_file', default='dataset_pids.txt', help='The input file with the dataset pids')
    parser.add_argument('-t', '--type', default='major', help='The type of version upgrade, minor for metadata changes, otherwise major.')
    args = parser.parse_args()

    publish_dataset_command(args.pids_file, args.type)