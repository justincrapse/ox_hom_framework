from hou_helper.utils.gen_classes import gen_node_classes as class_gen

import hou

obj_node = hou.node('/obj')
geo_node = obj_node.createNode('geo')
matnet_node = obj_node.createNode('matnet')
redshift_vopnet_node = matnet_node.createNode('redshift_vopnet')

root_node_list = [
    'obj',
]

obj_node_list = [
    'geo',
    'matnet',
]

geo_node_list = [
    'file',
    'unpack',
    'xform',
    'material'
]

matnet_node_list = [
    'redshift_vopnet'
]

redshift_node_list = [
    'redshift::Material',  # shader
    'redshift_material',  # end node
    'redshift::RSColorLayer',
    'redshift::TextureSampler',
    'redshift::BumpMap',
    'redshift::Displacement',
]


def populate_obj_node_classes():
    sub_dir = '../nodes/obj_nodes'
    for node_type in obj_node_list:
        print(f'node type: {node_type}')
        node = obj_node.createNode(node_type)
        class_gen.generate_node_class(node=node, sub_dir=sub_dir)


def populate_geo_node_classes():
    sub_dir = '../nodes/geo_nodes'
    for node_type in geo_node_list:
        node = geo_node.createNode(node_type)
        class_gen.generate_node_class(node=node, sub_dir=sub_dir)


def populate_matnet_node_classes():
    sub_dir = '../nodes/matnet_nodes'
    for node_type in matnet_node_list:
        node = matnet_node.createNode(node_type)
        class_gen.generate_node_class(node=node, sub_dir=sub_dir)


def populate_redshift_node_classes():
    sub_dir = '../nodes/redshift_nodes'
    for node_type in redshift_node_list:
        print(f'rs node pop: {node_type}')
        node = redshift_vopnet_node.createNode(node_type)
        class_gen.generate_node_class(node=node, sub_dir=sub_dir)


def populate_all_node_classes():
    populate_geo_node_classes()
    populate_obj_node_classes()
    populate_matnet_node_classes()
    populate_redshift_node_classes()

