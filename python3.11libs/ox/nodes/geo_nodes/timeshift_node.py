from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class TimeshiftNode(OXNode):
    node_type = 'timeshift'
    parm_lookup_dict = {'method': 'method', 'frame': 'frame', 'integerframe': 'integerframe', 'time': 'time', 'rangeclamp': 'rangeclamp', 'frange1': 'frange1', 'frange2': 'frange2', 'trange1': 'trange1', 'trange2': 'trange2'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_frame = Parameter(parm=self.node.parm('frame'))
        self.parm_integerframe = Parameter(parm=self.node.parm('integerframe'))
        self.parm_time = Parameter(parm=self.node.parm('time'))
        self.parm_frange1 = Parameter(parm=self.node.parm('frange1'))
        self.parm_frange2 = Parameter(parm=self.node.parm('frange2'))
        self.parm_trange1 = Parameter(parm=self.node.parm('trange1'))
        self.parm_trange2 = Parameter(parm=self.node.parm('trange2'))

        
        # parm menu vars:
        self.parm_method = MethodMenu(parm=self.node.parm('method'))
        self.parm_rangeclamp = RangeclampMenu(parm=self.node.parm('rangeclamp'))


        # input vars:
        self.input_input_1 = 'Input 1'


# parm menu classes:
class MethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_by_frame = ("byframe", 0)
        self.menu_by_time = ("bytime", 1)


class RangeclampMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("none", 0)
        self.menu_clamp_to_first = ("first", 1)
        self.menu_clamp_to_last = ("last", 2)
        self.menu_clamp_to_both = ("both", 3)



