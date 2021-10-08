from .parameter import Parameter


class Menu(Parameter, object):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)

    def __getattribute__(self, item):
        if item in ['parm']:
            return object.__getattribute__(self, item)
        else:
            attr_val = object.__getattribute__(self, item)
            self.parm.set(str(attr_val))
