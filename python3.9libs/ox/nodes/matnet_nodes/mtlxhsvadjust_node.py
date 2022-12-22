from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxhsvadjustNode(OXNode):
    node_type = 'mtlxhsvadjust'
    parm_lookup_dict = {'signature': 'signature', 'inr': 'inr', 'ing': 'ing', 'inb': 'inb', 'amountx': 'amountx', 'amounty': 'amounty', 'amountz': 'amountz', 'in_color4r': 'in_color4r', 'in_color4g': 'in_color4g', 'in_color4b': 'in_color4b', 'in_color4a': 'in_color4a'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_inr = Parameter(parm=self.node.parm('inr'))
        self.parm_ing = Parameter(parm=self.node.parm('ing'))
        self.parm_inb = Parameter(parm=self.node.parm('inb'))
        self.parm_amountx = Parameter(parm=self.node.parm('amountx'))
        self.parm_amounty = Parameter(parm=self.node.parm('amounty'))
        self.parm_amountz = Parameter(parm=self.node.parm('amountz'))
        self.parm_in_color4r = Parameter(parm=self.node.parm('in_color4r'))
        self.parm_in_color4g = Parameter(parm=self.node.parm('in_color4g'))
        self.parm_in_color4b = Parameter(parm=self.node.parm('in_color4b'))
        self.parm_in_color4a = Parameter(parm=self.node.parm('in_color4a'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))


        # input vars:
        self.input_input = 'Input'
        self.input_amount = 'Amount'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_color = ("default", 0)



