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


def prompt_for_string_input(message, title='Enter String'):
    return hou.ui.readInput(message=message, title=title)[1]
