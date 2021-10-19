import hou


class ParmTemplate:
    def __init__(self, node):
        self.node = node
        self.parm_template_group = node.parmTemplateGroup()

    def __save_template_group(self):
        self.node.setParmTemplateGroup(parm_template_group=self.parm_template_group)

    def add_parm_template_to_node_folder(self, folder_label, parm_template):
        folder = self.parm_template_group.findFolder(folder_label)
        self.parm_template_group.appendToFolder(folder, parm_template)
        self.__save_template_group()

    def __add_parm_template(self, parm_template):
        self.parm_template_group.append(parm_template)
        self.__save_template_group()

    def add_folder(self, folder_label, folder_name):
        folder_template = hou.FolderParmTemplate(folder_name, folder_label)
        self.__add_parm_template(parm_template=folder_template)
        self.__save_template_group()

    def add_int_parameter(self, name, label, num_components, folder_label=None, **kwargs):
        new_parm_template = hou.IntParmTemplate(name=name, label=label, num_components=num_components, **kwargs)
        if folder_label:
            self.add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template)
        return self.node.parm(name)

    def add_toggle_parameter(self, name, label, folder_label=None, **kwargs):
        new_parm_template = hou.ToggleParmTemplate(name=name, label=label, **kwargs)
        if folder_label:
            self.add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template)
        return self.node.parm(name)

    def add_button_parameter(self, name, label, folder_label=None, join_with_next=False, script_callback=None,
                             script_callback_language=hou.scriptLanguage.Python, **kwargs):
        new_parm_template = hou.ButtonParmTemplate(name=name, label=label, join_with_next=join_with_next, script_callback=script_callback,
                                                   script_callback_language=script_callback_language, **kwargs)
        if folder_label:
            self.add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template)
        return self.node.parm(name)

    def add_string_parameter(self, name, label, num_components=1, folder_label=None,  multiline=False, join_with_next=False, script_callback=None,
                             script_callback_language=hou.scriptLanguage.Python, tags=None, **kwargs):
        tags = tags if tags else {}
        if multiline:
            tags['editor'] = '1'
        new_parm_template = hou.StringParmTemplate(name=name, label=label, num_components=num_components, join_with_next=join_with_next,
                                                   script_callback=script_callback, script_callback_language=script_callback_language,
                                                   tags=tags, **kwargs)
        if folder_label:
            self.add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template)
        return self.node.parm(name)



