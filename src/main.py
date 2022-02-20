
import zipfile, os, random
import supervisely as sly
import sly_globals as g
from supervisely.io.fs import download
import numpy as np
import gdown


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


def extract_zip():
    if zipfile.is_zipfile(g.archive_path):
        with zipfile.ZipFile(g.archive_path, 'r') as archive:
            archive.extractall(g.work_dir_path)
    else:
        g.logger.warn('Archive cannot be unpacked {}'.format(g.arch_name))
        g.my_app.stop()


@g.my_app.callback("import_strawberry")
@sly.timeit
def import_strawberry(api: sly.Api, task_id, context, state, app_logger):

    gdown.download(g.strawberry_url, g.archive_path, quiet=False)
    extract_zip()

    strawberry_data_path = os.path.join(g.work_dir_path, sly.io.fs.get_file_name(g.arch_name))

    new_project = api.project.create(g.WORKSPACE_ID, g.project_name, change_name_if_conflict=True)
    api.project.update_meta(new_project.id, g.meta.to_json())

    for ds in g.datasets:
        new_dataset = api.dataset.create(new_project.id, ds, change_name_if_conflict=True)

        curr_strawberry_ds_path = os.path.join(strawberry_data_path, ds.lower())
        curr_img_path = os.path.join(curr_strawberry_ds_path, g.images_folder)
        curr_ann_path = os.path.join(curr_strawberry_ds_path, g.anns_folder)

        curr_img_cnt = g.sample_img_count[ds]
        app_logger.warn("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", curr_img_cnt)
        sample_img_path = random.sample(os.listdir(curr_img_path), curr_img_cnt)
        app_logger.warn("+++++++++++++++++++++++++++++++++++++++", len(sample_img_path))

        progress = sly.Progress('Create dataset {}'.format(ds), curr_img_cnt, app_logger)
        for img_batch in sly.batched(sample_img_path, batch_size=g.batch_size):

            img_pathes = [os.path.join(curr_img_path, name) for name in img_batch]
            ann_pathes = [os.path.join(curr_ann_path, name) for name in img_batch]

            anns = [create_ann(ann_path) for ann_path in ann_pathes]

            img_infos = api.image.upload_paths(new_dataset.id, img_batch, img_pathes)
            img_ids = [im_info.id for im_info in img_infos]
            api.annotation.upload_anns(img_ids, anns)
            progress.iters_done_report(g.batch_size)

    g.my_app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "TEAM_ID": g.TEAM_ID,
        "WORKSPACE_ID": g.WORKSPACE_ID
    })
    g.my_app.run(initial_events=[{"command": "import_strawberry"}])


if __name__ == '__main__':
    sly.main_wrapper("main", main)