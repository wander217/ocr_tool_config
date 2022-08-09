import argparse
from doccano_api_client import DoccanoClient
from admin_config import ADMIN_CONFIG


def get_role(host_name: str,
             admin_username: str,
             admin_password: str):
    client = DoccanoClient(host_name, admin_username, admin_password)
    for item in client.get_roles():
        print("-" * 100)
        print("- id:", item['id'])
        print("- name:", item['name'])
        print("-" * 100)


if __name__ == "__main__":
    get_role(**ADMIN_CONFIG)
