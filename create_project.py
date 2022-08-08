import argparse
from doccano_api_client import DoccanoClient


def create_project(url: str,
                   admin_username: str,
                   admin_password: str,
                   project_name: str,
                   description: str,
                   project_type: str,
                   resource_type: str):
    client = DoccanoClient(url, admin_username, admin_password)
    result = client.create_project(name=project_name,
                                   description=description,
                                   project_type=project_type,
                                   resourcetype=resource_type)
    print("-"*100)
    print("Project id:", result['id'])
    print("Project name:", result['name'])
    print("-" * 100)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="creating project")
    parser.add_argument("-b", "--base_url", type=str, help="base url")
    parser.add_argument("-au", "--admin_username", type=str, help="username of admin")
    parser.add_argument("-ap", "--admin_password", type=str, help="password of admin")
    parser.add_argument("-pn", "--project_name", type=str, help="name of project")
    parser.add_argument("-de", "--description", type=str, default="", help="description of project")
    parser.add_argument("-pt", "--project_type", type=str, default="ImageCaptioning", help="type of project")
    parser.add_argument("-rt", "--resource_type", type=str, default="ImageCaptioningProject", help="type of resource")
    arg = parser.parse_args()
    create_project(arg.base_url,
                   arg.admin_username,
                   arg.admin_password,
                   arg.project_name,
                   arg.description,
                   arg.project_type,
                   arg.resource_type)
