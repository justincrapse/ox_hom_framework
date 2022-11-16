from ox.utils import data_lover
import hou


def gen_menu_class_as_string(parm: hou.Parm):
    parm_name = parm.name()
    parm_class_name = data_lover.get_str_as_class(parm_name)
    menu_list = parm.menuLabels()
    menu_var_list = [data_lover.get_str_as_py_var(i) for i in menu_list]
    menu_item_list = [i for i in parm.menuItems()]
    menu_list_lines = "".join(
        [
            f'\t\tself.menu_{zip_tup[0]} = """{zip_tup[1]}"""\n'
            if "\n" in zip_tup[1]
            else f'\t\tself.menu_{zip_tup[0]} = ("{zip_tup[1]}", {index})\n'
            for index, zip_tup in enumerate(zip(menu_var_list, menu_item_list))
        ]
    )
    # menu_list_lines = ''.join([f"\t\tself.menu_{var} = {index}\n" for index, var in enumerate(menu_var_list)])
    class_string = f"""class {parm_class_name}Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
{menu_list_lines}
"""

    return class_string
