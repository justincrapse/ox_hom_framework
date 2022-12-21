from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class HeightfieldCutoutbyobjectNode(OXNode):
    node_type = "heightfield_cutoutbyobject"
    parm_lookup_dict = {
        "folder01": "folder01",
        "invert": "invert",
        "combine": "combine",
        "crop": "crop",
        "alphalayer": "alphalayer",
        "heightlayer": "heightlayer",
    }

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
        self.parm_folder01 = Parameter(parm=self.node.parm("folder01"))
        self.parm_invert = Parameter(parm=self.node.parm("invert"))
        self.parm_crop = Parameter(parm=self.node.parm("crop"))
        self.parm_alphalayer = Parameter(parm=self.node.parm("alphalayer"))
        self.parm_heightlayer = Parameter(parm=self.node.parm("heightlayer"))

        # parm menu vars:
        self.parm_combine = CombineMenu(parm=self.node.parm("combine"))

        # input vars:
        self.input_terrain_to_cutout = "Terrain to Cutout"
        self.input_geometry_to_cutout = "Geometry to Cutout"


# parm menu classes:
class CombineMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = ("replace", 0)
        self.menu_intersect = ("intersect", 1)
        self.menu_union = ("union", 2)
        self.menu_subtract = ("subtract", 3)
