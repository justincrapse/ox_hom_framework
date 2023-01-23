import logging
from typing import List


import hou

ox_logger = logging.getLogger("ox_logger")


class NetworkBox:
    def __init__(self, network_box, box_comment=None):
        self.network_box: hou.NetworkBox = network_box
        self.name = self.network_box.name()
        if box_comment:
            self.network_box.setComment(box_comment)

    def get_network_nodes(self) -> List[hou.Node]:
        nodes = self.network_box.nodes()
        return nodes

    def add_node(self, node: hou.Node):
        result = self.network_box.addItem(item=node)
        ox_logger.debug(f"Added item {node} to network box: {self.network_box}: result: {result}")

    def add_nodes(self, node_list: List[hou.Node]):
        for node in node_list:
            self.add_node(node=node)

    def get_network_node_by_type(self, node_type, raise_value_error=True, name_substring=None) -> hou.Node:
        """name_substring will be used in case multiple of same type are found"""
        node: hou.Node
        matching_nodes = []
        for node in self.get_network_nodes():
            hou_node_type = node.type().name()
            ox_logger.info(f"Node Type: {hou_node_type}")
            if hou_node_type == node_type:
                matching_nodes.append(node)
        matching_node_names_list = [i.name() for i in matching_nodes]
        ox_logger.debug(f"Matching network nodes of type {node_type}: {matching_nodes}")
        ox_logger.debug(f"Matching node names of type {node_type}: {matching_node_names_list}")
        if not matching_nodes and raise_value_error:
            raise ValueError(f'Node type "{node_type}" not found in network box "{self.name}"')
        if matching_nodes and len(matching_nodes) == 1:
            return matching_nodes[0]
        elif len(matching_nodes) > 1 and not name_substring:
            raise ValueError(f'Multiple nodes found for type "{node_type}": {matching_nodes}\n Did you mean to use "get_network_nodes_by_type?"')
        elif len(matching_nodes) > 1 and name_substring:
            node_substring_match = [i for i in matching_nodes if name_substring in i.name()]
            if not node_substring_match:
                raise ValueError(f"No node matching substring {name_substring} of type {node_type}")
            if len(node_substring_match) > 1:
                raise ValueError(f"Multiple nodes found for substring {name_substring} of type {node_type}")
            return node_substring_match[0]

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

    def get_nodes_parm_value_dict(self):
        """get a dict of dicts (node_name: {parm_name: parm_value}) for all nodes in network box"""
