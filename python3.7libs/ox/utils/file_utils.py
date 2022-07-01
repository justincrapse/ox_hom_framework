from os import listdir
from os.path import isfile, join, isdir


def get_file_list(folder_path):
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    return files

def get_all_image_files(folder_path, image_extenstion_list=['jpg', 'png']):
    all_files = get_file_list(folder_path=folder_path)
    img_file_list = [i for i in all_files if i.split('.')[-1] in image_extenstion_list]
    return img_file_list

def contains_folders_only(folder_path):
    is_all_dirs = all([isdir(join(folder_path, i)) for i in listdir(folder_path)])
    return is_all_dirs

def get_folders(folder_path):
    files = [f for f in listdir(folder_path) if isdir(join(folder_path, f))]
    return files

def get_dir_contents(folder_path):
    return listdir(folder_path)