from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class TriangulateDNode(OXNode):
    node_type = 'triangulate2d::3.0'
    parm_lookup_dict = {'points': 'points', 'planepossrc': 'planepossrc', 'originx': 'originx', 'originy': 'originy', 'originz': 'originz', 'dist': 'dist', 'dirx': 'dirx', 'diry': 'diry', 'dirz': 'dirz', 'pos2attrib': 'pos2attrib', 'options': 'options', 'useconstredges': 'useconstredges', 'constredges': 'constredges', 'useconstrpolys': 'useconstrpolys', 'constrpolys': 'constrpolys', 'ignorepolybridges': 'ignorepolybridges', 'usesilhouettepolys': 'usesilhouettepolys', 'silhouettepolys': 'silhouettepolys', 'allowconstrsplit': 'allowconstrsplit', 'useexactconstruction': 'useexactconstruction', 'ignorenonconstrpts': 'ignorenonconstrpts', 'outsideremoval': 'outsideremoval', 'removefromconvexhull': 'removefromconvexhull', 'removefromconstrpolys': 'removefromconstrpolys', 'removeoutsidesilhouette': 'removeoutsidesilhouette', 'refinement': 'refinement', 'refine': 'refine', 'allowrefineonstrsplit': 'allowrefineonstrsplit', 'encroachangle': 'encroachangle', 'minangle': 'minangle', 'trianglesize': 'trianglesize', 'maxarea': 'maxarea', 'targetedgelength': 'targetedgelength', 'minedgelength': 'minedgelength', 'maxnewpts': 'maxnewpts', 'lloydsteps': 'lloydsteps', 'allowmovinginteriorpts': 'allowmovinginteriorpts', 'outputgeo': 'outputgeo', 'restorepos': 'restorepos', 'keepprims': 'keepprims', 'updatenmls': 'updatenmls', 'removeunusedpoints': 'removeunusedpoints', 'removeduplicatepoints': 'removeduplicatepoints', 'outputgrps': 'outputgrps', 'usecontrsplitptgrp': 'usecontrsplitptgrp', 'constrsplitptgrp': 'constrsplitptgrp', 'useconstrdedges': 'useconstrdedges', 'constrdedges': 'constrdedges', 'randseed': 'randseed'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_points = Parameter(parm=self.node.parm('points'))
        self.parm_originx = Parameter(parm=self.node.parm('originx'))
        self.parm_originy = Parameter(parm=self.node.parm('originy'))
        self.parm_originz = Parameter(parm=self.node.parm('originz'))
        self.parm_dist = Parameter(parm=self.node.parm('dist'))
        self.parm_dirx = Parameter(parm=self.node.parm('dirx'))
        self.parm_diry = Parameter(parm=self.node.parm('diry'))
        self.parm_dirz = Parameter(parm=self.node.parm('dirz'))
        self.parm_pos2attrib = Parameter(parm=self.node.parm('pos2attrib'))
        self.parm_options = Parameter(parm=self.node.parm('options'))
        self.parm_useconstredges = Parameter(parm=self.node.parm('useconstredges'))
        self.parm_constredges = Parameter(parm=self.node.parm('constredges'))
        self.parm_useconstrpolys = Parameter(parm=self.node.parm('useconstrpolys'))
        self.parm_constrpolys = Parameter(parm=self.node.parm('constrpolys'))
        self.parm_ignorepolybridges = Parameter(parm=self.node.parm('ignorepolybridges'))
        self.parm_usesilhouettepolys = Parameter(parm=self.node.parm('usesilhouettepolys'))
        self.parm_silhouettepolys = Parameter(parm=self.node.parm('silhouettepolys'))
        self.parm_allowconstrsplit = Parameter(parm=self.node.parm('allowconstrsplit'))
        self.parm_useexactconstruction = Parameter(parm=self.node.parm('useexactconstruction'))
        self.parm_ignorenonconstrpts = Parameter(parm=self.node.parm('ignorenonconstrpts'))
        self.parm_outsideremoval = Parameter(parm=self.node.parm('outsideremoval'))
        self.parm_removefromconvexhull = Parameter(parm=self.node.parm('removefromconvexhull'))
        self.parm_removefromconstrpolys = Parameter(parm=self.node.parm('removefromconstrpolys'))
        self.parm_removeoutsidesilhouette = Parameter(parm=self.node.parm('removeoutsidesilhouette'))
        self.parm_refinement = Parameter(parm=self.node.parm('refinement'))
        self.parm_refine = Parameter(parm=self.node.parm('refine'))
        self.parm_allowrefineonstrsplit = Parameter(parm=self.node.parm('allowrefineonstrsplit'))
        self.parm_encroachangle = Parameter(parm=self.node.parm('encroachangle'))
        self.parm_minangle = Parameter(parm=self.node.parm('minangle'))
        self.parm_maxarea = Parameter(parm=self.node.parm('maxarea'))
        self.parm_targetedgelength = Parameter(parm=self.node.parm('targetedgelength'))
        self.parm_minedgelength = Parameter(parm=self.node.parm('minedgelength'))
        self.parm_maxnewpts = Parameter(parm=self.node.parm('maxnewpts'))
        self.parm_lloydsteps = Parameter(parm=self.node.parm('lloydsteps'))
        self.parm_allowmovinginteriorpts = Parameter(parm=self.node.parm('allowmovinginteriorpts'))
        self.parm_outputgeo = Parameter(parm=self.node.parm('outputgeo'))
        self.parm_restorepos = Parameter(parm=self.node.parm('restorepos'))
        self.parm_keepprims = Parameter(parm=self.node.parm('keepprims'))
        self.parm_updatenmls = Parameter(parm=self.node.parm('updatenmls'))
        self.parm_removeunusedpoints = Parameter(parm=self.node.parm('removeunusedpoints'))
        self.parm_removeduplicatepoints = Parameter(parm=self.node.parm('removeduplicatepoints'))
        self.parm_outputgrps = Parameter(parm=self.node.parm('outputgrps'))
        self.parm_usecontrsplitptgrp = Parameter(parm=self.node.parm('usecontrsplitptgrp'))
        self.parm_constrsplitptgrp = Parameter(parm=self.node.parm('constrsplitptgrp'))
        self.parm_useconstrdedges = Parameter(parm=self.node.parm('useconstrdedges'))
        self.parm_constrdedges = Parameter(parm=self.node.parm('constrdedges'))
        self.parm_randseed = Parameter(parm=self.node.parm('randseed'))

        
        # parm menu vars:
        self.parm_planepossrc = PlanepossrcMenu(parm=self.node.parm('planepossrc'))
        self.parm_trianglesize = TrianglesizeMenu(parm=self.node.parm('trianglesize'))


        # input vars:
        self.input_input_1 = 'Input 1'


# parm menu classes:
class PlanepossrcMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_fit_plane = ("fitplane", 0)
        self.menu_select_projection_plane = ("setprojplane", 1)
        self.menu_use_attribute = ("useattrib", 2)


class TrianglesizeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_unrestricted = ("unrestricted", 0)
        self.menu_cap_maximum_area = ("capmaxarea", 1)
        self.menu_set_target_edge_length = ("settargetedgelength", 2)



