import hou


def set_session_variable(var_name, value):
    setattr(hou.session, var_name, value)


def get_session_variable(var_name):
    if hasattr(hou.session, var_name):
        return getattr(hou.session, var_name)
