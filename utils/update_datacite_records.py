import argparse

import requests
from requests.auth import HTTPBasicAuth

from utils.common.batch_processing import batch_process
from utils.common.config import read_config_file
from utils.common.ds_pidsfile import load_pids
from utils.common.dv_api import get_dataset_metadata_export


def send_metadata_to_mds(config, doi, metadata):
    url = '%s/metadata/%s' % (config['datacite']['mds_endpoint'], doi)
    response = requests.put(
        url=url,
        auth=HTTPBasicAuth(config['datacite']['username'], config['datacite']['password']),
        headers={
            'Content-Type': 'application/xml;charset=UTF-8'
        },
        data=metadata)
    print(response.status_code)

def update_datacite_record(config):
    def update_datacite_record_for_pid(pid):
        md = get_dataset_metadata_export(config['dataverse']['server_url'], pid, 'Datacite', response_is_json=False)
        send_metadata_to_mds(config, pid, md)
        return False

    return update_datacite_record_for_pid


def update_datacite_records(config, pid_file):
    pids = load_pids(pid_file)
    batch_process(pids, update_datacite_record(config), logging_dir='../work/', delay=1)


if __name__ == '__main__':
    config = read_config_file()

    parser = argparse.ArgumentParser(
        description='Downloads the DataCite metadata from Dataverse for a list of datasets and updates DataCite with '
                    'those records')
    parser.add_argument('dataset_pids', help='Newline separated file with dataset PIDs')
    args = parser.parse_args()
    update_datacite_records(config, args.dataset_pids)
