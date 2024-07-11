from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class ParentconstraintNode(OXNode):
    node_type = 'kinefx::parentconstraint'
    parm_lookup_dict = {'updateoffset': 'updateoffset', 'clearoffset': 'clearoffset', 'blend': 'blend', 'components': 'components'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_updateoffset = Parameter(parm=self.node.parm('updateoffset'))
        self.parm_clearoffset = Parameter(parm=self.node.parm('clearoffset'))
        self.parm_blend = Parameter(parm=self.node.parm('blend'))

        
        # parm menu vars:
        self.parm_components = ComponentsMenu(parm=self.node.parm('components'))


        # input vars:
        self.input_transform = 'Transform'
        self.input_parent = 'Parent'
        self.input_parent_bind = 'Parent Bind'
        self.input_new_parent = 'New Parent'
        self.input_new_parent_bind = 'New Parent Bind'
        self.input_blend = 'Blend'
        self.input_components = 'Components'


# parm menu classes:
class ComponentsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_translate = ("t", 0)
        self.menu_rotate = ("r", 1)
        self.menu_scale = ("s", 2)



