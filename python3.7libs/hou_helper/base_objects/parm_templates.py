import hou


class ParmTemplate:
    def __init__(self, node):
        self.node = node
        self.parm_template_group = node.parmTemplateGroup()

    def add_parm_template_to_node_folder(self, folder_label, parm_template):
        folder = self.parm_template_group.findFolder(folder_label)
        self.parm_template_group.appendToFolder(folder, parm_template)
        self.node.setParmTemplateGroup(parm_template_group=self.parm_template_group)

    def add_parm_template(self, parm_template):
        self.parm_template_group.append(parm_template)

    def add_int_parameter(self, name, label, num_components, folder_label=None, **kwargs):
        new_parm_template = hou.IntParmTemplate(name=name, label=label, num_components=num_components, **kwargs)
        if folder_label:
            self.add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.add_parm_template(parm_template=new_parm_template)
        return self.node.parm(name)
