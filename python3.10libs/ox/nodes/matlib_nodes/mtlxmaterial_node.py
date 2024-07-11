from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxmaterialNode(OXNode):
    node_type = 'subnet'
    parm_lookup_dict = {'folder1': 'folder1', 'inherit_ctrl': 'inherit_ctrl', 'shader_referencetype': 'shader_referencetype', 'shader_baseprimpath': 'shader_baseprimpath', 'tabmenumask': 'tabmenumask', 'shader_rendercontextname': 'shader_rendercontextname', 'shader_forcechildren': 'shader_forcechildren'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_folder1 = Parameter(parm=self.node.parm('folder1'))
        self.parm_shader_baseprimpath = Parameter(parm=self.node.parm('shader_baseprimpath'))
        self.parm_tabmenumask = Parameter(parm=self.node.parm('tabmenumask'))
        self.parm_shader_rendercontextname = Parameter(parm=self.node.parm('shader_rendercontextname'))
        self.parm_shader_forcechildren = Parameter(parm=self.node.parm('shader_forcechildren'))

        
        # parm menu vars:
        self.parm_inherit_ctrl = InheritCtrlMenu(parm=self.node.parm('inherit_ctrl'))
        self.parm_shader_referencetype = ShaderReferencetypeMenu(parm=self.node.parm('shader_referencetype'))


        # input vars:
        self.input_next_input__all_types_allowed_ = 'Next Input (all types allowed)'


# parm menu classes:
class InheritCtrlMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_never = ("0", 0)
        self.menu_always = ("1", 1)
        self.menu_material_flag = ("2", 2)


class ShaderReferencetypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("none", 0)
        self.menu_reference = ("reference", 1)
        self.menu_inherit = ("inherit", 2)
        self.menu_specialize = ("specialize", 3)
        self.menu_represent = ("represent", 4)



