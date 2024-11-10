import logging
import os
from os.path import join

import hou

from ox.nodes.matnet_nodes import PrincipledshaderNode
from ox import nodes
from ox.base_objects.ox_node import OXNode
from ox.utils import file_utils, ui


ox_logger = logging.getLogger("ox_logger")


# WARNING: if a texture key is a substring of another key, you'll need to consider that in the for-loops.
# the dictionary values are not case-sensitive when matching file name, so just do lowercase.

texture_dict = {
    "BASE_COLOR": ["diffuse", "base color", "basecolor", "base_color", "albedo"],
    "METALNESS": ["metallic", "metallicity", "metalness", "metalic"],
    "SPECULAR": ["specular"],
    "SPECULAR_ROUGHNESS": ["roughness", "gloss", "glossiness"],
    "NORMAL": ["normal", "bump"],
    "DISPLACEMENT": ["displacement", "height"],
    "EMISSION": ["emissive", "luminance", "emission"],
    "EMISSION_COLOR": ["emission_color", "emission color", "emissive_color", "emissive color"],
    "OPACITY": ["opacity", "alpha"],
    "GLOSS": ["gloss", "glossiness"],
    "AO": ["ao", "ambient_occlusion", "ambientocclusion", "ambient occlusion"],
    "TRANSPARENCY": ["transparency", "transmission", "refraction", "translucency"],
    "IOR": ["ior", "intex_of_refraction"],
    "SSS": ["sss", "sub_surface_scattering", "subsurface"],
    "SSS_COLOR": ["sss_color", "sub_surface_color", "subsurface_color"]
}
ALL_SUBSTRINGS = [item for sub_list in texture_dict.values() for item in sub_list]

IMG_FILE_FORMATS = ["jpg", "png"]  # feel free to add more image files types to try out.


class MaterialHelper:
    def __init__(self) -> None:
        pass

    def import_as_principled_shader(self, folder_path: str, matnet_ox_node: OXNode) -> PrincipledshaderNode:
        hip_file_dir = os.environ["HIP"]
        folder_path = folder_path if not folder_path.endswith("/") else folder_path[:-1]
        folder_path_hip = folder_path.replace(hip_file_dir, "$HIP")
        folder_name = folder_path.split("/")[-1]

        img_files = file_utils.get_all_image_files(folder_path=folder_path, image_extenstion_list=IMG_FILE_FORMATS)
        ox_logger.info(f"Unfiltered Image Files: {img_files}")
        img_files = [img_file for img_file in img_files if any([i.lower() in img_file.lower() for i in ALL_SUBSTRINGS])]
        ox_logger.info(f"Filtered Image Files: {img_files}")

        princepled_shader_ox_node: PrincipledshaderNode
        princepled_shader_ox_node = matnet_ox_node.create_ox_node_if_not_exists(ox_node_class=PrincipledshaderNode, node_name=f"{folder_name}_principled_shader")
        princepled_shader_ox_node.parm_basecolorr = 1
        princepled_shader_ox_node.parm_basecolorg = 1
        princepled_shader_ox_node.parm_basecolorb = 1
        princepled_shader_ox_node.parm_basecolorb = 1
        princepled_shader_ox_node.parm_ior = 1
        princepled_shader_ox_node.parm_rough = 1
        for image_file in img_files:
            image_file = image_file.lower()
            image_path = f"{folder_path_hip}/{image_file}".replace("//", "/")

            if any([i.lower() in image_file for i in texture_dict["BASE_COLOR"]]):
                princepled_shader_ox_node.parm_basecolor_texture = image_path
                princepled_shader_ox_node.parm_basecolor_usetexture = 1

            elif any([i.lower() in image_file for i in texture_dict["AO"]]):
                princepled_shader_ox_node.parm_occlusion_texture = image_path
                princepled_shader_ox_node.parm_occlusion_usetexture = 1

            elif any([i.lower() in image_file for i in texture_dict["METALNESS"]]):
                princepled_shader_ox_node.parm_metallic_texture = image_path
                princepled_shader_ox_node.parm_metallic_usetexture = 1

            # elif any([i.lower() in image_file for i in texture_dict["SPECULAR"]]) and not any([i.lower() in image_file for i in texture_dict["SPECULAR_ROUGHNESS"]]):
            #     princepled_shader_ox_node.parm_specular = image_path
            #     princepled_shader_ox_node.parm_occlusion_usetexture = 1

            elif any([i.lower() in image_file for i in texture_dict["SPECULAR_ROUGHNESS"]]):
                princepled_shader_ox_node.parm_rough_texture = image_path
                princepled_shader_ox_node.parm_rough_usetexture = 1

            elif any([i.lower() in image_file for i in texture_dict["NORMAL"]]):
                princepled_shader_ox_node.parm_basebumpandnormal_enable = 1
                princepled_shader_ox_node.parm_basenormal_texture = image_path
                princepled_shader_ox_node.parm_basenormal_vectorspace.menu_object_space

            elif any([i.lower() in image_file for i in texture_dict["DISPLACEMENT"]]):
                princepled_shader_ox_node.parm_disptex_texture = image_path
                princepled_shader_ox_node.parm_disptex_enable = 1

            elif any([i.lower() in image_file for i in texture_dict["EMISSION"]]) and not any([i.lower() in image_file for i in texture_dict["EMISSION_COLOR"]]):
                princepled_shader_ox_node.parm_emitcolor_texture = image_path
                princepled_shader_ox_node.parm_emitcolor_usetexture = 1

            elif any([i.lower() in image_file for i in texture_dict["OPACITY"]]):
                princepled_shader_ox_node.parm_opaccolor_texture = image_path
                princepled_shader_ox_node.parm_opaccolor_usetexture = 1

            elif any([i.lower() in image_file for i in texture_dict["TRANSPARENCY"]]):
                princepled_shader_ox_node.parm_transparency_texture = image_path
                princepled_shader_ox_node.parm_transparency_usetexture = 1

            elif any([i.lower() in image_file for i in texture_dict["IOR"]]):
                princepled_shader_ox_node.parm_ior_texture = image_path
                princepled_shader_ox_node.parm_ior_usetexture = 1
        return princepled_shader_ox_node
