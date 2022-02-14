from typing import List

import hou


def select_node(title=None, expect_selection=True):
    node_path = hou.ui.selectNode(title=title)
    if not node_path and expect_selection:
        exit()
    hou_node = hou.node(node_path)
    return hou_node


def get_clipboard_parm_path():
    parm_path = hou.parmClipboardContents()[0]['path']
    return parm_path


def select_one_from_list(options_list, message=None, title='Select One', expect_selection=True):
    selected = hou.ui.selectFromList(options_list, exclusive=True, message=message, title=title)
    if selected:
        selected_text = options_list[selected[0]]
        return selected_text
    elif expect_selection:
        exit()


def select_many_from_list(options_list, message=None, title='Select One or More', expect_selection=True):
    selected_indexes = hou.ui.selectFromList(options_list, exclusive=False, message=message, title=title)
    selected_items = [options_list[i] for i in selected_indexes]
    if selected_items:
        return selected_items
    if not selected_items and expect_selection:
        display_message('Expected Selection. Exiting script')
        exit()


def select_parm(message=None, title='Select Parm'):
    parm_path = hou.ui.selectParm(message=message, title=title)[0]
    return parm_path


def prompt_for_string_input(message, title='Enter String', default_text=None):
    return hou.ui.readInput(message=message, title=title, initial_contents=default_text)[1]


def read_input(message, title='Enter String', default_text=None):
    return prompt_for_string_input(message=message, title=title, default_text=default_text)


def read_multi_input(input_labels, message, title='Enter strings', return_values_only=False):
    string_values = hou.ui.readMultiInput(input_labels=input_labels, message=message, title=title)[1]
    if return_values_only:
        return [i for i in string_values if i]
    return dict(zip(input_labels, string_values))


def user_select_file():
    file_path = hou.ui.selectFile()
    file_path = file_path.replace('$JOB', hou.getenv('JOB'))
    file_path = file_path.replace('$HIP', hou.getenv('HIP'))
    file_path = file_path.replace('$HOME', hou.getenv('HOME'))
    return file_path


def get_parent_path_from_file_path(file_path):
    folder_path = '/'.join(file_path.split('/')[0: -1])
    return folder_path


def display_message(message, title='Display Dialogue'):
    result = hou.ui.displayMessage(text=message, title=title)
    return result


def display_confirmation(message, title='Confirmation Display', require_confirmation=False):
    result = hou.ui.displayConfirmation(text=message, title=title)
    if require_confirmation and not result:
        exit()
    return result


def get_selected_nodes(expect_selected=True, expected_message='Tool Expected Node Selection', only_one=False) -> List:
    hou_node_list = [i for i in hou.selectedNodes()]
    if not hou_node_list and expect_selected:
        display_message(message=f'{expected_message}')
        exit()
    if only_one and len(hou_node_list) > 1:
        display_message(message=f'{len(hou_node_list)} nodes selected, but only expecting one')
    return hou_node_list


def get_single_selected_node(expected_message='Tool Expected Node Selection'):
    nodes_list = get_selected_nodes(only_one=True, expected_message=expected_message)
    return nodes_list[0]


def verify_and_return_selected_nodes(expected_selected=True, title='Verify Selected Nodes'):
    selected_hou_nodes = get_selected_nodes(expect_selected=expected_selected)
    msg = '\n'.join([i.name() for i in selected_hou_nodes])
    result = display_confirmation(message=msg, title=title)
    if result:
        return selected_hou_nodes
    else:
        exit()


def verify_selected_nodes(selected_hou_nodes, title='Verify Selected Nodes'):
    selected_hou_nodes = selected_hou_nodes if isinstance(selected_hou_nodes, list) else [selected_hou_nodes]
    msg = '\n'.join([i.name() for i in selected_hou_nodes])
    result = display_confirmation(message=msg, title=title)
    if result:
        return selected_hou_nodes
    else:
        exit()
