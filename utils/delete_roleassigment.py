import argparse
import os

import utils.config as CONFIG

from utils.common.batch_processing import batch_process
from utils.common.ds_pidsfile import load_pids
from utils.common.dv_api import delete_dataset_roleassigment, get_dataset_roleassigments


def delete_roleassigment_action(server_url, api_token, pid, role_assignee, role_alias):
    deleted_role = False
    resp_data = get_dataset_roleassigments(server_url, api_token, pid)
    # print(json.dumps(resp_data, indent=2))
    for role_assignment in resp_data:
        assignee = role_assignment['assignee']
        # role_id = role_assignment['roleId']
        alias = role_assignment['_roleAlias']
        print("Role assignee: " + assignee + ', role alias: ' + alias)
        if assignee == role_assignee and alias == role_alias:
            # delete this one
            assignment_id = role_assignment['id']
            print("Try deleting the role assignment")
            delete_dataset_roleassigment(server_url, api_token, pid, assignment_id)
            print("Done")
            deleted_role = True
        else:
            print("Leave as-is")
    return deleted_role

def delete_roleassigment_command(server_url, api_token, pids_file, role_assignee, role_alias):
    # look for inputfile in configured OUTPUT_DIR
    full_name = os.path.join(CONFIG.OUTPUT_DIR, pids_file)
    pids = load_pids(full_name)

    # could be fast, but depends on number of files inside the dataset
    batch_process(pids, lambda pid: delete_roleassigment_action(server_url, api_token, pid, role_assignee, role_alias), CONFIG.OUTPUT_DIR, delay=1.5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Delete role assigment for datasets with the pids in the given inputfile')
    parser.add_argument("role_assignee", help="Role assignee (example: @dataverseAdmin)")
    parser.add_argument("role_alias", help="Role alias (example: contributor")
    parser.add_argument('-p', '--pids_file', default='dataset_pids.txt', help='The input file with the dataset pids')
    args = parser.parse_args()

    role_assignee = args.role_assignee
    role_alias = args.role_alias

    server_url = CONFIG.SERVER_URL
    api_token = CONFIG.DATAVERSE_API_TOKEN

    delete_roleassigment_command(server_url, api_token, args.pids_file, role_assignee, role_alias)
