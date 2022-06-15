#!/usr/bin/env python3

import sys
import argparse
import os

from common.batch_processing import batch_process
from common.config import init
from common.ds_pidsfile import load_pids
from common.dv_api import delete_dataset_draft


def delete_dataset_command(server_url, api_token, pids_file):
    # look for inputfile in configured OUTPUT_DIR
    full_name = os.path.join(config['files']['output_dir'], pids_file)
    pids = load_pids(full_name)

    # delete DRAFT version!
    batch_process(pids, lambda pid: delete_dataset_draft(server_url, api_token, pid), config['files']['output_dir'], delay=2.0)


if __name__ == '__main__':
    config = init()
    parser = argparse.ArgumentParser(description='Delete datasets with the pids in the given inputfile. '
                                                 'Only the draft version is deleted '
                                                 'and it will fail if it is not a draft!')
    parser.add_argument('-p', '--pids_file', default='dataset_pids.txt', help='The input file with the dataset pids')
    # maybe support a destroy option to also destroy the whole dataset, even if published
    args = parser.parse_args()

    server_url = config['dataverse']['server_url']
    api_token = config.DATAVERSE_API_TOKEN

    print("Deleting datasets on: {}".format(server_url))
    print("Be aware that this is irreversible and you might lose information!")
    # Only proceed if user is sure
    if not input("Are you sure? (y/n): ").lower().strip()[:1] == "y" : print("Cancelling deletion"), sys.exit(1)
    print("Starting deletion")

    delete_dataset_command(server_url, api_token, args.pids_file)
