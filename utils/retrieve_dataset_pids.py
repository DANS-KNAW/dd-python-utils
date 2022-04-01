import argparse

import utils.config as CONFIG

from utils.common.ds_pidsfile import store_pids
from utils.common.dv_search import get_dataset_pids_from_search


def retrieve_dataset_pids_command(dataverse_alias, output_filename):
    print('Args: ' + dataverse_alias + ',  ' + output_filename)
    print("Example using server URL: " + CONFIG.SERVER_URL)
    pids = get_dataset_pids_from_search(CONFIG.SERVER_URL, dataverse_alias)
    # store in work dir, for further processing and or inspection
    store_pids(pids, CONFIG.OUTPUT_DIR, output_filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Retrieves the pids for all published datasets in the given collection')
    parser.add_argument('-o', '--output', default='dataset_pids.txt', help='The output file, for storing the pids retrieved')
    parser.add_argument('dataverse_alias', help='The short name (or alias) of the dataverse (collection)')
    args = parser.parse_args()

    retrieve_dataset_pids_command(args.dataverse_alias, args.output)
