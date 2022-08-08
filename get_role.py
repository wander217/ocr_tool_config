import argparse
from doccano_api_client import DoccanoClient


def get_role(url: str,
             admin_username: str,
             admin_password: str):
    client = DoccanoClient(url, admin_username, admin_password)
    for item in client.get_roles():
        print("-" * 100)
        print("- id:", item['id'])
        print("- name:", item['name'])
        print("-" * 100)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get role")
    parser.add_argument("-b", "--base_url", type=str, help="base url")
    parser.add_argument("-au", "--admin_username", type=str, help="username of admin")
    parser.add_argument("-ap", "--admin_password", type=str, help="password of admin")
    arg = parser.parse_args()
    get_role(arg.base_url,
             arg.admin_username,
             arg.admin_password)
