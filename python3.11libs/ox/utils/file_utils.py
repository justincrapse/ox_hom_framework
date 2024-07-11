from os import listdir
from os.path import isfile, join, isdir
import logging

ox_logger = logging.getLogger("ox_logger")


def get_file_list(folder_path):
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    ox_logger.debug(f"Get files result: {files}")
    return files


def get_all_image_files(folder_path, image_extenstion_list=["jpg", "png"]):
    all_files = get_file_list(folder_path=folder_path)
    img_file_list = [i for i in all_files if i.split(".")[-1] in image_extenstion_list]
    ox_logger.debug(f"Get image files result: {img_file_list}")
    return img_file_list


def contains_folders_only(folder_path):
    is_all_dirs = all([isdir(join(folder_path, i)) for i in listdir(folder_path)])
    ox_logger.debug(
        f"contains folders only result: {is_all_dirs}. dir contents: {listdir(folder_path)}"
    )
    return is_all_dirs


def get_folders(folder_path):
    folders = [f for f in listdir(folder_path) if isdir(join(folder_path, f))]
    ox_logger.debug(f"Get folders result: {folders}")
    return folders


def get_dir_contents(folder_path):
    folder_items = listdir(folder_path)
    ox_logger.debug(f"Get dir contents result: {folder_items}")
    return folder_items
