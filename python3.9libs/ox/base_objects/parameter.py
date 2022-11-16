import hou


class Parameter:
    def __init__(self, parm):
        """since we are not sure of a parameter's instantiation given the nature of auto-generated code. We will only let "parm" come in and
        will not evaluate its common properties. We can then get those properties useing the "get" methods. If a paremeter instance was
        instantiated with a "None" from the automated code, you will need to reinstantiate the node class. This is done by simply creating the
        class instance after you know the parameter is present for the houdini node you are using to instantiate the class with."""
        self.parm: hou.Parm = parm

    def get_path(self):
        return self.parm.path()

    def get_parm_tuple(self):
        path = self.get_path()
        return hou.parmTuple(path)

    def get_parm_template(self):
        parm_tup = self.get_parm_tuple()
        return parm_tup.parmTemplate()

    def get_raw_value(self):
        raw_value = self.parm.rawValue()
        return raw_value

    def get_parm_template_type(self):
        return self.get_parm_template().type().name()

    def get_parm_template_label(self):
        return self.get_parm_template().label()

    def press_button(self):
        self.parm.pressButton()

    def click(self):
        self.press_button()

    def lock(self, on=True):
        self.parm.lock(on=on)
