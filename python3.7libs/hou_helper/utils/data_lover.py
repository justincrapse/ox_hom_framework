import re


def get_str_as_py_var(string_in: str, del_digit=False, lower=True):
    # lower
    str_lowered = string_in.lower() if lower else string_in
    # clip the wings:
    str_clipped = str_lowered.strip()
    # spaces to underscores:
    str_unders = str_clipped.replace(' ', '_')
    # replace all non-word chars with underscores:
    str_subed = re.sub(r'\W', '_', str_unders)
    if del_digit:
        str_subed = re.sub('\d', '', string_in)
    str_no_first_digit = move_first_digit(string_in=str_subed)
    if str_no_first_digit == 'in':
        str_no_first_digit = 'inside'
    if str_no_first_digit == 'class':
        str_no_first_digit = 'class_alt'
    return str_no_first_digit


def get_str_as_class(node_name: str, del_digit=False):
    clean_str = get_str_as_py_var(string_in=node_name, lower=False)
    class_str = ''.join([i.title() for i in clean_str.split('_')])
    if del_digit:
        class_str = re.sub(r'\d', '', class_str)
    return class_str


def move_first_digit(string_in: str):
    if string_in[0].isdigit():
        first_pass = re.sub(r'(^\d*)(.*)', r'\2_\1', string_in)
        second_pass = re.sub(r'^_*', '', first_pass)
        return second_pass
    return string_in
