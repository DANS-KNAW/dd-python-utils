import argparse
import os
import json

import utils.config as CONFIG

from utils.common.batch_processing import batch_process
from utils.common.ds_pidsfile import load_pids

from utils.common.dv_api import get_dataset_locks, delete_dataset_locks


def unlock_dataset_action(server_url, api_token, pid):
    deleted_locks = False
    resp_data = get_dataset_locks(server_url, pid)
    # print(json.dumps(resp_data, indent=2))
    if len(resp_data) == 0:
        print("No locks")
        print("Leave as-is")
    else:
        print("Found locks")
        print(json.dumps(resp_data, indent=2))
        # delete
        print("Try deleting the locks")
        delete_dataset_locks(server_url, api_token, pid)
        print("Done")
        deleted_locks = True

    return deleted_locks


def reindex_dataset_command(server_url, api_token, pids_file):
    # look for inputfile in configured OUTPUT_DIR
    full_name = os.path.join(CONFIG.OUTPUT_DIR, pids_file)
    pids = load_pids(full_name)

    # could be fast, but depends on number of files inside the dataset
    batch_process(pids, lambda pid: unlock_dataset_action(server_url, api_token, pid), CONFIG.OUTPUT_DIR, delay=1.5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Unlock datasets (if locked) with the pids in the given inputfile')
    parser.add_argument('-p', '--pids_file', default='dataset_pids.txt', help='The input file with the dataset pids')
    args = parser.parse_args()

    server_url = CONFIG.SERVER_URL
    api_token = CONFIG.DATAVERSE_API_TOKEN

    reindex_dataset_command(server_url, api_token, args.pids_file)
