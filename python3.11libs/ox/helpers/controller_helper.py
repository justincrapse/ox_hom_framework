"""
THIS MODULE IS SLATED FOR DELETION. DO NOT USE. 
"""
from ox import nodes
from ox.constants import parm_template_types as pt_types


class CTRLHelper:
    def __init__(
        self,
    ):
        super().__init__()
        self.parm_ctrl_node = self.obj_node.create_node_if_not_exists(ox_node_class=nodes.obj_nodes.GeoNode)  # type: nodes.obj_nodes.GeoNode
        self.folder_labels = self.parm_ctrl_node.get_folder_labels()

    def get_folder_parms(self, folder_label):
        folder_parms = self.parm_ctrl_node.get_folder_parameters(folder_label=folder_label, return_parm_labels=True)
        return folder_parms

    def get_folder_parm_labels(self, folder_label):
        parms = self.parm_ctrl_node.get_folder_parameters(folder_label=folder_label, return_parm_labels=True)
        return parms

    def add_folder(self, folder_name, as_first=False):
        self.parm_ctrl_node.add_folder(
            folder_label=folder_name,
            folder_name=folder_name.replace(" ", "_").lower(),
            as_first=as_first,
        )

    def add_to_folder(self, parm_type, folder_label, name, label, **kwargs):
        if parm_type == pt_types.FLOAT:
            self.parm_ctrl_node.create_float_parm_template(name=name, label=label, folder_label=folder_label, **kwargs)
        elif parm_type == pt_types.BUTTON:
            self.parm_ctrl_node.create_button_parm_template(name=name, label=label, folder_label=folder_label, **kwargs)
        elif parm_type == pt_types.INT:
            self.parm_ctrl_node.create_int_parm_template(name=name, label=label, folder_label=folder_label, **kwargs)
        elif parm_type == pt_types.STRING:
            self.parm_ctrl_node.create_string_parm_template(name=name, label=label, folder_label=folder_label, **kwargs)
        elif parm_type == pt_types.MENU:
            self.parm_ctrl_node.create_menu_parm_template(name=name, label=label, folder_label=folder_label, **kwargs)
        elif parm_type == pt_types.RAMP:
            self.parm_ctrl_node.create_ramp_parm_template(name=name, label=label, folder_label=folder_label, **kwargs)
        elif parm_type == pt_types.SEPARATOR:
            self.parm_ctrl_node.create_separator_parm_template(name=name, label=label, folder_label=folder_label, **kwargs)
