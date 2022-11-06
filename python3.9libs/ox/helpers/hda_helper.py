import logging
import re

import hou
from ox.utils import ui

ox_logger = logging.getLogger("ox_logger")


from ox.base_objects.ox_node import OXNode
def get_ox_node_from_hda_parm(parm_name, node_class=OXNode, null_msg=None, allow_null=False, return_hou_node=False) -> OXNode:
    """ this will return an ox node for node path parm. Just a nice shortcut """
    node_path = hou.pwd().parm(parm_name).eval()
    if not node_path and not allow_null:
        msg = f'Expected value for parameter name "{parm_name}". But it was empty'
        null_msg = null_msg if null_msg else msg
        ui.display_message(message=null_msg, title='get_ox_node_from_hda_parm null message')
        raise ValueError(msg)
    hou_node = hou.node(node_path)
    ox_node = node_class(node=hou_node)
    return hou_node if return_hou_node else ox_node

def get_hda_parm_value(parm_name, as_raw_value=True, null_msg=None, allow_null=False):
    ox_logger.debug(f'get_hda_parm_value>HDA Parm: {hou.pwd().parm(parm_name)}')
    parm_value = hou.pwd().parm(parm_name).rawValue() if as_raw_value else hou.pwd().parm(parm_name).eval()
    if not parm_value and not allow_null:
        msg = f'Expected value for parameter name "{parm_name}". But it was empty'
        null_msg = null_msg if null_msg else msg
        ui.display_message(message=null_msg, title='get_hda_parm_value null message')
        raise ValueError(msg)
    return parm_value

def get_hda_parms_values_by_substring(parm_substring, as_raw_value=True, null_msg=None, allow_null=True):
    hda_ox_node = OXNode(node=hou.pwd())
    parms_list = hda_ox_node.get_parms_by_name_substring(substring=parm_substring)
    parm_values_list = [get_hda_parm_value(parm_name=i.name(), allow_null=allow_null, as_raw_value=as_raw_value, null_msg=null_msg) 
        for i in parms_list]
    return parm_values_list

def get_hda_parms_values_by_regex(regex_str, as_raw_value=True, null_msg=None, allow_null=True):
    hda_ox_node = OXNode(node=hou.pwd())
    parameters = hda_ox_node.get_parms()
    parm_sublist = [i for i in parameters if re.match(regex_str, i.name())]
    parm_values_list = [get_hda_parm_value(parm_name=i.name(), allow_null=allow_null, as_raw_value=as_raw_value, null_msg=null_msg) 
        for i in parm_sublist]
    return parm_values_list