import hou


def select_node():
    node_path = hou.ui.selectNode()
    hou_node = hou.node(node_path)
    return hou_node


def get_clipboard_parm_path():
    parm_path = hou.parmClipboardContents()[0]['path']
    return parm_path


def select_one_from_list(options_list):
    selected = hou.ui.selectFromList(options_list, exclusive=True)
    if selected:
        selected_text = options_list[selected[0]]
        return selected_text


def prompt_for_string_input(message, title='Enter String', default_text=None):
    return hou.ui.readInput(message=message, title=title, initial_contents=default_text)[1]


def user_select_file(return_parent_folder_path=False):
    file_path = hou.ui.selectFile()
    return file_path


def get_parent_path_from_file_path(file_path):
    folder_path = '/'.join(file_path.split('/')[0: -1])
    return folder_path
