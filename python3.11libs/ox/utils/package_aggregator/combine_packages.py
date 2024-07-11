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
    out_path = p_path.joinpath("aggregates")
    package_list = ["ox_mtlx_package", "ox_redshift_package", "ox_utils_package"]
    package_path_list = [p_path.joinpath(i) for i in package_list]
    aggregate_packages(
        package_path_list=package_path_list,
        out_path=out_path,
        out_folder="texture_packages",
    )
