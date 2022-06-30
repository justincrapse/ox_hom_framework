import logging


import hou

ox_logger = logging.getLogger("ox_logger")


class NetworkBox:
    def __init__(self, hou_network_box):
        self.network_box: hou.NetworkBox = hou_network_box
        self.name = self.network_box.name()

    def get_network_nodes(self):
        nodes = self.network_box.nodes()
        return nodes

    def get_network_node_by_type(self, node_type, raise_value_error=True):
        """This will return the fist matching node, so make sure you only really expect the one node of this type."""
        node: hou.Node
        for node in self.get_network_nodes():
            hou_node_type = node.type().name()
            ox_logger.info(f"Node Type: {hou_node_type}")
            if hou_node_type == node_type:
                return node
        if raise_value_error:
            raise ValueError(f'Node type "{node_type}" not found in network box "{self.name}"')
