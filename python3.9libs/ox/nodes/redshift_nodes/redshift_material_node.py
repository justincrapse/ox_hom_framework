from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class RedshiftMaterialNode(OXNode):
    node_type = "redshift_material"
    parm_lookup_dict = {"rs_matprop_id": "RS_matprop_ID"}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(
                node_type_name=self.node_type, node_name=node_name
            )
        self.node_name = self.node.name()
        super().__init__(node=self.node)

        # parm vars:
        self.parm_rs_matprop_id = Parameter(parm=self.node.parm("RS_matprop_ID"))

        # parm menu vars:

        # input vars:
        self.input_surface = "Surface"
        self.input_displacement = "Displacement"
        self.input_bump_map = "Bump Map"
        self.input_environment = "Environment"
        self.input_volume = "Volume"
        self.input_shadow = "Shadow"
        self.input_photon = "Photon"


# parm menu classes:
