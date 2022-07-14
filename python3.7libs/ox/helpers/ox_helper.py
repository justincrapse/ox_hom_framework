import logging

from ox.base_objects.ox_node import OXNode

ox_logger = logging.getLogger("ox_logger")


def delete_nodes_by_name_list(ox_parent_node: OXNode, node_name_list, debug=False):
    hou_nodes_list = {name: ox_parent_node.get_child_by_name(name) for name in node_name_list}
    for name, node in hou_nodes_list.items():
        if debug:
            print(f"Node name:{name}, Node: {node}")
        if node:
            node.destroy()


def delete_all_connected_nodes_upward(hou_node):
    for conn in hou_node.inputConnections():
        conn_hou_node = conn.inputNode()
        delete_all_connected_nodes_upward(hou_node=conn_hou_node)
    hou_node.destroy()


def reference_copy_nodes_to_source(source_hou_nodes, copied_hou_nodes):
    copied_hou_nodes = copied_hou_nodes if isinstance(copied_hou_nodes, list) else list(copied_hou_nodes)
    source_hou_nodes = source_hou_nodes if isinstance(source_hou_nodes, list) else list(source_hou_nodes)
    source_hou_nodes.sort(key=lambda x: x.name())
    copied_hou_nodes.sort(key=lambda x: x.name())
    for source_hou_node, copied_hou_node in zip(source_hou_nodes, copied_hou_nodes):
        for source_parm, copied_parm in zip(source_hou_node.parms(), copied_hou_node.parms()):
            ox_logger.debug(f"setting {copied_parm.name()} to {source_parm.name()}")
            copied_parm.set(source_parm)
