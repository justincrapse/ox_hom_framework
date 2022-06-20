import logging

from .parameter import Parameter
from hou import OperationFailed


class Menu(Parameter, object):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)

    def __getattribute__(self, item):
        logging.debug(f"getting menu item: {item}")
        if "menu_" not in item:
            return object.__getattribute__(self, item)
        else:
            attr_val = object.__getattribute__(self, item)
            msg = f"Setting {self.parm.name()} menu parameter to {attr_val}"
            logging.debug(msg)
            try:
                self.parm.set(str(attr_val))
            except OperationFailed:
                self.parm.set(attr_val)
