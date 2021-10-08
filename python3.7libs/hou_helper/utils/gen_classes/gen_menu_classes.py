from hou_helper.utils import data_lover


def gen_menu_class_as_string(parm):
    parm_name = parm.name()
    parm_class_name = data_lover.get_str_as_class(parm_name)
    menu_list = parm.menuLabels()
    menu_var_list = [data_lover.get_str_as_py_var(i) for i in menu_list]
    menu_list_lines = ''.join([f'\t\tself.{item} = {index}\n' for index, item in enumerate(menu_var_list)])
    class_string = f"""class {parm_class_name}Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
{menu_list_lines}
"""

    return class_string