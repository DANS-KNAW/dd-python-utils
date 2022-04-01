import argparse
import os

import utils.config as CONFIG

from utils.common.batch_processing import batch_process
from utils.common.ds_pidsfile import load_pids
from utils.common.dv_api import reindex_dataset


def reindex_dataset_command(server_url, pids_file):
    # look for inputfile in configured OUTPUT_DIR
    full_name = os.path.join(CONFIG.OUTPUT_DIR, pids_file)
    pids = load_pids(full_name)

    # could be fast, but depends on number of files inside the dataset
    batch_process(pids, lambda pid: reindex_dataset(server_url), CONFIG.OUTPUT_DIR, delay=1.5)

# Note this done is via the admin api
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reindex datasets with the pids in the given inputfile')
    parser.add_argument('-p', '--pids_file', default='dataset_pids.txt', help='The input file with the dataset pids')
    args = parser.parse_args()

    server_url = CONFIG.SERVER_URL

    reindex_dataset_command(server_url, args.pids_file)
