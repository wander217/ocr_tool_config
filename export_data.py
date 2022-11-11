import argparse
import json
import time
from io import BytesIO
from zipfile import ZipFile
from doccano_api_client import DoccanoClient
from admin_config import ADMIN_CONFIG


def get_result(host_name: str,
               admin_username: str,
               admin_password: str,
               project_id: int,
               save_path:str):
    client = DoccanoClient(host_name, admin_username, admin_password)
    result = client.post(f'v1/projects/{project_id}/download',
                         json={'exportApproved': False, 'format': 'JSONL'})
    task_id = result['task_id']
    while True:
        result = client.get(f'v1/tasks/status/{task_id}')
        if result['ready']:
            break
        time.sleep(1)
    result = client.get_file(f'v1/projects/{project_id}/download?taskId={task_id}')
    file_like_object = BytesIO(result.content)
    zipfile_obj = ZipFile(file_like_object)
    data = zipfile_obj.open(zipfile_obj.namelist()[0]).read().splitlines()
    data = [json.loads(line) for line in data]
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="creating project")
    parser.add_argument("-pi", "--project_id", type=int, help="id of project")
    parser.add_argument("-sp", "--save_path", type=str, help="path of save folder")
    arg = parser.parse_args()
    get_result(**ADMIN_CONFIG, project_id=arg.project_id, save_path=arg.save_path)
