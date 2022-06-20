from os import listdir
from os.path import isfile, join


def get_file_list(folder_path):
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    return files

def get_all_image_files(folder_path, image_extenstion_list=['jpg', 'png']):
    all_files = get_file_list(folder_path=folder_path)
    img_file_list = [i for i in all_files if i.split('.')[-1] in image_extenstion_list]
    return img_file_list