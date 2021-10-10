

class Parameter:
    def __init__(self, parm):
        self.parm = parm

    def reference_other_parm(self, hh_other_parm):
        self.parm.set(hh_other_parm.parm)