
import os, sys
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

train_ds = os.environ["modal.state.train"]
val_ds = os.environ["modal.state.val"]
test_ds = os.environ["modal.state.test"]

datasets = []

for ds in [train_ds, val_ds, test_ds]:
    if len(ds) != 2:
        datasets.append(ds[1:-1].replace('\'', ''))

if len(datasets) == 0:
    logger.warn('You have not selected a dataset to import')
    my_app.stop()

train_percent = int(os.environ["modal.state.samplePercentTrain"])
val_percent = int(os.environ["modal.state.samplePercentVal"])
test_percent = int(os.environ["modal.state.samplePercentTest"])

sample_img_count = {'Train': 28 * train_percent, 'Val': val_percent, 'Test': 2 * test_percent}


project_name = 'strawberry'
work_dir = 'strawberry_data'
strawberry_url = 'https://docs.google.com/uc?id=1elFB-q9dgPbfnleA7qIrTb96Qsli8PZl'
arch_name = 'StrawDI_Db1.zip'
images_folder = 'img'
anns_folder = 'label'
obj_class_name = 'strawberry'
batch_size = 30
obj_class = sly.ObjClass(obj_class_name, sly.Bitmap)
obj_class_collection = sly.ObjClassCollection([obj_class])
meta = sly.ProjectMeta(obj_classes=obj_class_collection)

storage_dir = my_app.data_dir
work_dir_path = os.path.join(storage_dir, work_dir)
sly.io.fs.mkdir(work_dir_path)
archive_path = os.path.join(work_dir_path, arch_name)
