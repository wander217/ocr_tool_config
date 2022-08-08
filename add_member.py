import argparse
from doccano_api_client import DoccanoClient
from typing import List


def add_member(url: str,
               admin_username: str,
               admin_password: str,
               project_id: int,
               username: List[str],
               roles: List[str]):
    client = DoccanoClient(url, admin_username, admin_password)
    result = client.post_members(project_id, username, roles)
    print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="creating member")
    parser.add_argument("-b", "--base_url", type=str, help="base url")
    parser.add_argument("-au", "--admin_username", type=str, help="username of admin")
    parser.add_argument("-ap", "--admin_password", type=str, help="password of admin")
    parser.add_argument("-pi", "--project_id", type=int, help="id of project")
    parser.add_argument("-mu", "--member_username", type=str, help="account of member")
    parser.add_argument("-rn", "--role_name", type=str, help="role name")
    arg = parser.parse_args()
    add_member(arg.base_url,
               arg.admin_username,
               arg.admin_password,
               arg.project_id,
               [arg.member_username],
               [arg.role_name])
