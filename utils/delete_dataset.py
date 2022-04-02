import sys
import argparse
import os

import utils.config as CONFIG
from utils.common.batch_processing import batch_process
from utils.common.ds_pidsfile import load_pids
from utils.common.dv_api import delete_dataset_draft


def delete_dataset_command(server_url, api_token, pids_file):
    # look for inputfile in configured OUTPUT_DIR
    full_name = os.path.join(CONFIG.OUTPUT_DIR, pids_file)
    pids = load_pids(full_name)

    # delete DRAFT version!
    batch_process(pids, lambda pid: delete_dataset_draft(server_url, api_token, pid), CONFIG.OUTPUT_DIR, delay=2.0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Delete datasets with the pids in the given inputfile. '
                                                 'Only the draft version is deleted '
                                                 'and it will fail if it is not a draft!')
    parser.add_argument('-p', '--pids_file', default='dataset_pids.txt', help='The input file with the dataset pids')
    # maybe support a destroy option to also destroy the whole dataset, even if published
    args = parser.parse_args()

    server_url = CONFIG.SERVER_URL
    api_token = CONFIG.DATAVERSE_API_TOKEN

    print("Deleting datasets on: {}".format(server_url))
    print("Be aware that this is irreversible and you might lose information!")
    # Only proceed if user is sure
    if not input("Are you sure? (y/n): ").lower().strip()[:1] == "y" : print("Cancelling deletion"), sys.exit(1)
    print("Starting deletion")

    delete_dataset_command(server_url, api_token, args.pids_file)
