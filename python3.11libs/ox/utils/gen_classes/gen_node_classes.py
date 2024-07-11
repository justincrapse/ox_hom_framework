"""
keep in mind that "node_type" is used instead of "type" as that is a built-in we don't want to use anywhere in our python code.
"""

from ox.utils import data_lover
from ox.utils.gen_classes import gen_menu_classes
from ox import set_log_level

import pathlib
import logging
import hou

ox_logger = logging.getLogger("ox_logger")
current_logging_level = ox_logger.level

current_path = pathlib.Path(__file__).parent.resolve()
nodes_path = current_path.parent.parent.joinpath("nodes")


def get_parm_menu_labels(parm: hou.Parm):
    ox_logger.debug(f"getting menu labels for: {parm}")
    parm_template = parm.parmTemplate()
    if hasattr(parm_template, "menuType"):
        menu_type = parm_template.menuType()
        print(f"menu type: {menu_type}")
        if not menu_type.name() == "Normal":
            return
    else:
        return
    try:
        print("weeeee")
        return parm.menuLabels()
    except Exception as e:
        ox_logger.debug(e)


def generate_node_class(node, sub_dir):
    node_name = node.name()
    node_type = node.type().name()

    # parms:
    parms_list = [i.name() for i in node.parms()]
    ox_logger.debug(f"parms names list: {parms_list}")
    parm_vars_list = [data_lover.get_str_as_py_var(i) for i in parms_list]
    parm_no_menu_list = [i for i in parms_list if not get_parm_menu_labels(node.parm(i))]
    parm_vars_no_menu_list = [data_lover.get_str_as_py_var(i) for i in parm_no_menu_list]
    parm_lookup_dict = dict(zip(parm_vars_list, parms_list))
    parm_var_lines_list = "".join([f"\t\tself.parm_{i} = Parameter(parm=self.node.parm('{j}'))\n" for i, j in zip(parm_vars_no_menu_list, parm_no_menu_list)])

    # menu parm lines:
    menu_list = [i for i in parms_list if get_parm_menu_labels(node.parm(i))]
    menu_vars_list = [data_lover.get_str_as_py_var(i) for i in menu_list]
    menu_var_lines_list = "".join([f"\t\tself.parm_{i} = {data_lover.get_str_as_class(i)}Menu(parm=self.node.parm('{j}'))\n" for i, j in zip(menu_vars_list, menu_list)])
    menu_class_lines_list = "".join([f"{gen_menu_classes.gen_menu_class_as_string(parm=node.parm(i))}\n" for i in menu_list])

    # inputs:
    input_list = node.inputLabels()
    input_vars_list = [data_lover.get_str_as_py_var(i) for i in input_list]
    input_lines_list = "".join([f"\t\tself.input_{label_var} = '{label}'\n" for label_var, label in zip(input_vars_list, input_list)])

    # for class string:
    class_name = data_lover.get_str_as_class(node_name=node_name, del_digit=True) + "Node"
    file_name = data_lover.get_str_as_py_var(string_in=node_name, del_digit=True).lower()
    file_name_node = f"{file_name}_node"
    file_name_ext = f"{file_name_node}.py"
    full_file_path = nodes_path.joinpath(sub_dir, file_name_ext)

    # folders
    parm_template_group = node.parmTemplateGroup()

    class_string = f"""from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class {class_name}(OXNode):
    node_type = '{node_type}'
    parm_lookup_dict = {parm_lookup_dict}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
{parm_var_lines_list}
        
        # parm menu vars:
{menu_var_lines_list}

        # input vars:
{input_lines_list}

# parm menu classes:
{menu_class_lines_list}
""".replace(
        "\t", "    "
    )
    with open(full_file_path, "w") as file:
        set_log_level(20)
        ox_logger.info(f"writing file: {full_file_path}")
        set_log_level(current_logging_level)
        file.write(class_string)

    import_line = f"from .{file_name_node} import {class_name}"
    init_file_path = full_file_path.parent.joinpath("__init__.py")
    with open(init_file_path, "r+") as file:
        for line in file:
            if import_line in line:
                break
        else:  # not found, we are at the eof
            ox_logger.debug(f"registering node in file: {init_file_path}")
            file.write(f"\n{import_line}")  # append missing data
