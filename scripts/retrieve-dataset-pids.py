#!/usr/bin/env python3

import argparse
import logging

from common.config import init
from common.ds_pidsfile import store_pids
from common.dv_search import get_dataset_pids_from_search


def retrieve_dataset_pids_command(config, dataverse_alias, output_filename):
    logging.info(msg=("Retrieving dataset PIDs from URL %, dataverse %", config['dataverse']['server_url'], dataverse_alias))
    pids = get_dataset_pids_from_search(config['dataverse']['server_url'], dataverse_alias)
    # store in work dir, for further processing and or inspection
    store_pids(pids, config['files']['output_dir'], output_filename)


if __name__ == '__main__':
    config = init()

    parser = argparse.ArgumentParser(description='Retrieves the pids for all published datasets in the given collection')
    parser.add_argument('-o', '--output', help='The output file, for storing the pids retrieved')
    parser.add_argument('dataverse_alias', help='The short name (or alias) of the dataverse (collection)')
    args = parser.parse_args()

    retrieve_dataset_pids_command(config, args.dataverse_alias, args.output)
