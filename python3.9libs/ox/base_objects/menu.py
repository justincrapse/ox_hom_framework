import logging

from .parameter import Parameter
from hou import OperationFailed
import hou

ox_logger = logging.getLogger("ox_logger")


class Menu(Parameter, object):
    def __init__(self, parm):
        self.parm: hou.Parm = parm
        super().__init__(parm=parm)

    def __getattribute__(self, item):
        ox_logger.debug(f"getting menu item: {item}")
        if "menu_" not in item:
            return object.__getattribute__(self, item)
        else:
            attr_tup = object.__getattribute__(self, item)
            str_attr = attr_tup[0]
            int_attr = attr_tup[1]
            ox_logger.debug(f"Setting {self.parm.name()} menu parameter to {str_attr}")
            try:
                self.parm.set(str_attr)
            except (TypeError, OperationFailed):
                ox_logger.debug(f"Failed to set {self.parm.name()} menu parameter to {str_attr}. trying int")
                self.parm.set(int_attr)
