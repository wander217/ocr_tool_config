import argparse
from doccano_api_client import DoccanoClient
from admin_config import ADMIN_CONFIG


def get_member(host_name: str,
               admin_username: str,
               admin_password: str):
    client = DoccanoClient(host_name, admin_username, admin_password)
    for item in client.get_user_list():
        print("-" * 100)
        print("- id:", item['id'])
        print("- username:", item['username'])
        print("- is_superuser:", item['is_superuser'])
        print("- is_staff:", item['is_staff'])
        print("-" * 100)


if __name__ == "__main__":
    get_member(**ADMIN_CONFIG)
