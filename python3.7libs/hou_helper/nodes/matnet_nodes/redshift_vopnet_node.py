from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu
# node class version: 0.1


class RedshiftVopnetNode(HHNode):
    node_type = 'redshift_vopnet'
    parm_lookup_dict = {'redshift_shop_parmswitcher1': 'Redshift_SHOP_parmSwitcher1', 'rs_matprop_id': 'RS_matprop_ID', 'ogl_diffr': 'ogl_diffr', 'ogl_diffg': 'ogl_diffg', 'ogl_diffb': 'ogl_diffb', 'ogl_emitr': 'ogl_emitr', 'ogl_emitg': 'ogl_emitg', 'ogl_emitb': 'ogl_emitb', 'ogl_specr': 'ogl_specr', 'ogl_specg': 'ogl_specg', 'ogl_specb': 'ogl_specb', 'ogl_rough': 'ogl_rough', 'ogl_alpha': 'ogl_alpha', 'ogl_light': 'ogl_light'}

    def __init__(self, node=None, hh_parent=None, node_name=None):
        self.hh_parent = hh_parent
        if node:
            self.node = node
        else:
            self.node = self.hh_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_redshift_shop_parmswitcher1 = Parameter(parm=self.node.parm('redshift_shop_parmswitcher1'))
        self.parm_rs_matprop_id = Parameter(parm=self.node.parm('rs_matprop_id'))
        self.parm_ogl_diffr = Parameter(parm=self.node.parm('ogl_diffr'))
        self.parm_ogl_diffg = Parameter(parm=self.node.parm('ogl_diffg'))
        self.parm_ogl_diffb = Parameter(parm=self.node.parm('ogl_diffb'))
        self.parm_ogl_emitr = Parameter(parm=self.node.parm('ogl_emitr'))
        self.parm_ogl_emitg = Parameter(parm=self.node.parm('ogl_emitg'))
        self.parm_ogl_emitb = Parameter(parm=self.node.parm('ogl_emitb'))
        self.parm_ogl_specr = Parameter(parm=self.node.parm('ogl_specr'))
        self.parm_ogl_specg = Parameter(parm=self.node.parm('ogl_specg'))
        self.parm_ogl_specb = Parameter(parm=self.node.parm('ogl_specb'))
        self.parm_ogl_rough = Parameter(parm=self.node.parm('ogl_rough'))
        self.parm_ogl_alpha = Parameter(parm=self.node.parm('ogl_alpha'))
        self.parm_ogl_light = Parameter(parm=self.node.parm('ogl_light'))

        
        # parm menu vars:


        # input vars:


# parm menu classes:

