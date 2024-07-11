from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class SubnetinputNode(OXNode):
    node_type = 'subnetconnector'
    parm_lookup_dict = {'connectorkind': 'connectorkind', 'parmaccess': 'parmaccess', 'parmname': 'parmname', 'parmlabel': 'parmlabel', 'parmtype': 'parmtype', 'parmtypename': 'parmtypename', 'floatdef': 'floatdef', 'intdef': 'intdef', 'toggledef': 'toggledef', 'angledef': 'angledef', 'logfloatdef': 'logfloatdef', 'float2def1': 'float2def1', 'float2def2': 'float2def2', 'float3def1': 'float3def1', 'float3def2': 'float3def2', 'float3def3': 'float3def3', 'vectordef1': 'vectordef1', 'vectordef2': 'vectordef2', 'vectordef3': 'vectordef3', 'normaldef1': 'normaldef1', 'normaldef2': 'normaldef2', 'normaldef3': 'normaldef3', 'pointdef1': 'pointdef1', 'pointdef2': 'pointdef2', 'pointdef3': 'pointdef3', 'directiondefx': 'directiondefx', 'directiondefy': 'directiondefy', 'directiondefz': 'directiondefz', 'float4def1': 'float4def1', 'float4def2': 'float4def2', 'float4def3': 'float4def3', 'float4def4': 'float4def4', 'floatm2def1': 'floatm2def1', 'floatm2def2': 'floatm2def2', 'floatm2def3': 'floatm2def3', 'floatm2def4': 'floatm2def4', 'float9def1': 'float9def1', 'float9def2': 'float9def2', 'float9def3': 'float9def3', 'float9def4': 'float9def4', 'float9def5': 'float9def5', 'float9def6': 'float9def6', 'float9def7': 'float9def7', 'float9def8': 'float9def8', 'float9def9': 'float9def9', 'float16def1': 'float16def1', 'float16def2': 'float16def2', 'float16def3': 'float16def3', 'float16def4': 'float16def4', 'float16def5': 'float16def5', 'float16def6': 'float16def6', 'float16def7': 'float16def7', 'float16def8': 'float16def8', 'float16def9': 'float16def9', 'float16def10': 'float16def10', 'float16def11': 'float16def11', 'float16def12': 'float16def12', 'float16def13': 'float16def13', 'float16def14': 'float16def14', 'float16def15': 'float16def15', 'float16def16': 'float16def16', 'stringdef': 'stringdef', 'filedef': 'filedef', 'imagedef': 'imagedef', 'geometrydef': 'geometrydef', 'colordefr': 'colordefr', 'colordefg': 'colordefg', 'colordefb': 'colordefb', 'color4defr': 'color4defr', 'color4defg': 'color4defg', 'color4defb': 'color4defb', 'color4defa': 'color4defa', 'bsdfdef': 'bsdfdef', 'dictdef': 'dictdef', 'coshaderdef': 'coshaderdef', 'surfacedef': 'surfacedef', 'displacementdef': 'displacementdef', 'atmospheredef': 'atmospheredef', 'lightdef': 'lightdef', 'lightfilterdef': 'lightfilterdef', 'coshaderadef': 'coshaderadef', 'structdef': 'structdef', 'useasparmdefiner': 'useasparmdefiner', 'parmuniform': 'parmuniform'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_parmname = Parameter(parm=self.node.parm('parmname'))
        self.parm_parmlabel = Parameter(parm=self.node.parm('parmlabel'))
        self.parm_floatdef = Parameter(parm=self.node.parm('floatdef'))
        self.parm_intdef = Parameter(parm=self.node.parm('intdef'))
        self.parm_toggledef = Parameter(parm=self.node.parm('toggledef'))
        self.parm_angledef = Parameter(parm=self.node.parm('angledef'))
        self.parm_logfloatdef = Parameter(parm=self.node.parm('logfloatdef'))
        self.parm_float2def1 = Parameter(parm=self.node.parm('float2def1'))
        self.parm_float2def2 = Parameter(parm=self.node.parm('float2def2'))
        self.parm_float3def1 = Parameter(parm=self.node.parm('float3def1'))
        self.parm_float3def2 = Parameter(parm=self.node.parm('float3def2'))
        self.parm_float3def3 = Parameter(parm=self.node.parm('float3def3'))
        self.parm_vectordef1 = Parameter(parm=self.node.parm('vectordef1'))
        self.parm_vectordef2 = Parameter(parm=self.node.parm('vectordef2'))
        self.parm_vectordef3 = Parameter(parm=self.node.parm('vectordef3'))
        self.parm_normaldef1 = Parameter(parm=self.node.parm('normaldef1'))
        self.parm_normaldef2 = Parameter(parm=self.node.parm('normaldef2'))
        self.parm_normaldef3 = Parameter(parm=self.node.parm('normaldef3'))
        self.parm_pointdef1 = Parameter(parm=self.node.parm('pointdef1'))
        self.parm_pointdef2 = Parameter(parm=self.node.parm('pointdef2'))
        self.parm_pointdef3 = Parameter(parm=self.node.parm('pointdef3'))
        self.parm_directiondefx = Parameter(parm=self.node.parm('directiondefx'))
        self.parm_directiondefy = Parameter(parm=self.node.parm('directiondefy'))
        self.parm_directiondefz = Parameter(parm=self.node.parm('directiondefz'))
        self.parm_float4def1 = Parameter(parm=self.node.parm('float4def1'))
        self.parm_float4def2 = Parameter(parm=self.node.parm('float4def2'))
        self.parm_float4def3 = Parameter(parm=self.node.parm('float4def3'))
        self.parm_float4def4 = Parameter(parm=self.node.parm('float4def4'))
        self.parm_floatm2def1 = Parameter(parm=self.node.parm('floatm2def1'))
        self.parm_floatm2def2 = Parameter(parm=self.node.parm('floatm2def2'))
        self.parm_floatm2def3 = Parameter(parm=self.node.parm('floatm2def3'))
        self.parm_floatm2def4 = Parameter(parm=self.node.parm('floatm2def4'))
        self.parm_float9def1 = Parameter(parm=self.node.parm('float9def1'))
        self.parm_float9def2 = Parameter(parm=self.node.parm('float9def2'))
        self.parm_float9def3 = Parameter(parm=self.node.parm('float9def3'))
        self.parm_float9def4 = Parameter(parm=self.node.parm('float9def4'))
        self.parm_float9def5 = Parameter(parm=self.node.parm('float9def5'))
        self.parm_float9def6 = Parameter(parm=self.node.parm('float9def6'))
        self.parm_float9def7 = Parameter(parm=self.node.parm('float9def7'))
        self.parm_float9def8 = Parameter(parm=self.node.parm('float9def8'))
        self.parm_float9def9 = Parameter(parm=self.node.parm('float9def9'))
        self.parm_float16def1 = Parameter(parm=self.node.parm('float16def1'))
        self.parm_float16def2 = Parameter(parm=self.node.parm('float16def2'))
        self.parm_float16def3 = Parameter(parm=self.node.parm('float16def3'))
        self.parm_float16def4 = Parameter(parm=self.node.parm('float16def4'))
        self.parm_float16def5 = Parameter(parm=self.node.parm('float16def5'))
        self.parm_float16def6 = Parameter(parm=self.node.parm('float16def6'))
        self.parm_float16def7 = Parameter(parm=self.node.parm('float16def7'))
        self.parm_float16def8 = Parameter(parm=self.node.parm('float16def8'))
        self.parm_float16def9 = Parameter(parm=self.node.parm('float16def9'))
        self.parm_float16def10 = Parameter(parm=self.node.parm('float16def10'))
        self.parm_float16def11 = Parameter(parm=self.node.parm('float16def11'))
        self.parm_float16def12 = Parameter(parm=self.node.parm('float16def12'))
        self.parm_float16def13 = Parameter(parm=self.node.parm('float16def13'))
        self.parm_float16def14 = Parameter(parm=self.node.parm('float16def14'))
        self.parm_float16def15 = Parameter(parm=self.node.parm('float16def15'))
        self.parm_float16def16 = Parameter(parm=self.node.parm('float16def16'))
        self.parm_stringdef = Parameter(parm=self.node.parm('stringdef'))
        self.parm_filedef = Parameter(parm=self.node.parm('filedef'))
        self.parm_imagedef = Parameter(parm=self.node.parm('imagedef'))
        self.parm_geometrydef = Parameter(parm=self.node.parm('geometrydef'))
        self.parm_colordefr = Parameter(parm=self.node.parm('colordefr'))
        self.parm_colordefg = Parameter(parm=self.node.parm('colordefg'))
        self.parm_colordefb = Parameter(parm=self.node.parm('colordefb'))
        self.parm_color4defr = Parameter(parm=self.node.parm('color4defr'))
        self.parm_color4defg = Parameter(parm=self.node.parm('color4defg'))
        self.parm_color4defb = Parameter(parm=self.node.parm('color4defb'))
        self.parm_color4defa = Parameter(parm=self.node.parm('color4defa'))
        self.parm_bsdfdef = Parameter(parm=self.node.parm('bsdfdef'))
        self.parm_dictdef = Parameter(parm=self.node.parm('dictdef'))
        self.parm_coshaderdef = Parameter(parm=self.node.parm('coshaderdef'))
        self.parm_surfacedef = Parameter(parm=self.node.parm('surfacedef'))
        self.parm_displacementdef = Parameter(parm=self.node.parm('displacementdef'))
        self.parm_atmospheredef = Parameter(parm=self.node.parm('atmospheredef'))
        self.parm_lightdef = Parameter(parm=self.node.parm('lightdef'))
        self.parm_lightfilterdef = Parameter(parm=self.node.parm('lightfilterdef'))
        self.parm_coshaderadef = Parameter(parm=self.node.parm('coshaderadef'))
        self.parm_structdef = Parameter(parm=self.node.parm('structdef'))
        self.parm_useasparmdefiner = Parameter(parm=self.node.parm('useasparmdefiner'))
        self.parm_parmuniform = Parameter(parm=self.node.parm('parmuniform'))

        
        # parm menu vars:
        self.parm_connectorkind = ConnectorkindMenu(parm=self.node.parm('connectorkind'))
        self.parm_parmaccess = ParmaccessMenu(parm=self.node.parm('parmaccess'))
        self.parm_parmtype = ParmtypeMenu(parm=self.node.parm('parmtype'))
        self.parm_parmtypename = ParmtypenameMenu(parm=self.node.parm('parmtypename'))


        # input vars:


# parm menu classes:
class ConnectorkindMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_input = ("input", 0)
        self.menu_output = ("output", 1)
        self.menu_input_and_output = ("inputoutput", 2)


class ParmaccessMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_default = ("", 0)
        self.menu_public = ("public", 1)
        self.menu_private = ("private", 2)


class ParmtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_float__float_ = ("float", 0)
        self.menu_integer__int_ = ("int", 1)
        self.menu_toggle__int_ = ("toggle", 2)
        self.menu_angle__float_ = ("angle", 3)
        self.menu_logarithmic__float_ = ("logfloat", 4)
        self.menu_floats__vector2__2 = ("float2", 5)
        self.menu_floats__vector__3 = ("float3", 6)
        self.menu_vector__vector_ = ("vector", 7)
        self.menu_normal__normal_ = ("normal", 8)
        self.menu_point__point_ = ("point", 9)
        self.menu_direction__vector_ = ("direction", 10)
        self.menu_floats__vector4__4 = ("float4", 11)
        self.menu_floats__matrix2__4 = ("floatm2", 12)
        self.menu_floats__matrix3__9 = ("float9", 13)
        self.menu_floats__matrix__16 = ("float16", 14)
        self.menu_string__string_ = ("string", 15)
        self.menu_file__string_ = ("file", 16)
        self.menu_image__string_ = ("image", 17)
        self.menu_geometry__string_ = ("geometry", 18)
        self.menu_color__color_ = ("color", 19)
        self.menu_color_with_alpha__vector4_ = ("coloralpha", 20)
        self.menu_bsdf__f_ = ("bsdf", 21)
        self.menu_dictionary__dict_ = ("dict", 22)
        self.menu_co_shader__shader_ = ("coshader", 23)
        self.menu_surface__shader_ = ("surface", 24)
        self.menu_displacement__shader_ = ("displacement", 25)
        self.menu_volume__shader_ = ("atmosphere", 26)
        self.menu_light__shader_ = ("light", 27)
        self.menu_light_filter__shader_ = ("lightfilter", 28)
        self.menu_float_array__float___ = ("floata", 29)
        self.menu_integer_array__int___ = ("inta", 30)
        self.menu_float_array__vector2____2 = ("vector2a", 31)
        self.menu_vector_array__vector___ = ("vectora", 32)
        self.menu_point_array__point___ = ("pointa", 33)
        self.menu_normal_array__normal___ = ("normala", 34)
        self.menu_color_array__color___ = ("colora", 35)
        self.menu_float_array__vector4____4 = ("float4a", 36)
        self.menu_float_array__matrix2____4 = ("floatm2a", 37)
        self.menu_float_array__matrix3____9 = ("float9a", 38)
        self.menu_float_array__matrix4____16 = ("float16a", 39)
        self.menu_string_array__string___ = ("stringa", 40)
        self.menu_dictionary_array__dict___ = ("dicta", 41)
        self.menu_co_shader_array__shader___ = ("coshadera", 42)
        self.menu_custom__struct_ = ("struct", 43)


class ParmtypenameMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_default = ("", 0)
        self.menu_floatramp = ("FloatRamp", 1)
        self.menu_shaderlayer = ("ShaderLayer", 2)
        self.menu_colorramp = ("ColorRamp", 3)
        self.menu_shaderexports = ("ShaderExports", 4)
        self.menu_mapper = ("Mapper", 5)
        self.menu_dualrest = ("DualRest", 6)
        self.menu_pxrlayer = ("PxrLayer", 7)
        self.menu_dualrest4 = ("DualRest4", 8)
        self.menu_workitempool = ("WorkItemPool", 9)
        self.menu_workitem = ("WorkItem", 10)
        self.menu_pxrlmlayer = ("PxrLMLayer", 11)
        self.menu_pxrmanifold = ("PxrManifold", 12)
        self.menu_fuzzyset = ("FuzzySet", 13)
        self.menu_vdf = ("vdf", 14)
        self.menu_edf = ("edf", 15)



