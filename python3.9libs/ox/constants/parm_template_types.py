BUTTON = "Button"
DATA = "Data"
FLOAT = "Float"
FOLDER = "Folder"
FOLDERSET = "FolderSet"
INT = "Int"
LABEL = "Label"
MENU = "Menu"
RAMP = "Ramp"
SEPARATOR = "Separator"
STRING = "String"
TOGGLE = "Toggle"
PARM_TEMPLATE_LIST = [
    "Button",
    "Data",
    "Float",
    "Folder",
    "FolderSet",
    "Int",
    "Label",
    "Menu",
    "Ramp",
    "Separator",
    "String",
    "Toggle",
]

if __name__ == "__main__":
    """
    Shortcut for printing the code above is needed
    """
    blue = """hou.ButtonParmTemplate
    hou.DataParmTemplate
    hou.FloatParmTemplate**
    hou.FolderParmTemplate
    hou.FolderSetParmTemplate
    hou.IntParmTemplate
    hou.LabelParmTemplate
    hou.MenuParmTemplate
    hou.RampParmTemplate
    hou.SeparatorParmTemplate
    hou.StringParmTemplate
    hou.ToggleParmTemplate"""

    lines = blue.split("ParmTemplate")
    list_print = [
        line.replace("hou.", "").replace("\n", "").strip().replace("\t", "")
        for line in lines
    ]
    list_print = [i for i in list_print if i]
    for line in lines:
        type_str = line.replace("hou.", "").replace("\n", "").strip()
        print(f"{type_str.upper()} = '{type_str}'")
    print(f"PARM_TEMPLATE_LIST = {list_print}")
