import os
from os import listdir
from os.path import isfile, join, isdir
import logging
import re
import pprint

ox_logger = logging.getLogger("ox_logger")


def get_file_list(folder_path, search_subfolders=False):
    if search_subfolders:
        files = []
        for path, subdirs, items in os.walk(folder_path):
            for name in items:
                files.append(os.path.join(path, name))
    else:
        files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
        ox_logger.debug(f"Get files result: {files}")
    return files


def get_all_image_files(folder_path, image_extenstion_list=["jpg", "png", "tga", "exr", "tif", "bmp", "gif"], search_subfolders=False):
    all_files = get_file_list(folder_path=folder_path, search_subfolders=search_subfolders)
    img_file_list = [i for i in all_files if i.split(".")[-1] in image_extenstion_list]
    ox_logger.debug(f"Get image files result: {img_file_list}")
    return img_file_list


def contains_folders_only(folder_path):
    is_all_dirs = all([isdir(join(folder_path, i)) for i in listdir(folder_path)])
    ox_logger.debug(f"contains folders only result: {is_all_dirs}. dir contents: {listdir(folder_path)}")
    return is_all_dirs


def get_folders(folder_path, regex=None):
    folders = [f for f in listdir(folder_path) if isdir(join(folder_path, f))]
    if regex:
        folders = [i for i in folders if re.match(regex, i)]
    ox_logger.debug(f"Get folders result: {folders}")
    full_paths = [join(folder_path, i) for i in folders]
    return full_paths


def get_dir_contents(folder_path):
    folder_items = listdir(folder_path)
    ox_logger.debug(f"Get dir contents result: {folder_items}")
    return folder_items


if __name__ == "__main__":
    folders = get_folders(folder_path="Z:/quixel_library/Downloaded/surface/", regex=r".*cliff.*")
    pprint.pprint(folders)
