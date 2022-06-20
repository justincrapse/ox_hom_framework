from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxinvertNode(OXNode):
    node_type = 'mtlxinvert'
    parm_lookup_dict = {'signature': 'signature', 'inside': 'in', 'amount': 'amount', 'in_color3r': 'in_color3r', 'in_color3g': 'in_color3g', 'in_color3b': 'in_color3b', 'amount_color3r': 'amount_color3r', 'amount_color3g': 'amount_color3g', 'amount_color3b': 'amount_color3b', 'in_color3far': 'in_color3FAr', 'in_color3fag': 'in_color3FAg', 'in_color3fab': 'in_color3FAb', 'in_color4r': 'in_color4r', 'in_color4g': 'in_color4g', 'in_color4b': 'in_color4b', 'in_color4a': 'in_color4a', 'amount_color4r': 'amount_color4r', 'amount_color4g': 'amount_color4g', 'amount_color4b': 'amount_color4b', 'amount_color4a': 'amount_color4a', 'in_color4far': 'in_color4FAr', 'in_color4fag': 'in_color4FAg', 'in_color4fab': 'in_color4FAb', 'in_color4faa': 'in_color4FAa', 'in_vector2x': 'in_vector2x', 'in_vector2y': 'in_vector2y', 'amount_vector2x': 'amount_vector2x', 'amount_vector2y': 'amount_vector2y', 'in_vector2fax': 'in_vector2FAx', 'in_vector2fay': 'in_vector2FAy', 'in_vector3x': 'in_vector3x', 'in_vector3y': 'in_vector3y', 'in_vector3z': 'in_vector3z', 'amount_vector3x': 'amount_vector3x', 'amount_vector3y': 'amount_vector3y', 'amount_vector3z': 'amount_vector3z', 'in_vector3fax': 'in_vector3FAx', 'in_vector3fay': 'in_vector3FAy', 'in_vector3faz': 'in_vector3FAz', 'in_vector4x': 'in_vector4x', 'in_vector4y': 'in_vector4y', 'in_vector4z': 'in_vector4z', 'in_vector4w': 'in_vector4w', 'amount_vector4x': 'amount_vector4x', 'amount_vector4y': 'amount_vector4y', 'amount_vector4z': 'amount_vector4z', 'amount_vector4w': 'amount_vector4w', 'in_vector4fax': 'in_vector4FAx', 'in_vector4fay': 'in_vector4FAy', 'in_vector4faz': 'in_vector4FAz', 'in_vector4faw': 'in_vector4FAw'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_inside = Parameter(parm=self.node.parm('in'))
        self.parm_amount = Parameter(parm=self.node.parm('amount'))
        self.parm_in_color3r = Parameter(parm=self.node.parm('in_color3r'))
        self.parm_in_color3g = Parameter(parm=self.node.parm('in_color3g'))
        self.parm_in_color3b = Parameter(parm=self.node.parm('in_color3b'))
        self.parm_amount_color3r = Parameter(parm=self.node.parm('amount_color3r'))
        self.parm_amount_color3g = Parameter(parm=self.node.parm('amount_color3g'))
        self.parm_amount_color3b = Parameter(parm=self.node.parm('amount_color3b'))
        self.parm_in_color3far = Parameter(parm=self.node.parm('in_color3FAr'))
        self.parm_in_color3fag = Parameter(parm=self.node.parm('in_color3FAg'))
        self.parm_in_color3fab = Parameter(parm=self.node.parm('in_color3FAb'))
        self.parm_in_color4r = Parameter(parm=self.node.parm('in_color4r'))
        self.parm_in_color4g = Parameter(parm=self.node.parm('in_color4g'))
        self.parm_in_color4b = Parameter(parm=self.node.parm('in_color4b'))
        self.parm_in_color4a = Parameter(parm=self.node.parm('in_color4a'))
        self.parm_amount_color4r = Parameter(parm=self.node.parm('amount_color4r'))
        self.parm_amount_color4g = Parameter(parm=self.node.parm('amount_color4g'))
        self.parm_amount_color4b = Parameter(parm=self.node.parm('amount_color4b'))
        self.parm_amount_color4a = Parameter(parm=self.node.parm('amount_color4a'))
        self.parm_in_color4far = Parameter(parm=self.node.parm('in_color4FAr'))
        self.parm_in_color4fag = Parameter(parm=self.node.parm('in_color4FAg'))
        self.parm_in_color4fab = Parameter(parm=self.node.parm('in_color4FAb'))
        self.parm_in_color4faa = Parameter(parm=self.node.parm('in_color4FAa'))
        self.parm_in_vector2x = Parameter(parm=self.node.parm('in_vector2x'))
        self.parm_in_vector2y = Parameter(parm=self.node.parm('in_vector2y'))
        self.parm_amount_vector2x = Parameter(parm=self.node.parm('amount_vector2x'))
        self.parm_amount_vector2y = Parameter(parm=self.node.parm('amount_vector2y'))
        self.parm_in_vector2fax = Parameter(parm=self.node.parm('in_vector2FAx'))
        self.parm_in_vector2fay = Parameter(parm=self.node.parm('in_vector2FAy'))
        self.parm_in_vector3x = Parameter(parm=self.node.parm('in_vector3x'))
        self.parm_in_vector3y = Parameter(parm=self.node.parm('in_vector3y'))
        self.parm_in_vector3z = Parameter(parm=self.node.parm('in_vector3z'))
        self.parm_amount_vector3x = Parameter(parm=self.node.parm('amount_vector3x'))
        self.parm_amount_vector3y = Parameter(parm=self.node.parm('amount_vector3y'))
        self.parm_amount_vector3z = Parameter(parm=self.node.parm('amount_vector3z'))
        self.parm_in_vector3fax = Parameter(parm=self.node.parm('in_vector3FAx'))
        self.parm_in_vector3fay = Parameter(parm=self.node.parm('in_vector3FAy'))
        self.parm_in_vector3faz = Parameter(parm=self.node.parm('in_vector3FAz'))
        self.parm_in_vector4x = Parameter(parm=self.node.parm('in_vector4x'))
        self.parm_in_vector4y = Parameter(parm=self.node.parm('in_vector4y'))
        self.parm_in_vector4z = Parameter(parm=self.node.parm('in_vector4z'))
        self.parm_in_vector4w = Parameter(parm=self.node.parm('in_vector4w'))
        self.parm_amount_vector4x = Parameter(parm=self.node.parm('amount_vector4x'))
        self.parm_amount_vector4y = Parameter(parm=self.node.parm('amount_vector4y'))
        self.parm_amount_vector4z = Parameter(parm=self.node.parm('amount_vector4z'))
        self.parm_amount_vector4w = Parameter(parm=self.node.parm('amount_vector4w'))
        self.parm_in_vector4fax = Parameter(parm=self.node.parm('in_vector4FAx'))
        self.parm_in_vector4fay = Parameter(parm=self.node.parm('in_vector4FAy'))
        self.parm_in_vector4faz = Parameter(parm=self.node.parm('in_vector4FAz'))
        self.parm_in_vector4faw = Parameter(parm=self.node.parm('in_vector4FAw'))

        
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
        self.menu_float = 'default'



