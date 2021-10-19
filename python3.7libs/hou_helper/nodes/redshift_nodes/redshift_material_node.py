from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu
# node class version: 0.1


class RedshiftMaterialNode(HHNode):
    node_type = 'redshift_material'
    parm_lookup_dict = {'rs_matprop_id': 'RS_matprop_ID'}

    def __init__(self, node=None, hh_parent=None, node_name=None):
        self.hh_parent = hh_parent
        if node:
            self.node = node
        else:
            self.node = self.hh_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_rs_matprop_id = Parameter(parm=self.node.parm('RS_matprop_ID'))

        
        # parm menu vars:


        # input vars:
        self.input_surface = 0
        self.input_displacement = 1
        self.input_bump_map = 2
        self.input_environment = 3
        self.input_volume = 4
        self.input_shadow = 5
        self.input_photon = 6


# parm menu classes:

