# given an u.e. folder, parse the contents and return vex code for "unreal_instance" attribute assignment
from os import listdir
from os.path import isfile, join

def create_unreal_instance_vex_code(file_path):
    asset_files = [file for file in listdir(file_path) if isfile(join(file_path, file))]
    



if __name__ == "__main__":
    file_path = r"J:\UE_PROJECTS\SANDBOXES\sandbox\Content\EuropeanBeech\Foliage\PivotPainter"
