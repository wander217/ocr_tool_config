import argparse
import os
from doccano_api_client import DoccanoClient
from admin_config import ADMIN_CONFIG


def add_image(host_name: str,
              admin_username: str,
              admin_password: str,
              project_id: int,
              root: str):
    client = DoccanoClient(host_name, admin_username, admin_password)
    upload_ids = []
    for text_file in os.listdir(root):
        try:
            txt = open(os.path.join(root, text_file), 'rb')
            fp_resp = client.post("v1/fp/process/", files={"filepond": txt}, as_json=False)
            fp_resp.raise_for_status()
            upload_ids.append(fp_resp.text)
        except Exception as e:
            # revert previous uploads if we have a problem
            for upload_id in upload_ids:
                client.delete(
                    "v1/fp/revert/", data=upload_id, headers={"Content-Type": "text/plain"}
                )
            raise e
    upload_data = {
        "uploadIds": upload_ids,
        "format": "TextFile",
        'task': "IntentDetectionAndSlotFilling"
    }
    try:
        client.post(f"v1/projects/{project_id}/upload", json=upload_data)
        print("Upload complete!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="creating project")
    parser.add_argument("-pi", "--project_id", type=int, help="id of project")
    parser.add_argument("-ip", "--text_root", type=str, default="", help="root of text folder")
    arg = parser.parse_args()
    add_image(**ADMIN_CONFIG,
              project_id=arg.project_id,
              root=arg.text_root)
