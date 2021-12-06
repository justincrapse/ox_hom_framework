import hou

from ox.base_objects.ox_node import OXNode
from ox import nodes
from ox.constants import node_names
from ox.constants import colors


class TerrainHelper:
    def __init__(self, terrain_node: nodes.obj_nodes.GeoNode, scatter_anchor_node: OXNode):
        self.obj_node = OXNode(node=hou.node('/obj'))
        self.terrain_node = terrain_node
        self.hf_node = scatter_anchor_node
        # scatter bridge setup:
        self.scatter_bridge_node = self.obj_node.create_node_if_not_exist(
            ox_node_class=nodes.obj_nodes.GeoNode, node_name=node_names.SCATTER_BRIDGE)  # type: nodes.obj_nodes.GeoNode
        self.scatter_bridge_node.set_color(colors.cerulean_blue)
        self.scatter_bridge_node.set_display_flag(on=False, include_render_flag=False)
        self.geo_import_node_tup_list = []  # we need a count, so a dict doesn't work
        self.mask_null_node_dict = {}
        self.prev_hf_node = None
        self.new_obj_mask_name = None  # name of the following hf mask

    def get_user_masks(self, mask_suffix='_mask'):
        prim_names = self.hf_node.get_prim_values(field='name')
        user_masks = [i for i in prim_names if i.endswith(mask_suffix)]
        return user_masks

    def get_scatter_nodes(self, node_name_substring='mask_hf_scatter'):
        scatter_nodes = self.terrain_node.get_children_hou_nodes_by_partial_name(substring=node_name_substring)
        return scatter_nodes

    def get_scatter_node_names(self):
        scatter_nodes = self.get_scatter_nodes()
        scatter_nodes_names_list = [i.name() for i in scatter_nodes]
        return scatter_nodes_names_list

    def get_used_mask_names_from_scatter_nodes(self):
        user_masks = self.get_user_masks()
        scatter_nodes = self.get_scatter_nodes()
        mask_names_list = [i.name().replace('_hf_scatter', '') for i in scatter_nodes]
        sorted_used_masks = [mask for mask in user_masks if mask in mask_names_list]
        return sorted_used_masks

    def get_unused_user_mask_names(self):
        used_mask_names = set(self.get_used_mask_names_from_scatter_nodes())
        user_masks = set(self.get_user_masks())
        available_masks = user_masks - used_mask_names
        return list(available_masks)

    def get_scatter_set_nodes(self):
        scatter_set_nodes = self.obj_node.get_children_hou_nodes_by_partial_name('scatter_set')
        return scatter_set_nodes

    def get_scatter_set_node(self, scatter_set_name):
        scatter_nodes = self.get_scatter_set_nodes()
        for hou_node in scatter_nodes:
            if hou_node.name() == f'{scatter_set_name}_scatter_set':
                return hou_node

    def set_scatter_set_imports_in_bridge(self, scatter_set_hou_node, postfix='OUT_'):
        scatter_set_node = OXNode(node=scatter_set_hou_node)
        path_list = scatter_set_node.get_children_paths_by_partial_name(substring=postfix)
        geo_node_name = scatter_set_hou_node.name()
        node_name = f'{geo_node_name}_import'
        merge_object_node = self.scatter_bridge_node.create_node_if_not_exist(
            ox_node_class=nodes.geo_nodes.ObjectMergeNode, node_name=node_name)  # type: nodes.geo_nodes.ObjectMergeNode
        merge_object_node.parm_numobj = len(path_list)
        for index, path in enumerate(path_list, 1):
            merge_object_node.node.parm(f'objpath{index}').set(path)
        merge_object_node.parm_pack = True
        self.geo_import_node_tup_list.append((geo_node_name, merge_object_node))

    def finish_scatter_set_bridge_to(self, mask_name):
        name_only = mask_name.replace('_mask', '')
        null_node = self.scatter_bridge_node.create_node_if_not_exist(
            ox_node_class=nodes.geo_nodes.NullNode, node_name=f'OUT_{mask_name}')  # type: nodes.geo_nodes.NullNode
        matching_import_nodes = [i for i in self.geo_import_node_tup_list if name_only in i[0]]
        xform_node = self.scatter_bridge_node.create_node_if_not_exist(
            ox_node_class=nodes.geo_nodes.TransformNode, node_name=f'{mask_name}_xform')  # type: nodes.geo_nodes.TransformNode
        if len(matching_import_nodes) > 1:
            merge_node = self.scatter_bridge_node.create_node_if_not_exist(
                ox_node_class=nodes.geo_nodes.MergeNode, node_name=f'{mask_name}_merge_node')  # type: nodes.geo_nodes.MergeNode
            for index, ox_node in enumerate(matching_import_nodes):
                weight_node_name = f'{mask_name}_weight_attr_{index}'
                weight_attr_node = self.scatter_bridge_node.create_node_if_not_exist(
                    ox_node_class=nodes.geo_nodes.AttribcreateNode, node_name=weight_node_name)  # type: nodes.geo_nodes.AttribcreateNode
                weight_attr_node.parm_name1 = 'weight'
                weight_attr_node.parm_value1v1 = 1
                weight_attr_node.parm_class1.menu_primitive
                weight_attr_node.connect_from(ox_node=ox_node[1])
                merge_node.connect_from(ox_node=weight_attr_node, input_index=index)
            xform_node.connect_from(merge_node)
        elif matching_import_nodes:
            xform_node.connect_from(ox_node=matching_import_nodes[0][1])
        null_node.connect_from(xform_node)
        self.mask_null_node_dict[mask_name] = null_node

    def create_scatter_node(self, user_mask, user_source_points, prev_hf_node, next_mask=None, is_first_mask=False, is_last_mask=False,
                            simple_scatter=False, scatter_node=None, preset_lookup_dict=None):
        """
        Make sure we don't have any defaults AFTER a node preset is loaded.
        """
        prev_hf_node = self.prev_hf_node if self.prev_hf_node else prev_hf_node
        name_only = user_mask.replace('_mask', '')
        preset_name = preset_lookup_dict.get(name_only, name_only)
        if not scatter_node:
            scatter_node = nodes.geo_nodes.HeightfieldScatterNode(ox_parent=self.terrain_node, node_name=f'{user_mask}_hf_scatter')
            scatter_node.unlock_node()
            scatter_node.parm_keepterrain = False
            scatter_node.parm_keepscatterpoints = False
            scatter_node.parm_randomyaw = 180
            scatter_node.load_preset(preset_name=preset_name)
            new_vex_hou_parm = scatter_node.add_string_parameter(name=f'{user_mask}_scat_vex', label=f'{user_mask}_Scatter Point Vex', multiline=True)
            scatter_node.add_float_parameter(name='falloff_scalar', label=f'Vex Falloff Scalar', min_f=1, max_f=10)
            scatter_node.add_float_parameter(name='pluck_scalar', label=f'Vex Pluck Scalar', min_f=0, max_f=1)
            scatter_node.add_float_parameter(name='extra_scalar', label=f'Vex Extra Scalar', min_f=0, max_f=10)
            if user_source_points:
                source_tag = f'{user_mask}_source_scatter'
                source_scatter_node = nodes.geo_nodes.HeightfieldScatterNode(ox_parent=self.terrain_node, node_name=f'{user_mask}_source_scatter')
                if is_first_mask:
                    source_scatter_node.parm_layer = user_mask
                source_scatter_node.connect_from(ox_node=prev_hf_node)
                source_scatter_node.connect_from(ox_node=prev_hf_node, input_label=source_scatter_node.input_mask_or_scatter_points)
                source_scatter_node.parm_coverage = 0.13  # just in case, but will be overridden by load_preset if exists
                # now load presets specific to source-point scattering.
                source_scatter_node.load_preset(preset_name=f'{preset_name}_source')
                scatter_node.load_preset(preset_name=f'{preset_name}_point')
                scatter_node.connect_from(ox_node=source_scatter_node)
                scatter_node.connect_from(ox_node=source_scatter_node, input_label=scatter_node.input_mask_or_scatter_points)
                scatter_node.parm_scattermethod.menu_per_point_count_using_source_points
                scatter_node.parm_sourcetag = source_tag
            else:
                if is_first_mask or simple_scatter:
                    scatter_node.parm_layer = user_mask
                scatter_node.connect_from(ox_node=prev_hf_node, input_label=scatter_node.input_terrain)
                scatter_node.connect_from(ox_node=prev_hf_node, input_label=scatter_node.input_mask_or_scatter_points)

            # inner vex wrangle:
            inner_vex_node = nodes.geo_nodes.AttribwrangleNode(ox_parent=scatter_node, node_name=f'{user_mask}_inner_vex')
            inner_vex_node.parm_snippet = new_vex_hou_parm
            # get the prev and next inner nodes
            prev_inner_hou_node = scatter_node.get_child_by_name('generate_rand_id')
            next_inner_hou_node = scatter_node.get_child_by_name('foreach_begin2')
            prev_inner_node = OXNode(node=prev_inner_hou_node)
            next_inner_node = OXNode(node=next_inner_hou_node)
            inner_vex_node.connect_from(prev_inner_node)
            next_inner_node.connect_from(inner_vex_node)

            import_node = nodes.geo_nodes.ObjectMergeNode(ox_parent=self.terrain_node, node_name=f'{user_mask}_import_from_bridge')
            import_node.parm_objpath1 = f'{self.scatter_bridge_node.path}/{f"OUT_{user_mask}"}'
            scatter_node.connect_from(ox_node=import_node, input_label=scatter_node.input_primitives_to_instance)
            if simple_scatter:
                return

        if not is_last_mask:
            mask_by_obj_node = nodes.geo_nodes.HeightfieldMaskbyobjectNode(ox_parent=self.terrain_node, node_name=f'{user_mask}_mask_by_obj')
            mask_by_obj_node.connect_from(ox_node=prev_hf_node)
            mask_by_obj_node.connect_from(ox_node=scatter_node, input_label=mask_by_obj_node.input_geometry_to_build_mask_from)
            mask_by_obj_node.parm_maskdir.menu_below_heightfield
            mask_by_obj_node.parm_value = 2
            mask_by_obj_node.parm_blurradius = 2
            mask_by_obj_node.load_preset(preset_name=preset_name)

            if not is_first_mask:
                hf_combine_prev_node = nodes.geo_nodes.HfCombineMasksNode(ox_parent=self.terrain_node, node_name=f'{user_mask}_hf_prev_combine')
                hf_combine_prev_node.connect_from(ox_node=mask_by_obj_node)
                hf_combine_prev_node.parm_folder0 = 1  # adds a layer
                hf_combine_prev_node = nodes.geo_nodes.HfCombineMasksNode(node=hf_combine_prev_node.node)
                hf_combine_prev_node.parm_layername_1 = self.new_obj_mask_name
                hf_combine_prev_node.parm_mode_1.menu_add

                self.new_obj_mask_name = f'{user_mask}_scatter_mask'
                new_obj_layer_name = f'{user_mask}_scatter_layer'
                hf_copy_layer_node = nodes.geo_nodes.HeightfieldCopylayerNode(ox_parent=self.terrain_node, node_name=new_obj_layer_name)
                hf_copy_layer_node.parm_dstname1 = f'{user_mask}_scatter_mask'
                hf_copy_layer_node.connect_from(ox_node=hf_combine_prev_node)
            else:
                self.new_obj_mask_name = f'{user_mask}_scatter_mask'
                new_obj_layer_name = f'{user_mask}_scatter_layer'
                hf_copy_layer_node = nodes.geo_nodes.HeightfieldCopylayerNode(ox_parent=self.terrain_node, node_name=new_obj_layer_name)
                hf_copy_layer_node.parm_dstname1 = f'{user_mask}_scatter_mask'
                hf_copy_layer_node.connect_from(ox_node=mask_by_obj_node)

            hf_wrangle_node = nodes.geo_nodes.VolumewrangleNode(ox_parent=self.terrain_node, node_name=f'{user_mask}_hf_wrangle')
            hf_wrangle_node.parm_snippet = '@mask=1-@mask;'
            hf_wrangle_node.connect_from(ox_node=hf_copy_layer_node)

            hf_combine = nodes.geo_nodes.HfCombineMasksNode(ox_parent=self.terrain_node, node_name=f'{user_mask}_hf_combine')
            hf_combine.connect_from(ox_node=hf_wrangle_node)
            hf_combine.parm_folder0 = 1  # adds a layer
            hf_combine = nodes.geo_nodes.HfCombineMasksNode(node=hf_combine.node)
            hf_combine.parm_layername_1 = next_mask
            hf_combine.parm_mode_1.menu_minimum

            self.prev_hf_node = hf_combine

    # def create_simple_scatter_node(self, user_mask, prev_hf_node, user_source_points, is_first_mask=False):
    #     prev_hf_node = self.prev_hf_node if self.prev_hf_node else prev_hf_node
    #     name_only = user_mask.replace('_mask', '')
    #     scatter_node = nodes.geo_nodes.HeightfieldScatterNode(ox_parent=self.terrain_node, node_name=f'{user_mask}_hf_scatter')
    #     scatter_node.unlock_node()
    #     scatter_node.parm_keepterrain = False
    #     scatter_node.parm_keepscatterpoints = False
    #     scatter_node.parm_randomyaw = 180
    #     scatter_node.load_preset(preset_name=preset_name)
    #     new_vex_hou_parm = scatter_node.add_string_parameter(name=f'{user_mask}_scat_vex', label=f'{user_mask}_Scatter Point Vex', multiline=True)
    #     scatter_node.add_float_parameter(name='falloff_scalar', label=f'Vex Falloff Scalar', min_f=1, max_f=10)
    #     scatter_node.add_float_parameter(name='pluck_scalar', label=f'Vex Pluck Scalar', min_f=0, max_f=1)
    #     scatter_node.add_float_parameter(name='extra_scalar', label=f'Vex Extra Scalar', min_f=0, max_f=10)
    #     if user_source_points:
    #         source_tag = f'{user_mask}_source_scatter'
    #         source_scatter_node = nodes.geo_nodes.HeightfieldScatterNode(ox_parent=self.terrain_node, node_name=f'{user_mask}_source_scatter')
    #         if is_first_mask:
    #             source_scatter_node.parm_layer = user_mask
    #         source_scatter_node.connect_from(ox_node=prev_hf_node)
    #         source_scatter_node.connect_from(ox_node=prev_hf_node, input_label=source_scatter_node.input_mask_or_scatter_points)
    #         source_scatter_node.parm_coverage = 0.13
    #         source_scatter_node.load_preset(preset_name=f'{preset_name}_source')
    #         scatter_node.connect_from(ox_node=source_scatter_node)
    #         scatter_node.connect_from(ox_node=source_scatter_node, input_label=scatter_node.input_mask_or_scatter_points)
    #         scatter_node.parm_scattermethod.menu_per_point_count_using_source_points
    #         scatter_node.parm_sourcetag = source_tag
    #         scatter_node.parm_outerradius = 0.2
    #         scatter_node.parm_positioning_offsetmax = 2
    #     else:
    #         scatter_node.parm_layer = user_mask
    #         scatter_node.connect_from(ox_node=prev_hf_node, input_label=scatter_node.input_terrain)
    #         scatter_node.connect_from(ox_node=prev_hf_node, input_label=scatter_node.input_mask_or_scatter_points)
    #
    #     # inner vex wrangle:
    #     inner_vex_node = nodes.geo_nodes.AttribwrangleNode(ox_parent=scatter_node, node_name=f'{user_mask}_inner_vex')
    #     inner_vex_node.parm_snippet = new_vex_hou_parm
    #     # get the prev and next inner nodes
    #     prev_inner_hou_node = scatter_node.get_child_by_name('generate_rand_id')
    #     next_inner_hou_node = scatter_node.get_child_by_name('foreach_begin2')
    #     prev_inner_node = OXNode(node=prev_inner_hou_node)
    #     next_inner_node = OXNode(node=next_inner_hou_node)
    #     inner_vex_node.connect_from(prev_inner_node)
    #     next_inner_node.connect_from(inner_vex_node)
    #
    #     import_node = nodes.geo_nodes.ObjectMergeNode(ox_parent=self.terrain_node, node_name=f'{user_mask}_import_from_bridge')
    #     import_node.parm_objpath1 = f'{self.scatter_bridge_node.path}/{f"OUT_{user_mask}"}'
    #     scatter_node.connect_from(ox_node=import_node, input_label=scatter_node.input_primitives_to_instance)

    def create_render_controller(self, user_mask, index, force_override=False, preset_lookup_dict=None):
        scatter_set_name = user_mask.replace('_mask', '')
        preset_name = preset_lookup_dict.get(scatter_set_name, scatter_set_name) if preset_lookup_dict else scatter_set_name
        if force_override:
            self.obj_node.delete_child_node(child_name=f'{user_mask}_controller')
        user_mask_controller_node = self.obj_node.create_node_if_not_exist(
            ox_node_class=nodes.obj_nodes.GeoNode, node_name=f'{user_mask}_controller')  # type: nodes.obj_nodes.GeoNode
        user_mask_controller_node.move_node_relative_to(relative_node=self.terrain_node, y=-(1 + index))
        user_mask_controller_node.parm_rs_objprop_inst_packedpriminstancing = True
        scatter_import_hou_node = user_mask_controller_node.get_child_by_name(child_name=f'{user_mask}_scatter_import')
        if scatter_import_hou_node:
            return
        scatter_import_node = nodes.geo_nodes.ObjectMergeNode(ox_parent=user_mask_controller_node)
        scatter_node_path = f'{self.terrain_node.path}/{user_mask}_hf_scatter'
        scatter_import_node.parm_objpath1 = scatter_node_path
        scatter_import_node.set_render_flag()

        # for matching scatter sets:
        scatter_set_hou_node = self.get_scatter_set_node(scatter_set_name=scatter_set_name)
        if scatter_set_hou_node:
            scatter_set_node = nodes.obj_nodes.GeoNode(node=scatter_set_hou_node)
            merge_node = nodes.geo_nodes.MergeNode(ox_parent=user_mask_controller_node)
            copy_2_points_node = nodes.geo_nodes.CopytopointsNode(ox_parent=user_mask_controller_node)
            copy_2_points_node.parm_useidattrib = True
            copy_2_points_node.connect_from(merge_node, input_label=copy_2_points_node.input_geometry_to_copy)
            copy_2_points_node.connect_from(scatter_import_node, input_label=copy_2_points_node.input_target_points_to_copy_to)
            copy_2_points_node.set_display_flag(include_render_flag=False)

            scatter_set_out_hou_nodes = scatter_set_node.get_children_paths_by_partial_name('OUT')
            for index, variant_out_path in enumerate(scatter_set_out_hou_nodes):
                obj_merge_node = nodes.geo_nodes.ObjectMergeNode(ox_parent=user_mask_controller_node)
                obj_merge_node.parm_objpath1 = variant_out_path
                box_node = nodes.geo_nodes.BoxNode(ox_parent=user_mask_controller_node)
                attr_transfer_node = nodes.geo_nodes.AttribtransferNode(ox_parent=user_mask_controller_node)
                attr_transfer_node.parm_pointattriblist = 'Cd'
                attr_transfer_node.parm_primitiveattribs = False
                attr_transfer_node.connect_from(box_node)
                attr_transfer_node.connect_from(obj_merge_node, input_label=attr_transfer_node.input_geometry_to_transfer_attributes_from)
                match_size_node = nodes.geo_nodes.MatchsizeNode(ox_parent=user_mask_controller_node)
                match_size_node.parm_doscale = True
                match_size_node.connect_from(attr_transfer_node)
                match_size_node.connect_from(obj_merge_node, input_label=match_size_node.input_geometry_whose_bounding_box_is_to_be_matched)
                match_size_node.parm_justify_y.menu_none
                transform_node = nodes.geo_nodes.TransformNode(ox_parent=user_mask_controller_node)
                transform_node.connect_from(match_size_node)
                transform_node.load_preset(preset_name=preset_name)
                attr_create = nodes.geo_nodes.AttribcreateNode(ox_parent=user_mask_controller_node)
                attr_create.parm_name1 = 'variant'
                attr_create.parm_value1v1 = index
                attr_create.connect_from(transform_node)
                merge_node.connect_from(attr_create, input_index=index)

