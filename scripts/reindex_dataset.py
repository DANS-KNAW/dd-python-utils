#!/usr/bin/env python3

import argparse
import os

from common.batch_processing import batch_process
from common.config import init
from common.ds_pidsfile import load_pids
from common.dv_api import reindex_dataset


def reindex_dataset_command(server_url, pids_file):
    # look for inputfile in configured OUTPUT_DIR
    full_name = os.path.join(config['files']['output_dir'], pids_file)
    pids = load_pids(full_name)

    # could be fast, but depends on number of files inside the dataset
    batch_process(pids, lambda pid: reindex_dataset(server_url, pid), config['files']['output_dir'], delay=1.5)

# Note this done is via the admin api
if __name__ == '__main__':
    config = init()
    parser = argparse.ArgumentParser(description='Reindex datasets with the pids in the given inputfile')
    parser.add_argument('-p', '--pids_file', default='dataset_pids.txt', help='The input file with the dataset pids')
    args = parser.parse_args()

    server_url = config['dataverse']['server_url']

    reindex_dataset_command(server_url, args.pids_file)
