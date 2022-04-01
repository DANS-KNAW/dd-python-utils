import argparse
import os

import utils.config as CONFIG

from utils.common.batch_processing import batch_process
from utils.common.ds_pidsfile import load_pids
from utils.common.dv_api import publish_dataset


def publish_dataset_command(server_url, api_token, pids_file, type):
    # look for inputfile in configured OUTPUT_DIR
    full_name = os.path.join(CONFIG.OUTPUT_DIR, pids_file)
    pids = load_pids(full_name)

    # Long delay because publish is doing a lot after the async. request is returning
    # and sometimes datasets get locked
    batch_process(pids, lambda pid: publish_dataset(server_url, api_token, pid, type), CONFIG.OUTPUT_DIR, delay=5.0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Published datasets with the pids in the given inputfile')
    parser.add_argument('-p', '--pids_file', default='dataset_pids.txt', help='The input file with the dataset pids')
    parser.add_argument('-t', '--type', default='major', help='The type of version upgrade, minor for metadata changes, otherwise major.')
    args = parser.parse_args()

    server_url = CONFIG.SERVER_URL
    api_token = CONFIG.DATAVERSE_API_TOKEN

    publish_dataset_command(server_url, api_token, args.pids_file, args.type)