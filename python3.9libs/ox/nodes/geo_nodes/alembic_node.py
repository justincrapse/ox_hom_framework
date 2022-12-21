from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class AlembicNode(OXNode):
    node_type = "alembic"
    parm_lookup_dict = {
        "reload": "reload",
        "numlayers": "numlayers",
        "filename": "fileName",
        "frame": "frame",
        "fps": "fps",
        "missingfile": "missingfile",
        "stdswitcher1": "stdswitcher1",
        "abcxform": "abcxform",
        "loadmode": "loadmode",
        "viewportlod": "viewportlod",
        "pointmode": "pointmode",
        "polysoup": "polysoup",
        "includexform": "includeXform",
        "usevisibility": "usevisibility",
        "statictimezero": "statictimezero",
        "groupnames": "groupnames",
        "subdgroup": "subdgroup",
        "rootpath": "rootPath",
        "pickrootpath": "pickrootPath",
        "objectpath": "objectPath",
        "pickobjectpath": "pickobjectPath",
        "objectexclude": "objectExclude",
        "pickobjectexclude": "pickobjectExclude",
        "objectpattern": "objectPattern",
        "animationfilter": "animationfilter",
        "polygonfilter": "polygonFilter",
        "curvefilter": "curveFilter",
        "nurbsfilter": "NURBSFilter",
        "pointsfilter": "pointsFilter",
        "subdfilter": "subdFilter",
        "loadlocator": "loadLocator",
        "boxcull": "boxcull",
        "boxsource": "boxsource",
        "boxsizex": "boxsizex",
        "boxsizey": "boxsizey",
        "boxsizez": "boxsizez",
        "boxcenterx": "boxcenterx",
        "boxcentery": "boxcentery",
        "boxcenterz": "boxcenterz",
        "sizecull": "sizecull",
        "sizecompare": "sizecompare",
        "size": "size",
        "pointattributes": "pointAttributes",
        "vertexattributes": "vertexAttributes",
        "primitiveattributes": "primitiveAttributes",
        "detailattributes": "detailAttributes",
        "facesetattributes": "facesetAttributes",
        "loaduserprops": "loadUserProps",
        "addpath": "addpath",
        "pathattrib": "pathattrib",
        "addfile": "addfile",
        "fileattrib": "fileattrib",
        "remapattributes": "remapAttributes",
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
        self.parm_reload = Parameter(parm=self.node.parm("reload"))
        self.parm_numlayers = Parameter(parm=self.node.parm("numlayers"))
        self.parm_frame = Parameter(parm=self.node.parm("frame"))
        self.parm_fps = Parameter(parm=self.node.parm("fps"))
        self.parm_stdswitcher1 = Parameter(parm=self.node.parm("stdswitcher1"))
        self.parm_includexform = Parameter(parm=self.node.parm("includeXform"))
        self.parm_usevisibility = Parameter(parm=self.node.parm("usevisibility"))
        self.parm_statictimezero = Parameter(parm=self.node.parm("statictimezero"))
        self.parm_subdgroup = Parameter(parm=self.node.parm("subdgroup"))
        self.parm_pickrootpath = Parameter(parm=self.node.parm("pickrootPath"))
        self.parm_pickobjectpath = Parameter(parm=self.node.parm("pickobjectPath"))
        self.parm_pickobjectexclude = Parameter(
            parm=self.node.parm("pickobjectExclude")
        )
        self.parm_objectpattern = Parameter(parm=self.node.parm("objectPattern"))
        self.parm_polygonfilter = Parameter(parm=self.node.parm("polygonFilter"))
        self.parm_curvefilter = Parameter(parm=self.node.parm("curveFilter"))
        self.parm_nurbsfilter = Parameter(parm=self.node.parm("NURBSFilter"))
        self.parm_pointsfilter = Parameter(parm=self.node.parm("pointsFilter"))
        self.parm_subdfilter = Parameter(parm=self.node.parm("subdFilter"))
        self.parm_loadlocator = Parameter(parm=self.node.parm("loadLocator"))
        self.parm_boxsource = Parameter(parm=self.node.parm("boxsource"))
        self.parm_boxsizex = Parameter(parm=self.node.parm("boxsizex"))
        self.parm_boxsizey = Parameter(parm=self.node.parm("boxsizey"))
        self.parm_boxsizez = Parameter(parm=self.node.parm("boxsizez"))
        self.parm_boxcenterx = Parameter(parm=self.node.parm("boxcenterx"))
        self.parm_boxcentery = Parameter(parm=self.node.parm("boxcentery"))
        self.parm_boxcenterz = Parameter(parm=self.node.parm("boxcenterz"))
        self.parm_size = Parameter(parm=self.node.parm("size"))
        self.parm_pointattributes = Parameter(parm=self.node.parm("pointAttributes"))
        self.parm_vertexattributes = Parameter(parm=self.node.parm("vertexAttributes"))
        self.parm_primitiveattributes = Parameter(
            parm=self.node.parm("primitiveAttributes")
        )
        self.parm_detailattributes = Parameter(parm=self.node.parm("detailAttributes"))
        self.parm_facesetattributes = Parameter(
            parm=self.node.parm("facesetAttributes")
        )
        self.parm_addpath = Parameter(parm=self.node.parm("addpath"))
        self.parm_pathattrib = Parameter(parm=self.node.parm("pathattrib"))
        self.parm_addfile = Parameter(parm=self.node.parm("addfile"))
        self.parm_fileattrib = Parameter(parm=self.node.parm("fileattrib"))
        self.parm_remapattributes = Parameter(parm=self.node.parm("remapAttributes"))

        # parm menu vars:
        self.parm_filename = FilenameMenu(parm=self.node.parm("fileName"))
        self.parm_missingfile = MissingfileMenu(parm=self.node.parm("missingfile"))
        self.parm_abcxform = AbcxformMenu(parm=self.node.parm("abcxform"))
        self.parm_loadmode = LoadmodeMenu(parm=self.node.parm("loadmode"))
        self.parm_viewportlod = ViewportlodMenu(parm=self.node.parm("viewportlod"))
        self.parm_pointmode = PointmodeMenu(parm=self.node.parm("pointmode"))
        self.parm_polysoup = PolysoupMenu(parm=self.node.parm("polysoup"))
        self.parm_groupnames = GroupnamesMenu(parm=self.node.parm("groupnames"))
        self.parm_rootpath = RootpathMenu(parm=self.node.parm("rootPath"))
        self.parm_objectpath = ObjectpathMenu(parm=self.node.parm("objectPath"))
        self.parm_objectexclude = ObjectexcludeMenu(
            parm=self.node.parm("objectExclude")
        )
        self.parm_animationfilter = AnimationfilterMenu(
            parm=self.node.parm("animationfilter")
        )
        self.parm_boxcull = BoxcullMenu(parm=self.node.parm("boxcull"))
        self.parm_sizecull = SizecullMenu(parm=self.node.parm("sizecull"))
        self.parm_sizecompare = SizecompareMenu(parm=self.node.parm("sizecompare"))
        self.parm_loaduserprops = LoaduserpropsMenu(
            parm=self.node.parm("loadUserProps")
        )

        # input vars:
        self.input_bounding_source = "Bounding Source"


# parm menu classes:
class FilenameMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__hip_render_whit___name__os__f4_exr = (
            "$HIP/render_white_desert_closeup/$HIPNAME.$OS.$F4.exr",
            0,
        )
        self.menu__hip_tunder_rend___name__os__f4_exr = (
            "$HIP/tunder_render_closeup/$HIPNAME.$OS.$F4.exr",
            1,
        )
        self.menu__hip_render_gras___name__os__f4_exr = (
            "$HIP/render_grassy_hills_closeup/$HIPNAME.$OS.$F4.exr",
            2,
        )
        self.menu__hip_render_gras___name__os__f4_exr = (
            "$HIP/render_grassy_hills/$HIPNAME.$OS.$F4.exr",
            3,
        )
        self.menu__hip_tunder_rend___name__os__f4_exr = (
            "$HIP/tunder_render/$HIPNAME.$OS.$F4.exr",
            4,
        )
        self.menu_e__art_old_3d_as___field_wind_2_abc = (
            "E:/ART_OLD/3D_ASSETS/00_my_trees/palm_with_wind_abc/Palm_Coconut_Field_wind_2.abc",
            5,
        )
        self.menu_e__art_old_3d_as___t_field_wind_abc = (
            "E:/ART_OLD/3D_ASSETS/00_my_trees/palm_with_wind_abc/Palm_Coconut_Field_wind.abc",
            6,
        )
        self.menu_e__renders_houdi___name__os__f4_exr = (
            "E:/RENDERS/HOUDINI/TUTORIALS/MAGIC_RENDR/$HIPNAME.$OS.$F4.exr",
            7,
        )
        self.menu_e__renders_houdi___r_magic_prev__f3 = (
            "E:/RENDERS/HOUDINI/TUTORIALS/MAGIC_RENDR/magic_prev.$F3",
            8,
        )
        self.menu_e__art_projects____y_first_hdrlight = (
            "E:/ART/PROJECTS/00_shared/hdri/my_first_hdrlight",
            9,
        )


class MissingfileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_report_error = ("error", 0)
        self.menu_no_geometry = ("empty", 1)


class AbcxformMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_shape_nodes_only = ("off", 0)
        self.menu_shape_and_transform_nodes = ("on", 1)
        self.menu_transform_nodes_only = ("xform", 2)


class LoadmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_alembic_delayed_load_primitives = ("alembic", 0)
        self.menu_unpack_alembic_delayed_load_primitives = ("unpack", 1)
        self.menu_load_houdini_geometry__deprecated_ = ("houdini", 2)
        self.menu_houdini_point_cloud = ("hpoints", 3)
        self.menu_bounding_boxes = ("hboxes", 4)


class ViewportlodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_full_geometry = ("full", 0)
        self.menu_point_cloud = ("points", 1)
        self.menu_bounding_box = ("box", 2)
        self.menu_centroid = ("centroid", 3)
        self.menu_hidden = ("hidden", 4)


class PointmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_shared_point = ("shared", 0)
        self.menu_unique_points_at_origin = ("unique", 1)
        self.menu_unique_points_at_centroid = ("centroid", 2)
        self.menu_unique_points_at_shape_origin = ("shape", 3)


class PolysoupMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_poly_soup_primitives = ("none", 0)
        self.menu_use_poly_soups_for_polygon_meshes = ("polymesh", 1)
        self.menu_use_poly_soups_wherever_possible = ("subd", 2)


class GroupnamesMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_groups = ("none", 0)
        self.menu_name_group_using_shape_node_full_path = ("shape", 1)
        self.menu_name_group_using_transform_node_full_path = ("xform", 2)
        self.menu_name_group_using_shape_node_name = ("basename", 3)
        self.menu_name_group_using_transform_node_name = ("xformbase", 4)


class RootpathMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = ("/", 0)
        self.menu__gabc = ("/gabc", 1)
        self.menu__gabc_gabc = ("/gabc/gabc", 2)


class ObjectpathMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = ("/", 0)
        self.menu__gabc = ("/gabc", 1)
        self.menu__gabc_gabc = ("/gabc/gabc", 2)


class ObjectexcludeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = ("/", 0)
        self.menu__gabc = ("/gabc", 1)
        self.menu__gabc_gabc = ("/gabc/gabc", 2)


class AnimationfilterMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_include_all_primitives = ("all", 0)
        self.menu_only_static_primitives = ("static", 1)
        self.menu_only_deforming_primitives = ("deforming", 2)
        self.menu_only_transforming_primitives = ("transforming", 3)
        self.menu_only_deforming_or_transforming_primitives = ("animating", 4)


class BoxcullMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_spatial_filtering = ("none", 0)
        self.menu_load_objects_entirely_inside_box = ("inside", 1)
        self.menu_load_objects_with_any_part_in_box = ("anyinside", 2)
        self.menu_load_object_outside_box = ("outside", 3)
        self.menu_load_objects_with_any_part_outside_box = ("anyoutside", 4)


class SizecullMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_size_filtering = ("none", 0)
        self.menu_filter_objects_by_bounding_area = ("area", 1)
        self.menu_filter_objects_by_bounding_radius = ("radius", 2)
        self.menu_filter_objects_by_bounding_volume = ("volume", 3)


class SizecompareMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_less_than = ("lessthan", 0)
        self.menu_greater_than = ("greaterthan", 1)


class LoaduserpropsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_do_not_load = ("none", 0)
        self.menu_load_values_only = ("data", 1)
        self.menu_load_values_and_metadata = ("both", 2)
