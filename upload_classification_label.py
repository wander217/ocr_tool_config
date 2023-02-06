import argparse
import os
from doccano_api_client import DoccanoClient
from admin_config import ADMIN_CONFIG
from tqdm import tqdm
import random

def add_image(host_name: str,
              admin_username: str,
              admin_password: str,
              project_id: int,
              label_path: str):
    client = DoccanoClient(host_name, admin_username, admin_password)
    with open(label_path, 'r', encoding='utf-8') as f:
        labels = f.readlines()
    for i, label in enumerate(labels):
        try:
            color = '#ffffff'
            while color == '#ffffff':
                color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
            print(color)
            client.post(f"/v1/projects/{project_id}/category-types", json={
                "text": label,
                "prefix_key": None,
                "suffix_key": i,
                "background_color": color,
                "text_color": '#ffffff'
            })
            print("Upload complete!")
        except Exception as e:
            print(e)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="creating project")
    parser.add_argument("-pi", "--project_id", type=int, help="id of project")
    parser.add_argument("-lp", "--label_path", type=str, default="", help="path of label file")
    arg = parser.parse_args()
    add_image(**ADMIN_CONFIG,
              project_id=arg.project_id,
              label_path=arg.label_path)
