from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxpositionNode(OXNode):
    node_type = 'mtlxposition'
    parm_lookup_dict = {'space': 'space'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:

        
        # parm menu vars:
        self.parm_space = SpaceMenu(parm=self.node.parm('space'))


        # input vars:
        self.input_space = 'Space'


# parm menu classes:
class SpaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_model = ("model", 0)
        self.menu_object = ("object", 1)
        self.menu_world = ("world", 2)



