from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class LopnetNode(OXNode):
    node_type = 'lopnet'
    parm_lookup_dict = {'pinnedprims': 'pinnedprims', 'resolvercontextassetpath': 'resolvercontextassetpath', 'resolvercontextstringcount': 'resolvercontextstringcount', 'variantselectioncount': 'variantselectioncount', 'insertionpointdescriptor': 'insertionpointdescriptor', 'rendergallerysource': 'rendergallerysource'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_pinnedprims = Parameter(parm=self.node.parm('pinnedprims'))
        self.parm_resolvercontextassetpath = Parameter(parm=self.node.parm('resolvercontextassetpath'))
        self.parm_resolvercontextstringcount = Parameter(parm=self.node.parm('resolvercontextstringcount'))
        self.parm_variantselectioncount = Parameter(parm=self.node.parm('variantselectioncount'))
        self.parm_insertionpointdescriptor = Parameter(parm=self.node.parm('insertionpointdescriptor'))
        self.parm_rendergallerysource = Parameter(parm=self.node.parm('rendergallerysource'))

        
        # parm menu vars:


        # input vars:


# parm menu classes:

