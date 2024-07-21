from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class AssignmaterialNode(OXNode):
    node_type = 'assignmaterial'
    parm_lookup_dict = {'nummaterials': 'nummaterials', 'enable1': 'enable1', 'primpattern1': 'primpattern1', 'matspecmethod1': 'matspecmethod1', 'matspecpath1': 'matspecpath1', 'matspeccvex1': 'matspeccvex1', 'matspecvexpr1': 'matspecvexpr1', 'parmsovermethod1': 'parmsovermethod1', 'parmsovercvex1': 'parmsovercvex1', 'parmsovervexpr1': 'parmsovervexpr1', 'parmsoverexports1': 'parmsoverexports1', 'matparentpath1': 'matparentpath1', 'matparenttype1': 'matparenttype1', 'cvexbindingsfolder1': 'cvexbindingsfolder1', 'cvexautobind1': 'cvexautobind1', 'cvexbindings1': 'cvexbindings1', 'matbindingfolder1': 'matbindingfolder1', 'geosubset1': 'geosubset1', 'bindpurpose1': 'bindpurpose1', 'bindstrength1': 'bindstrength1', 'bindmethod1': 'bindmethod1', 'bindcollectionexpand1': 'bindcollectionexpand1', 'bindpath1': 'bindpath1', 'bindname1': 'bindname1'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_nummaterials = Parameter(parm=self.node.parm('nummaterials'))
        self.parm_enable1 = Parameter(parm=self.node.parm('enable1'))
        self.parm_primpattern1 = Parameter(parm=self.node.parm('primpattern1'))
        self.parm_matspecpath1 = Parameter(parm=self.node.parm('matspecpath1'))
        self.parm_matspeccvex1 = Parameter(parm=self.node.parm('matspeccvex1'))
        self.parm_matspecvexpr1 = Parameter(parm=self.node.parm('matspecvexpr1'))
        self.parm_parmsovercvex1 = Parameter(parm=self.node.parm('parmsovercvex1'))
        self.parm_parmsovervexpr1 = Parameter(parm=self.node.parm('parmsovervexpr1'))
        self.parm_parmsoverexports1 = Parameter(parm=self.node.parm('parmsoverexports1'))
        self.parm_matparentpath1 = Parameter(parm=self.node.parm('matparentpath1'))
        self.parm_cvexbindingsfolder1 = Parameter(parm=self.node.parm('cvexbindingsfolder1'))
        self.parm_cvexautobind1 = Parameter(parm=self.node.parm('cvexautobind1'))
        self.parm_cvexbindings1 = Parameter(parm=self.node.parm('cvexbindings1'))
        self.parm_matbindingfolder1 = Parameter(parm=self.node.parm('matbindingfolder1'))
        self.parm_geosubset1 = Parameter(parm=self.node.parm('geosubset1'))
        self.parm_bindcollectionexpand1 = Parameter(parm=self.node.parm('bindcollectionexpand1'))
        self.parm_bindpath1 = Parameter(parm=self.node.parm('bindpath1'))
        self.parm_bindname1 = Parameter(parm=self.node.parm('bindname1'))

        
        # parm menu vars:
        self.parm_matspecmethod1 = Matspecmethod1Menu(parm=self.node.parm('matspecmethod1'))
        self.parm_parmsovermethod1 = Parmsovermethod1Menu(parm=self.node.parm('parmsovermethod1'))
        self.parm_matparenttype1 = Matparenttype1Menu(parm=self.node.parm('matparenttype1'))
        self.parm_bindpurpose1 = Bindpurpose1Menu(parm=self.node.parm('bindpurpose1'))
        self.parm_bindstrength1 = Bindstrength1Menu(parm=self.node.parm('bindstrength1'))
        self.parm_bindmethod1 = Bindmethod1Menu(parm=self.node.parm('bindmethod1'))


        # input vars:
        self.input_input_stage = 'Input Stage'


# parm menu classes:
class Matspecmethod1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_explicit_path = ("path", 0)
        self.menu_cvex_script = ("cvex", 1)
        self.menu_vexpression = ("vexpr", 2)


class Parmsovermethod1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("none", 0)
        self.menu_cvex_script = ("cvex", 1)
        self.menu_vexpression = ("vexpr", 2)


class Matparenttype1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("", 0)
        self.menu_xform = ("UsdGeomXform", 1)
        self.menu_scope = ("UsdGeomScope", 2)


class Bindpurpose1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_all = ("", 0)
        self.menu_full_render = ("full", 1)
        self.menu_preview_render = ("preview", 2)


class Bindstrength1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_default = ("fallback", 0)
        self.menu_stronger_than_descendants = ("strong", 1)
        self.menu_weaker_than_descendants = ("weak", 2)


class Bindmethod1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_direct = ("direct", 0)
        self.menu_collection_based = ("collection", 1)



