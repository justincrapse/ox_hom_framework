import logging

import hou

from ox.base_objects.ox_node import OXNode

ox_logger = logging.getLogger("ox_logger")


def delete_nodes_by_name_list(ox_parent_node: OXNode, node_name_list, debug=False):
    hou_nodes_list = {
        name: ox_parent_node.get_child_node_by_name(name) for name in node_name_list
    }
    for name, node in hou_nodes_list.items():
        if debug:
            print(f"Node name:{name}, Node: {node}")
        if node:
            node.destroy()


def delete_all_connected_nodes_upward(node: hou.Node):
    ox_logger.debug(f"Starting delete all upstream nodes for {node.name()} node")
    for conn in node.inputConnections():
        conn_node = conn.inputNode()
        ox_logger.debug(f'Found output node "{conn_node.name()}" for node: {node}')
        delete_all_connected_nodes_upward(node=conn_node)
    ox_logger.debug(f"Destroying node: {node.name()}")
    node.destroy()


def delete_all_downstream_nodes(node: hou.Node):
    ox_logger.debug(f"Starting delete all downstream nodes for {node.name()} node")
    for conn in node.outputConnections():
        conn_node = conn.outputNode()
        ox_logger.debug(f'Found output node "{conn_node.name()}" for node: {node}')
        delete_all_downstream_nodes(node=conn_node)
    ox_logger.debug(f"Destroying node: {node.name()}")
    node.destroy()


def reference_copy_nodes_to_source(source_hou_nodes, copied_hou_nodes):
    """
    this method takes two lists of hou nodes and references copied nodes to source nodes.
    """
    copied_hou_nodes = (
        copied_hou_nodes
        if isinstance(copied_hou_nodes, list)
        else list(copied_hou_nodes)
    )
    source_hou_nodes = (
        source_hou_nodes
        if isinstance(source_hou_nodes, list)
        else list(source_hou_nodes)
    )
    source_hou_nodes.sort(key=lambda x: x.name())
    copied_hou_nodes.sort(key=lambda x: x.name())
    for source_hou_node, copied_hou_node in zip(source_hou_nodes, copied_hou_nodes):
        for source_parm, copied_parm in zip(
            source_hou_node.parms(), copied_hou_node.parms()
        ):
            ox_logger.debug(f"setting {copied_parm.name()} to {source_parm.name()}")
            copied_parm.set(source_parm)


def reference_node(source_node: hou.Node, destination_node: hou.Node):
    for source_parm, dest_parm in zip(source_node.parms(), destination_node.parms()):
        ox_logger.debug(f"setting {dest_parm.name()} to {source_parm.name()}")
        dest_parm.set(source_parm)
