import logging
import re

import hou
from ox.utils import ui

ox_logger = logging.getLogger("ox_logger")


from ox.base_objects.ox_node import OXNode


def get_ox_node_from_hda_parm(parm_name, node_class=OXNode, null_msg=None, allow_null=True, return_hou_node=False) -> OXNode:
    """this will return an ox node for node path parm. Just a nice shortcut"""
    ox_logger.debug(f'getting hda parm by name: {parm_name}. for method "get_ox_node_from_hda_parm"')
    node_path_parm = hou.pwd().parm(parm_name)
    if not node_path_parm:
        raise ValueError(f'No parm found for parm name "{parm_name}" for hda ox node using get_ox_node_from_hda_parm method')
    node_path = node_path_parm.eval()
    if not node_path and not allow_null:
        msg = f'Expected value for parameter name "{parm_name}". But it was empty'
        null_msg = null_msg if null_msg else msg
        ui.display_message(message=null_msg, title="get_ox_node_from_hda_parm null message")
        raise ValueError(msg)
    elif not node_path and allow_null:
        return None
    hou_node = hou.node(node_path)
    ox_node = node_class(node=hou_node)
    return hou_node if return_hou_node else ox_node


def get_parm_value(parm_name, as_raw_value=False, null_msg=None, allow_null=True):
    """
    parm_name: keep this as the first position as it is going to be the standard and only likely parameter required and passed without kwarg
    """
    ox_logger.debug(f"get_parm_value>HDA Parm: {hou.pwd().parm(parm_name)}")
    parm_value = hou.pwd().parm(parm_name).rawValue() if as_raw_value else hou.pwd().parm(parm_name).eval()
    if not parm_value and not allow_null:
        msg = f'Expected value for parameter name "{parm_name}". But it was empty'
        null_msg = null_msg if null_msg else msg
        ui.display_message(message=null_msg, title="get_parm_value null message")
        raise ValueError(msg)
    return parm_value


def get_menu_parm_value(parm_name, null_msg=None, allow_null=True):
    return get_parm_value(parm_name=parm_name, as_raw_value=True, null_msg=null_msg, allow_null=allow_null)


def get_color_parm_values(parm_name):
    r = hou.pwd().parm(f"{parm_name}r").eval()
    g = hou.pwd().parm(f"{parm_name}g").eval()
    b = hou.pwd().parm(f"{parm_name}b").eval()
    return r, g, b


def set_color_parm_values(parm_name, r, g, b):
    hou.pwd().parm(f"{parm_name}r").set(r)
    hou.pwd().parm(f"{parm_name}g").set(g)
    hou.pwd().parm(f"{parm_name}b").set(b)


def get_parm(parm_name)-> hou.Parm:
    """Returns the hda parm by name"""
    parm = hou.pwd().parm(parm_name)
    return parm


def get_parm_values_by_substring(substring, as_raw_value=False, null_msg=None, allow_null=True):
    hda_ox_node = OXNode(node=hou.pwd())
    parms_list = hda_ox_node.get_parms_by_name_substring(substring=substring)
    parm_values_list = [
        get_parm_value(
            parm_name=i.name(),
            allow_null=allow_null,
            as_raw_value=as_raw_value,
            null_msg=null_msg,
        )
        for i in parms_list
    ]
    return parm_values_list


def get_parm_values_by_regex(regex_str, as_raw_value=False, null_msg=None, allow_null=True):
    hda_ox_node = OXNode(node=hou.pwd())
    parameters = hda_ox_node.get_parms()
    parm_sublist = [i for i in parameters if re.match(regex_str, i.name())]
    parm_values_list = [
        get_parm_value(
            parm_name=i.name(),
            allow_null=allow_null,
            as_raw_value=as_raw_value,
            null_msg=null_msg,
        )
        for i in parm_sublist
    ]
    return parm_values_list
