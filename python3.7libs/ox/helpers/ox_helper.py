import hou
from ox.base_objects.ox_node import OXNode


class OXHelper:
    def __init__(self):
        self.obj_node = OXNode(node=hou.node('/obj'))

    def delete_nodes_by_name_list(self, ox_parent_node: OXNode, node_name_list, debug=False):
        hou_nodes_list = {name: ox_parent_node.get_child_by_name(name) for name in node_name_list}
        for name, node in hou_nodes_list.items():
            if debug:
                print(f'Node name:{name}, Node: {node}')
            if node:
                node.destroy()

    def delete_all_connected_nodes_upward(self, hou_node):
        for conn in hou_node.inputConnections():
            conn_hou_node = conn.inputNode()
            self.delete_all_connected_nodes_upward(hou_node=conn_hou_node)
        hou_node.destroy()


