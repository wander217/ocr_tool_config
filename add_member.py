import argparse
from doccano_api_client import DoccanoClient
from admin_config import ADMIN_CONFIG
from typing import List


def add_member(host_name: str,
               admin_username: str,
               admin_password: str,
               project_id: int,
               member_usernames: List[str],
               member_roles: List[str]):
    client = DoccanoClient(host_name, admin_username, admin_password)
    result = client.post_members(project_id, member_usernames, member_roles)
    print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Adding member to project")
    parser.add_argument("-pi", "--project_id", type=int, help="id of project")
    parser.add_argument("-mu", "--member_username", type=str, help="account of member")
    parser.add_argument("-rn", "--role_name", type=str, help="role name")
    arg = parser.parse_args()
    add_member(**ADMIN_CONFIG,
               project_id=arg.project_id,
               member_usernames=[arg.member_username],
               member_roles=[arg.role_name])
