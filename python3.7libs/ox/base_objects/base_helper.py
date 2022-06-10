import hou


from ox.base_objects.ox_node import OXNode


class BaseHelper:
    def __init__(self):
        self.obj_node = OXNode(node=hou.node('/obj'))