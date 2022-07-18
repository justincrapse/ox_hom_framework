import logging
from typing import List


import hou

ox_logger = logging.getLogger("ox_logger")


class NetworkBox:
    def __init__(self, hou_network_box):
        self.network_box: hou.NetworkBox = hou_network_box
        self.name = self.network_box.name()

    def get_network_nodes(self) -> List[hou.Node]:
        nodes = self.network_box.nodes()
        return nodes

    def get_network_node_by_type(self, node_type, raise_value_error=True) -> hou.Node:
        node: hou.Node
        matching_nodes = []
        for node in self.get_network_nodes():
            hou_node_type = node.type().name()
            ox_logger.info(f"Node Type: {hou_node_type}")
            if hou_node_type == node_type:
                matching_nodes.append(node)
        if not matching_nodes and raise_value_error:
            raise ValueError(f'Node type "{node_type}" not found in network box "{self.name}"')
        if matching_nodes and len(matching_nodes) == 1:
            return matching_nodes[0]
        else:
            raise ValueError(f'Multiple nodes found for type "{node_type}": {matching_nodes}\n Did you mean to use "get_network_nodes_by_type?"')

    def get_network_nodes_by_type(self, node_type, raise_value_error=True) -> List[hou.Node]:
        node: hou.Node
        matching_nodes = []
        for node in self.get_network_nodes():
            hou_node_type = node.type().name()
            ox_logger.info(f"Node Type: {hou_node_type}")
            if hou_node_type == node_type:
                matching_nodes.append(node)
        if not matching_nodes and raise_value_error:
            raise ValueError(f'Node type "{node_type}" not found in network box "{self.name}"')
        else:
            return matching_nodes
