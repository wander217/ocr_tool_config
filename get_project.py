from doccano_api_client import DoccanoClient
from admin_config import ADMIN_CONFIG


def get_project(host_name: str,
                admin_username: str,
                admin_password: str):
    client = DoccanoClient(host_name, admin_username, admin_password)
    projects = client.get_project_list()['results']
    for item in projects:
        print("-" * 100)
        print("- id:", item['id'])
        print("- name:", item['name'])
        print("- description:", item['description'])
        print("- project_type:", item['project_type'])
        print("-" * 100)


if __name__ == "__main__":
    get_project(**ADMIN_CONFIG)
