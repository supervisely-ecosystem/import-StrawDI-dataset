
import zipfile, os
import supervisely as sly
import sly_globals as g
import init_ui
from functools import partial
from supervisely.io.fs import download
import numpy as np


def create_ann(ann_path):
    ann_np = sly.imaging.image.read(ann_path)[:, :, 0]
    unique_idx = list(np.unique(ann_np))
    unique_idx.remove(0)
    labels = []
    for idx in unique_idx:
        mask = ann_np==idx
        curr_bitmap = sly.Bitmap(mask)
        curr_label = sly.Label(curr_bitmap, g.obj_class)
        labels.append(curr_label)

    return sly.Annotation(img_size=(ann_np.shape[0], ann_np.shape[1]), labels=labels)


@g.my_app.callback("import_strawberry")
@sly.timeit
def import_strawberry(api: sly.Api, task_id, context, state, app_logger):

    # def update_progress(count, index, api: sly.Api, task_id, progress: sly.Progress):
    #     progress.iters_done(count)
    #
    #
    # def get_progress_cb(index, message, total, is_size=False, min_report_percent=5, upd_func=update_progress):
    #     progress = sly.Progress(message, total, is_size=is_size, min_report_percent=min_report_percent)
    #     progress_cb = partial(upd_func, index=index, api=api, task_id=TASK_ID, progress=progress)
    #     progress_cb(0)
    #     return progress_cb
    #
    # response = requests.head(strawberry_url, allow_redirects=True)
    # sizeb = int(response.headers.get('content-length', 0))
    # progress_cb = get_progress_cb(6, "Download {}".format(arch_name), sizeb, is_size=True, min_report_percent=1)
    # download(strawberry_url, archive_path, my_app.cache, progress_cb)
    # ===============================================================================================================
    # extract zip
    # if zipfile.is_zipfile(g.archive_path):
    #     with zipfile.ZipFile(g.archive_path, 'r') as archive:
    #         archive.extractall(g.work_dir_path)
    # else:
    #     g.logger.warn('Archive cannot be unpacked {}'.format(g.arch_name))
    #     g.my_app.stop()

    strawberry_data_path = os.path.join(g.work_dir_path, sly.io.fs.get_file_name(g.arch_name))

    # dataset = os.environ["modal.state.currDataset"]

    datasets = ['Val', 'Test'] # TODO for debug

    new_project = api.project.create(g.WORKSPACE_ID, g.project_name, change_name_if_conflict=True)

    obj_class_collection = sly.ObjClassCollection([g.obj_class])
    meta = sly.ProjectMeta(obj_classes=obj_class_collection)
    api.project.update_meta(new_project.id, meta.to_json())

    for ds in datasets:
        new_dataset = api.dataset.create(new_project.id, ds, change_name_if_conflict=True)

        curr_strawberry_ds_path = os.path.join(strawberry_data_path, ds.lower())
        curr_img_path = os.path.join(curr_strawberry_ds_path, g.images_folder)
        curr_ann_path = os.path.join(curr_strawberry_ds_path, g.anns_folder)

        for img_batch in sly.batched(os.listdir(curr_img_path), batch_size=10):

            img_pathes = [os.path.join(curr_img_path, name) for name in img_batch]
            ann_pathes = [os.path.join(curr_ann_path, name) for name in img_batch]

            anns = [create_ann(ann_path) for ann_path in ann_pathes]

            img_infos = api.image.upload_paths(new_dataset.id, img_batch, img_pathes)
            img_ids = [im_info.id for im_info in img_infos]
            api.annotation.upload_anns(img_ids, anns)

    g.my_app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "TEAM_ID": g.TEAM_ID,
        "WORKSPACE_ID": g.WORKSPACE_ID
    })
    g.my_app.run(initial_events=[{"command": "import_strawberry"}])


if __name__ == '__main__':
    sly.main_wrapper("main", main)