from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class SubstanceMaterialNode(OXNode):
    node_type = 'labs::substance_material'
    parm_lookup_dict = {'file': 'file', 'reload': 'reload', 'size1': 'size1', 'size2': 'size2', 'cop_input': 'cop_input', 'group1': 'group1', 'fd_materialsettings': 'fd_materialsettings', 'basenormal_flipy': 'baseNormal_flipY', 'disptex_enable': 'dispTex_enable', 'disptex_scale': 'dispTex_scale', 'disptex_offset': 'dispTex_offset', 'gamma_diffuse': 'gamma_diffuse', 'gamma_roughness': 'gamma_roughness'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_file = Parameter(parm=self.node.parm('file'))
        self.parm_reload = Parameter(parm=self.node.parm('reload'))
        self.parm_size1 = Parameter(parm=self.node.parm('size1'))
        self.parm_size2 = Parameter(parm=self.node.parm('size2'))
        self.parm_cop_input = Parameter(parm=self.node.parm('cop_input'))
        self.parm_group1 = Parameter(parm=self.node.parm('group1'))
        self.parm_fd_materialsettings = Parameter(parm=self.node.parm('fd_materialsettings'))
        self.parm_basenormal_flipy = Parameter(parm=self.node.parm('baseNormal_flipY'))
        self.parm_disptex_enable = Parameter(parm=self.node.parm('dispTex_enable'))
        self.parm_disptex_scale = Parameter(parm=self.node.parm('dispTex_scale'))
        self.parm_disptex_offset = Parameter(parm=self.node.parm('dispTex_offset'))
        self.parm_gamma_diffuse = Parameter(parm=self.node.parm('gamma_diffuse'))
        self.parm_gamma_roughness = Parameter(parm=self.node.parm('gamma_roughness'))

        
        # parm menu vars:


        # input vars:
        self.input_mesh_to_apply_material_to = 'Mesh To Apply Material To'


# parm menu classes:

