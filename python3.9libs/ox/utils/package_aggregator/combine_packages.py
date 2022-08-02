
from pathlib import Path
from os import listdir
import distutils.dir_util


def aggregate_packages(package_path_list, out_path, out_folder):
    for package_path in package_path_list:
        dir_contents = listdir(package_path)
        distutils.dir_util.copy_tree(str(package_path), str(out_path))
        print(f"{package_path}: dir_contents: {dir_contents}")


if __name__ == "__main__":
    p_path = Path("D:\houdini_plugins")
    out_path = p_path.joinpath('aggregates')
    mtlx_path = p_path.joinpath("ox_mtlx_package")
    redshift_path = p_path.joinpath("ox_redshift_package")
    utils_path = p_path.joinpath("ox_utils_package")

    package_path_list = [mtlx_path, redshift_path, utils_path]
    aggregate_packages(package_path_list=package_path_list, out_path=out_path, out_folder='texture_packages')
