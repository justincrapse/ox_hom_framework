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

    def get_parm_template_type(self):
        print('sdfds')
        return self.__get_parm_template().type().name()

    def get_parm_template_label(self):
        return self.__get_parm_template().label()

