
import os, sys, requests
from pathlib import Path
import supervisely as sly


my_app = sly.AppService()
api: sly.Api = my_app.public_api

root_source_dir = str(Path(sys.argv[0]).parents[1])
sly.logger.info(f"Root source directory: {root_source_dir}")
sys.path.append(root_source_dir)

TASK_ID = int(os.environ["TASK_ID"])
TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])

logger = sly.logger

project_name = 'strawberry'
work_dir = 'strawberry_data'
strawberry_url = 'https://doc-08-04-docs.googleusercontent.com/docs/securesc/fjksl4stcffi0pt64pddibn3jn1rboko'
arch_name = 'StrawDI_Db1.zip'
images_folder = 'img'
anns_folder = 'label'
obj_class_name = 'strawberry'
obj_class = sly.ObjClass(obj_class_name, sly.Bitmap)

storage_dir = my_app.data_dir
work_dir_path = os.path.join(storage_dir, work_dir)
# sly.io.fs.mkdir(work_dir_path)
archive_path = os.path.join(work_dir_path, arch_name)

