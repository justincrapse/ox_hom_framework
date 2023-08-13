"""
WARNING:
this class' attribute access and namespace is particularly arranged. All access to attributes will be checked to see if it is a parameter existing
in the child class (that represents a houdini node.) Avoid adding attributes to this class. The few that are here are added to a "skip_list" so that
they are not evaluated in the same manner. If there is overlap with this skip list and a parameter attribute that you want to change, a message
will let the coder know that there is an overlap and that this particular attribute will have to be set using the hou module.
"""
from collections import defaultdict
import re
import logging
from typing import List

import hou

from ox.base_objects.parm_templates import ParmTemplate
from ox.utils.node_color_lookup import color_lookup_dict
from ox.constants import parm_template_types

ox_logger = logging.getLogger("ox_logger")


class OXNode(ParmTemplate):  # mixins
    # these are for child class lookups (that inherit from OXNode):
    parm_lookup_dict = {}

    def __init__(self, node=None):
        super().__init__(node=node)
        self.name: str = node.name()
        self.node: hou.Node = node
        self.path: str = node.path()
        self.type: str = node.type().name()

        # not sure how to handle this, but will leave for R2 review. This loads in user-defined node colors by node type.
        if self.type in color_lookup_dict:
            self.set_color(color_lookup_dict[self.type])

    def __setattr__(self, name, value):
        """
        What this special method does is overrides the nature of ox_some_node.parm_some_parm = some_new_value. Instead of just setting the
        instance value, which would do nothing in Houdini, this gets the actual parameter and sets it to some_new_value
        """
        skip_list = ["node", "name", "path", "type"]
        clean_key = self.__clean_parm_key(raw_key=name)
        if (
            clean_key in self.parm_lookup_dict
            and clean_key not in skip_list
            and hasattr(self, name)
        ):
            hou_parm_string = self.parm_lookup_dict[clean_key]
            ox_logger.debug(f"Hou parm string: {hou_parm_string}")
            parm = self.node.parm(hou_parm_string)
            parm.deleteAllKeyframes()  # this is for channel referencing. lots of issues with channel referencing otherwise.
            ox_logger.debug(
                f'Setting parm "{parm}" to value "{value}" of type: "{type(value)}"'
            )
            parm.set(value)
        else:
            super().__setattr__(name, value)

    @staticmethod
    def __clean_parm_key(raw_key):
        """Cleans the parm attribute name to match the key in the child ox node class parm_lookup_dict so that it can get the actual name of the
        parameter before it was modified to be a python-valid attribute name"""
        del_list = ["parm_"]
        clean_key = re.sub(
            r"{}".format("|".join(del_list)), "", raw_key
        )  # TODO: This is kind of odd and should have had a comment.
        return clean_key

    ##################################################################################################################################################
    # node opperations
    def delete_node(self):
        """A simple method to delete the current node. Also see destroy_node method"""
        self.destroy_node()

    def destroy_node(self):
        """A simple method to delete the current node. Also see delete_node method"""

        result = self.node.destroy()
        ox_logger.debug(f'Result for delete node "{self.name}": {result}')

    def delete_child_node_by_name(self, child_name, expect_child_node=True):
        """
        Deletes a child node matching the child_name. will raise an exception if no child is found and excpect_child_node is True

        :param expect_child_node: this is another parm
        """
        child_hou_node = self.get_child_node_by_name(child_name=child_name)
        if child_hou_node:
            child_hou_node.destroy()
        elif expect_child_node:
            raise ValueError(f'Expected child node with name "{child_name}"')

    def delete_all_child_nodes(self):
        """delete all child nodes. Keep in mind this might not delete everything within a node network. See "delete_all_items" method"""
        for child_node in self.get_child_nodes():
            child_node.destroy()

    def delete_all_items(self):
        """deletes all items within the node"""
        all_items = self.node.allItems()
        self.node.deleteItems(all_items)

    def get_input_labels(self):
        """Gets all input labels for the node"""
        labels = self.node.inputLabels()
        return list(labels)

    def get_input_label_index(self, label):
        """Given an input label, returns the input index value"""
        labels = self.get_input_labels()
        try:
            index = labels.index(label)
            return index
        except ValueError:
            raise ValueError(f"Label: {label}. Was not found in node: {self.path}")

    def get_input_connections_node_name_list(self):
        """Returns a list of node names of the connected input nodes"""
        connections = self.node.inputConnections()
        node_name_list = [i.inputItem().name() for i in connections]
        return node_name_list

    def get_connected_output_node_by_index(self, index=0) -> hou.Node:
        """Returns the node connected to the specified output index"""
        out_cons = self.node.outputConnections()
        connected_node = out_cons[index].outputItem()
        return connected_node

    def get_connected_input_node_by_index(self, index=0) -> hou.Node:
        """Returns the node connected to the specified input index"""
        in_cons = self.node.inputConnections()
        connected_node = in_cons[index].inputItem()
        return connected_node

    def create_node(self, node_type_name, node_name=None) -> hou.Node:
        """Creates a child node. It's better to create nodes using the 'nodes' package."""
        if node_name:
            node_name = node_name.replace(" ", "_")
        new_node = self.node.createNode(node_type_name, node_name)
        return new_node

    def create_node_if_not_exists(
        self, ox_node_class=None, ox_node_type=None, node_name=None
    ) -> hou.Node:
        """Creates a child node, but only if it does not already exist. need to pass in either ox_node_class or ox_node_type str"""
        node_type_name = ox_node_class.node_type if ox_node_class else ox_node_type
        if not node_type_name:
            raise ValueError("Need to specify either ox_node_class or ox_node_type str")
        child_node = self.get_child_node_by_name(child_name=node_name)
        if not child_node:
            child_node = self.create_node(
                node_type_name=node_type_name, node_name=node_name
            )
        return child_node

    def create_ox_node_if_not_exists(self, ox_node_class, node_name=None):
        """shortcut method that will go ahead and create and return an ox node"""
        child_node = self.create_node_if_not_exists(
            ox_node_class=ox_node_class, node_name=node_name
        )
        return ox_node_class(node=child_node)

    def connect_from_subnet_input(
        self, subnet_node: hou.Node, indirect_input_index, input_index=0
    ):
        self.node.setInput(
            input_index, subnet_node.indirectInputs()[indirect_input_index]
        )

    def connect_from(self, ox_node=None, input_index=0, out_index=0, input_label=None):
        """Connects to this node's input from another ox node's output. use input_label over input_index whenever possible."""
        other_hou_node = ox_node.node
        if input_label:
            input_index = self.get_input_label_index(label=input_label)
        self.node.setInput(
            input_index=input_index,
            item_to_become_input=other_hou_node,
            output_index=out_index,
        )

    def get_child_node_by_name(self, child_name) -> hou.Node:
        """Returns a matching child node, if it exists, else None is returned"""
        child_name = child_name.replace(
            " ", "_"
        )  # in case someone accidentally includes spaces.
        for child in self.get_child_nodes():
            if child.name() == child_name:
                return child

    def get_child_ox_node_by_name(self, child_name, node_class=None):
        """Returns a child ox node matching the child_hame parameter."""
        node_class = node_class if node_class else OXNode
        child_node = self.get_child_node_by_name(child_name=child_name)
        child_ox_node = node_class(child_node)
        return child_ox_node

    def get_child_node_by_partial_name(
        self, substring, exclude_substring=None, case_sensitive=True
    ) -> hou.Node:
        """Searches for a child node by substring. Returns the first match."""
        all_matches = self.get_child_nodes_by_partial_name(
            substring=substring,
            exclude_substring=exclude_substring,
            case_sensitive=case_sensitive,
        )
        first_match = all_matches[0]
        return first_match

    def has_child_with_name(self, child_name) -> bool:
        """Checks for child match by exact name"""
        return bool(self.get_child_node_by_name(child_name=child_name))

    def has_child_with_node_type(self, node_type, expect_match=False) -> bool:
        """Checks for a child match by node type"""
        return bool(
            self.get_child_by_node_type(node_type=node_type, expect_match=expect_match)
        )

    def child(self, child_name):
        """shorthand method for get_child_node_by_name"""
        child_node = self.get_child_node_by_name(child_name=child_name)
        return child_node

    def ox_child(self, child_name, node_class):
        ox_child = self.get_child_ox_node_by_name(
            child_name=child_name, node_class=node_class
        )
        return ox_child

    def get_child_node_paths_by_partial_name(self, substring) -> List[str]:
        """Returns child node paths based on child nodes matched to the substring"""
        path_list = []
        for node in self.get_child_nodes():
            if substring in node.name():
                path_list.append(node.path())
        return path_list

    def get_child_nodes_by_partial_name(
        self, substring, exclude_substring=None, case_sensitive=True
    ) -> List[hou.Node]:
        """Returns a list of child nodes matched by substring"""
        node_list = []
        for node in self.get_child_nodes():
            node_name = node.name()
            node_name_lower = node_name.lower()
            if not case_sensitive and exclude_substring:
                if (
                    substring.lower() in node_name_lower
                    and exclude_substring.lower() not in node_name_lower
                ):
                    node_list.append(node)
            elif not case_sensitive:
                if substring.lower() in node_name_lower:
                    node_list.append(node)
            elif exclude_substring:
                if substring in node_name and exclude_substring not in node_name:
                    node_list.append(node)
            else:
                if substring in node_name:
                    node_list.append(node)
        return node_list

    def get_child_nodes(self) -> List[hou.Node]:
        """Returns all child nodes"""
        children_node_list = self.node.children()
        return children_node_list

    def get_all_items(self):
        all_items = self.node.allItems()
        return all_items

    def get_child_nodes_by_type(self, node_type, substring=None, expect_match=False):
        """Returns all child nodes mathcing specified type."""
        if substring:
            matching_nodes = [
                i
                for i in self.get_child_nodes_by_partial_name(substring=substring)
                if i.type().name() == node_type
            ]
        else:
            matching_nodes = [
                i for i in self.get_child_nodes() if i.type().name() == node_type
            ]
        if not matching_nodes and expect_match:
            raise ValueError(
                f'Expected child node of type "{node_type}" but no matches were found'
            )
        return matching_nodes

    def get_child_node_by_type(self, node_type, substring=None, expect_match=False):
        """Returns the first matching child node of node_type parameter"""
        if substring:
            matching_nodes = self.get_child_nodes_by_type(
                node_type=node_type, expect_match=expect_match, substring=substring
            )
        else:
            matching_nodes = self.get_child_nodes_by_type(
                node_type=node_type, expect_match=expect_match
            )
        return matching_nodes[0]

    def get_child_ox_node_by_type(self, node_class, expect_match=False):
        """Returns the first matching child node as ox node of node_type parameter"""
        node_type = node_class.node_type
        matching_nodes = self.get_child_nodes_by_type(
            node_type=node_type, expect_match=expect_match
        )
        child_ox_node = node_class(matching_nodes[0])
        return child_ox_node

    def get_child_by_node_type(
        self, node_type, substring=None, expect_match=False, only_one_match=True
    ):
        """WARNING: TO BE DEPRICATED. this is redundant and poorly named. use get_child_node_by_type instead"""
        matching_nodes = self.get_child_nodes_by_type(
            node_type=node_type, expect_match=expect_match
        )
        if matching_nodes and len(matching_nodes) > 1 and only_one_match:
            raise ValueError(
                f"Expected only one match for child node type {node_type} but found many: {matching_nodes}"
            )
        if matching_nodes and len(matching_nodes) == 1:
            return matching_nodes[0]

    def get_child_nodes_by_regex(self, regex_str):
        """Returns all nodes with names that match the regular expression"""
        child_nodes = self.get_child_nodes()
        matching_nodes = [i for i in child_nodes if re.match(regex_str, i.name())]
        return matching_nodes

    def set_color(self, color):
        """Can pass in a tuple for RGB values or a hou.Color object."""
        color = color if isinstance(color, hou.Color) else hou.Color(color)
        self.node.setColor(color)

    def set_name(self, new_name):
        """Sets the node name"""
        self.node.setName(new_name)
        self.name = new_name

    def get_prim_values_by_field(self, field, filter_out_blank_values=True):
        """Returns primative values by specified field"""
        value_list = [i.attribValue(field) for i in self.node.geometry().prims()]
        if filter_out_blank_values:
            value_list = [i for i in value_list if i]
        return value_list

    def get_planes(self):
        """Returns planes. Heightfield Masks are held as planes. Not sure what else this is fore."""
        planes = self.node.planes()
        ox_logger.debug(f"planes returned by get_planes for node {self.name}: {planes}")
        planes_clean = [i for i in planes if i]
        ox_logger.debug(
            f"clean planes returned by get_planse for node {self.name}: {planes}"
        )
        return planes_clean

    def get_heightfield_masks(self):
        hf_masks = self.get_planes()
        return hf_masks

    def get_displayed_child_node(self) -> hou.Node:
        """Returns displayed child node."""
        for node in self.get_child_nodes():
            if node.isDisplayFlagSet():
                return node

    def is_display_flag_set(self):
        """Checks to see if display flag is set"""
        return self.node.isDisplayFlagSet()

    def layout_children(self):
        """Auto-layout children"""
        self.node.layoutChildren()

    def move_node_relative_to(self, ox_node, x=0, y=-1, unit_multiplier=1):
        """a handy method that will move this node relative to another node. The default moves the node below the relative node"""
        relative_position_vector = ox_node.node.position()
        r_x = relative_position_vector[0]
        r_y = relative_position_vector[1]
        vector = hou.Vector2(r_x + x * unit_multiplier, r_y + y * unit_multiplier)
        self.node.setPosition(vector)

    def unlock_node(self):
        """Allows editing of node contents."""
        self.node.allowEditingOfContents()

    def get_folder_labels(self):
        """Returns top-level folder labels."""
        templates = self.get_parm_templates_by_type(
            template_type=parm_template_types.FOLDER
        )
        labels = [i.label() for i in templates]
        return labels

    def set_display_flag(self, on=True):
        """Sets the display flag"""
        self.node.setDisplayFlag(on=on)

    def set_render_flag(self, on=True):
        """Sets the render flag"""
        self.node.setRenderFlag(on=on)

    def set_display_and_render_flags(self, on=True):
        """Sets the display and render flags"""
        self.set_display_flag(on=on)
        self.set_render_flag(on=on)

    def set_bypass_flag(self, on=True):
        """Sets the bypass flag"""
        self.node.bypass(on=on)

    def get_prim_groups(self):
        """Returns the primative group names"""
        group_list = [i.name() for i in self.node.geometry().primGroups()]
        return group_list

    def get_prim_int_values(self, prim_name):
        """Returns primative integer values by prim name"""
        geo = self.node.geometry()
        value_tup = geo.primIntAttribValues(prim_name)
        return value_tup

    def load_preset(self, preset_name=None):
        """Loads a preset. if no preset name specified, just use the node name. This is a good default for many use cases"""
        preset_name = preset_name if preset_name else self.name
        script = f"oppresetload {self.path} {preset_name}"
        ox_logger.debug(f"Running script: {script}")
        result = hou.hscript(script)
        if "Invalid preset name" not in result[1]:
            ox_logger.info(
                f'Successfully Loaded Preset Name "{preset_name}" for node type {self.type}'
            )
        else:
            ox_logger.info(
                f'Preset Name "{preset_name}" Not Found for node type {self.type}. Result: {result}'
            )

    def save_preset(self, preset_name, preset_path, node_path=None):
        """Saves a preset"""
        node_path = node_path if node_path else self.path
        script = f'oppresetsave {node_path} "{preset_name}" {preset_path}'
        result = hou.hscript(script)
        if result[1]:
            ox_logger.debug(f"there was a result message: {result}")
        ox_logger.info(
            f"Saved preset {preset_name} to node {node_path} to folder: {preset_path} Result: {result}"
        )

    def delete_preset(self, node_path, preset_name, preset_path=None):
        """Deletes a preset. uses default preset path when preset_path not specified"""
        if preset_path:
            script = f'oppresetrm {node_path} "{preset_name}" {preset_path}'
        else:
            script = f'oppresetrm {node_path} "{preset_name}"'
        result = hou.hscript(script)
        if result[1]:
            ox_logger.info(f"there was a result message: {result}")
        ox_logger.info(
            f"Deleted preset {preset_name} on node {node_path} on folder: {preset_path} Result: {result}"
        )

    def select_node(self, on=True):
        """ " Set node as selected"""
        self.node.setSelected(on=on)

    def rename_node(self, new_name):
        """Alternative to 'set_name' with more debugging if needed."""
        ox_logger.info(f'renaming node from "{self.name}" to "{new_name}"')
        result = self.node.setName(name=new_name)
        self.name = new_name
        ox_logger.debug(f"rename node result: {result}")

    def get_input_connections_count(self):
        """returns number of connected input connections"""
        input_count = len(self.node.inputConnections())
        return input_count

    def copy_node(
        self,
        new_name_postfix=None,
        destination_node: hou.Node = None,
        delete_if_exists=False,
        keep_existing_parm_values=False,
        return_ox=True,
        keep_existing_children_parm_values=False,
    ):
        """Copies a node to a destination with optional behaviors"""
        parent_node = self.node.parent()
        parent_ox_node = OXNode(parent_node)
        new_name = f"{self.name}_{new_name_postfix}" if new_name_postfix else self.name
        has_existing = parent_ox_node.has_child_with_name(child_name=new_name)
        if has_existing and not delete_if_exists:
            raise ValueError(f'Node with name "{new_name}" already exists')
        if has_existing:
            existing_node = parent_ox_node.get_child_node_by_name(child_name=new_name)
            existing_ox_node = OXNode(existing_node)
            if keep_existing_children_parm_values:
                child_parms_dict = existing_ox_node.get_child_parms_dict()
            if keep_existing_parm_values:
                node_parm_values_dict = existing_ox_node.get_parms_as_dict()
            if delete_if_exists:
                existing_ox_node.destroy_node()

        destination_node = destination_node if destination_node else parent_node
        copied_node = hou.copyNodesTo(
            nodes=[self.node], destination_node=destination_node
        )
        copied_ox_node = OXNode(copied_node[0])
        copied_ox_node.set_name(new_name=new_name)
        if has_existing and keep_existing_children_parm_values:
            copied_ox_node.apply_child_parms_dict(children_parms_dict=child_parms_dict)
        if has_existing and keep_existing_parm_values:
            copied_ox_node.apply_parms_dict(parms_dict=node_parm_values_dict)
        return copied_ox_node if return_ox else copied_node

    ##################################################################################################################################################
    # parm methods
    def get_parms(self) -> List[hou.Parm]:
        """Gets all parms"""
        parameters = self.node.parms()
        return parameters

    def get_parms_by_name_substring(
        self, substring, ends_with=False, starts_with=False
    ) -> List[hou.parm]:
        """Returns all parms that match the specified substring"""
        parameters = self.get_parms()
        if ends_with:
            parm_sublist = [i for i in parameters if i.name().endswith(substring)]
        elif starts_with:
            parm_sublist = [i for i in parameters if i.name().startswith(substring)]
        else:
            parm_sublist = []
            for item in parameters:
                if substring in item.name():
                    parm_sublist.append(item)
                    ox_logger.info(
                        f'Substring "{substring}" is in "{item.name()}": {substring in item.name()}'
                    )
        ox_logger.info(f"return parm_sublist: {parm_sublist}")
        return parm_sublist

    def remove_parms_by_name_substring(
        self, substring, ends_with=False, starts_with=False
    ):
        """Removes all parms by name that match a substring"""
        parm_list = self.get_parms_by_name_substring(
            substring=substring, ends_with=ends_with, starts_with=starts_with
        )
        for parm in parm_list:
            ox_logger.info(
                f"removing parm by name: {parm.name()} for substring: {substring}"
            )
            self.remove_parm_template_by_name(parm.name(), save_template_group=False)
        self._save_template_group()

    def get_parms_by_regex(self, regex_str):
        """Returns all parms that match the regular expression"""
        parameters = self.get_parms()
        parm_sublist = [i for i in parameters if re.match(regex_str, i.name())]
        return parm_sublist

    def get_parm_labels(self):
        """Returns all parm labels"""
        parameters = self.get_parms()
        parm_label_list = [i.label() for i in parameters]
        return parm_label_list

    def get_parm_names(self):
        """Returns all parm names"""
        parameters = self.get_parms()
        parm_name_list = [i.name() for i in parameters]
        return parm_name_list

    def get_parm_names_by_substring(self, substring):
        """Returns all parm names that match the substring"""
        parm_names = self.get_parm_names()
        parm_sublist = [i for i in parm_names if substring in i]
        return parm_sublist

    def delete_parms_by_name(self, parm_name_list: List[str]):
        """Deletes all parameters by list of parm names"""
        for parm_name in parm_name_list:
            self.remove_parm_template_by_name(parm_name=parm_name)

    ##################################################################################################################################################
    # copying and re-applying parm values methods:

    def get_parms_as_dict(self, substring=None, as_raw_value=False):
        """
        returns all parameters as a dictionary with the parm name as key and parm value as the value.
        If a substring is specified, this will only match parameter names with that substring
        """
        parm_list = (
            self.get_parms_by_name_substring(substring=substring)
            if substring
            else self.get_parms()
        )
        if as_raw_value:
            parm_dict = {i.name(): i.rawValue() for i in parm_list}
        else:
            parm_dict = {i.name(): i.eval() for i in parm_list}
        return parm_dict

    def apply_parms_dict(self, parms_dict):
        """Applies the values from a parm dictionary returned by get_parms_as_dict"""
        for parm_name, parm_value in parms_dict.items():
            ox_logger.debug(f'Setting parameter "{parm_name}" to value "{parm_value}"')
            parm = self.node.parm(parm_name)
            if parm:
                parm.set(parm_value)
            else:
                ox_logger.debug(
                    f'No parameter "{parm_name}" to set value to: {parm_value}'
                )

    def get_child_parms_dict(
        self, node_list: List[hou.Node] = None, exclude_type_list: List[str] = None
    ):
        """
        exclude_type_list: a list of types (from node.type() values) to exclude from the parms dict
        handy method that gets all children nodes and parameters as a dict to reaply later or to another node.
        """
        child_parms_dict = defaultdict(dict)
        node_list = node_list if node_list else self.get_child_nodes()
        if exclude_type_list:
            clean_node_list = []
            for node in node_list:
                node_type = node.type().name()
                ox_logger.debug(
                    f"child_node_type: {node_type}, exclusion_list={exclude_type_list}"
                )
                if node_type not in exclude_type_list:
                    clean_node_list.append(node)
            node_list = clean_node_list
        for node in node_list:
            ox_logger.debug(f"coppying parms for child node {node.name()}")
            for parm in node.parms():
                parm_value = parm.eval()
                parm_name = parm.name()
                node_name = node.name()
                child_parms_dict[node_name][parm_name] = parm_value
        return child_parms_dict

    def apply_child_parms_dict(self, children_parms_dict):
        """Applies a dictionary of child nodes and their parameter values as returned from get_child_parms_dict method"""
        for key, value in children_parms_dict.items():
            ox_logger.debug(
                f"Getting child node by key: ({key}) to apply children parms to"
            )
            key_node: hou.Node = self.get_child_node_by_name(key)
            for parm_key, parm_value in value.items():
                try:
                    parm: hou.Parm = key_node.parm(parm_key)
                except AttributeError:
                    ox_logger.info(
                        f'No parm "{parm_key}" found for node {key_node} to apply value to. Skipping'
                    )
                    continue
                ox_logger.debug(
                    f'Node: {key_node} - Setting parm "{parm_key}" to value: {parm_value}'
                )
                parm.set(parm_value)

    ##################################################################################################################################################
    # network box node stuff. Put dedicated network box methods in the network box base object.

    def get_parent_network_box(self):
        """Returns the parent Network box this node is contained in."""
        parent_network_box = self.node.parentNetworkBox()
        return parent_network_box
