import hou
from ox.utils import ui

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
    parm_value = hou.pwd().parm(parm_name).rawValue() if as_raw_value else hou.pwd().parm(parm_name).eval()
    if not parm_value and not allow_null:
        msg = f'Expected value for parameter name "{parm_name}". But it was empty'
        null_msg = null_msg if null_msg else msg
        ui.display_message(message=null_msg, title='get_hda_parm_value null message')
        raise ValueError(msg)
    return parm_value
    