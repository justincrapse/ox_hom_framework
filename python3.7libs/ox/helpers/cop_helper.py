import hou

from ox.base_objects.ox_node import OXNode
from ox import nodes


class COPHelper:
    def __init__(self, ox_cop_node):
        self.obj_node = OXNode(node=hou.node("/obj"))
        self.ox_cop_node: nodes.obj_nodes.CopNetNode = ox_cop_node

    def get_planes(self):
        planes = self.ox_sop_node.get_planes()
        return planes

    def create_output_for_each_plane(self, ox_copnet_node, rename_layer_name="C"):
        planes = ox_copnet_node.get_planes()
        for plane in planes:
            delete_node = nodes.cop_nodes.DeleteNode(ox_parent=self.ox_cop_node, node_name=f"{plane}_delete")
            delete_node.parm_delete.menu_non_scoped_planes___components
            delete_node.parm_scope = plane
            delete_node.connect_from(ox_node=self.ox_sop_node)

            rename_node = nodes.cop_nodes.RenameNode(ox_parent=self.ox_cop_node, node_name=f"{plane}_rename")
            rename_node.parm_from = plane
            rename_node.parm_to = rename_layer_name
            rename_node.connect_from(ox_node=delete_node)

            equalize_node = nodes.cop_nodes.EqualizeNode(ox_parent=self.ox_cop_node, node_name=f"{plane}_equalize")
            equalize_node.connect_from(ox_node=rename_node)
            equalize_node.load_preset(plane)

            brightness_node = nodes.cop_nodes.BrightNode(ox_parent=self.ox_cop_node, node_name=f"{plane}_brightness")
            brightness_node.connect_from(ox_node=equalize_node)
            brightness_node.load_preset(plane)

            null_node = nodes.cop_nodes.NullNode(ox_parent=self.ox_cop_node, node_name=f"OUT_{plane}")
            null_node.connect_from(ox_node=brightness_node)

            self.ox_cop_node.layout_children()

    def get_output_hou_nodes(self):
        out_hou_nodes = self.ox_cop_node.get_children_nodes_by_partial_name(substring="OUT_")
        return out_hou_nodes
