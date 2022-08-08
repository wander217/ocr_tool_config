import argparse
from doccano_api_client import DoccanoClient


def get_member(url: str,
               admin_username: str,
               admin_password: str):
    client = DoccanoClient(url, admin_username, admin_password)
    for item in client.get_user_list():
        print("-" * 100)
        print("- id:", item['id'])
        print("- username:", item['username'])
        print("- is_superuser:", item['is_superuser'])
        print("- is_staff:", item['is_staff'])
        print("-" * 100)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get username")
    parser.add_argument("-b", "--base_url", type=str, help="base url")
    parser.add_argument("-au", "--admin_username", type=str, help="username of admin")
    parser.add_argument("-ap", "--admin_password", type=str, help="password of admin")
    arg = parser.parse_args()
    get_member(arg.base_url,
               arg.admin_username,
               arg.admin_password)
