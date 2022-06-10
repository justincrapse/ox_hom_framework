import hou


class Parameter:
    def __init__(self, parm):
        self.parm = parm

    def reference_other_parm(self, hh_other_parm):
        self.parm.set(hh_other_parm.parm)

    def __get_path(self):
        return self.parm.path()

    def __get_parm_tuple(self):
        path = self.__get_path()
        return hou.parmTuple(path)

    def __get_parm_template(self):
        parm_tup = self.__get_parm_tuple()
        return parm_tup.parmTemplate()

    def get_raw_value(self):
        raw_value = self.parm.rawValue()
        return raw_value

    def get_parm_template_type(self):
        return self.__get_parm_template().type().name()

    def get_parm_template_label(self):
        return self.__get_parm_template().label()

    def press_button(self):
        self.parm.pressButton()

    def click(self):
        self.press_button()

    def lock_parm(self, on=True):
        self.parm.lock(on=on)
