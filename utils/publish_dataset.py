import argparse
import os

from utils.common.batch_processing import batch_process
from utils.common.config import read_config_file
from utils.common.ds_pidsfile import load_pids
from utils.common.dv_api import publish_dataset


def publish_dataset_command(server_url, api_token, pids_file, type):
    # look for inputfile in configured OUTPUT_DIR
    full_name = os.path.join(config['files']['output_dir'], pids_file)
    pids = load_pids(full_name)

    # Long delay because publish is doing a lot after the async. request is returning
    # and sometimes datasets get locked
    batch_process(pids, lambda pid: publish_dataset(server_url, api_token, pid, type), config['files']['output_dir'], delay=5.0)


if __name__ == '__main__':
    config = read_config_file()
    parser = argparse.ArgumentParser(description='Published datasets with the pids in the given inputfile')
    parser.add_argument('-p', '--pids_file', default='dataset_pids.txt', help='The input file with the dataset pids')
    parser.add_argument('-t', '--type', default='major', help='The type of version upgrade, minor for metadata changes, otherwise major.')
    args = parser.parse_args()

    server_url = config['dataverse']['server_url']
    api_token = config.DATAVERSE_API_TOKEN

    publish_dataset_command(server_url, api_token, args.pids_file, args.type)
