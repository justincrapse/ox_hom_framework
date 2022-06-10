import hou

from ox.base_objects.ox_node import OXNode
from ox import nodes
from ox.constants import node_names


class COPHelper:
    def __init__(self, ox_cop_node, sop_node_name=node_names.SOP_IMPORT):
        self.obj_node = OXNode(node=hou.node('/obj'))
        self.ox_cop_node = ox_cop_node  # type:nodes.obj_nodes.CopNetNode
        self.ox_sop_node = self.ox_cop_node.create_node_if_not_exist(ox_node_class=nodes.cop_nodes.SopimportNode, node_name=sop_node_name)

    def set_sop_import_node(self, sop_path):
        self.ox_sop_node.parm_soppath = sop_path
        self.ox_sop_node.parm_setres.click()
        self.ox_sop_node.parm_setplanes.click()

    def get_planes(self):
        planes = self.ox_sop_node.get_planes()
        return planes

    def create_output_for_each_plane(self, rename_layer_name='C'):
        """ This is with Redshift in mind """
        planes = self.get_planes()
        for plane in planes:
            delete_node = nodes.cop_nodes.DeleteNode(ox_parent=self.ox_cop_node)
            delete_node.parm_delete.menu_non_scoped_planes___components
            delete_node.parm_scope = plane
            delete_node.connect_from(ox_node=self.ox_sop_node)

            rename_node = nodes.cop_nodes.RenameNode(ox_parent=self.ox_cop_node)
            rename_node.parm_from = plane
            rename_node.parm_to = rename_layer_name
            rename_node.connect_from(ox_node=delete_node)

            equalize_node = nodes.cop_nodes.EqualizeNode(ox_parent=self.ox_cop_node)
            equalize_node.connect_from(ox_node=rename_node)

            brightness_node = nodes.cop_nodes.BrightNode(ox_parent=self.ox_cop_node)
            brightness_node.connect_from(ox_node=equalize_node)

            null_node = nodes.cop_nodes.NullNode(ox_parent=self.ox_cop_node, node_name=f'OUT_{plane}')
            null_node.connect_from(ox_node=brightness_node)

    def get_output_hou_nodes(self):
        out_hou_nodes = self.ox_cop_node.get_children_hou_nodes_by_partial_name(substring='OUT_')
        return out_hou_nodes


