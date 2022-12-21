import re
import logging

ox_logger = logging.getLogger("ox_logger")


def get_str_as_py_var(string_in: str, del_digit=False, lower=True):
    """
    This method takes in a potential python class instance variable name, mainly for auto-generated OX Nodes.
    R2 TODO: review a few generated classes and make some adjustments here, such as what to replace specific non-word characters with
    """
    # lower
    str_lowered = string_in.lower() if lower else string_in
    # clip the wings:
    str_clipped = str_lowered.strip()
    # spaces to underscores:
    str_unders = str_clipped.replace(" ", "_")
    # replace all non-word chars with underscores:
    str_subed = re.sub(r"\W", "_", str_unders)
    if del_digit:
        str_subed = re.sub("\d", "", string_in)
    str_no_first_digit = move_first_digit(string_in=str_subed)
    if str_no_first_digit == "in":
        str_no_first_digit = "inside"
    if str_no_first_digit == "class":
        str_no_first_digit = "class_alt"
    return str_no_first_digit


def get_str_as_class(node_name: str, del_digit=False):
    """similar to get_str_as_py_var, but for a class name. We delete the digit just for ease of use for adding from hou nodes that usually default
    to a name that includes a number (That we don't want)"""
    clean_str = get_str_as_py_var(string_in=node_name, lower=False)
    class_str = "".join([i.title() for i in clean_str.split("_")])
    if del_digit:
        class_str = re.sub(r"\d", "", class_str)
    return class_str


def move_first_digit(string_in: str):
    if string_in[0].isdigit():
        # replace anything that starts with a digit with the same string, but the digit comes after.
        first_pass = re.sub(r"(^\d*)(.*)", r"\2_\1", string_in)
        second_pass = re.sub(
            r"^_*", "", first_pass
        )  # don't want our new string starting with an underscore
        if second_pass[0].isdigit():
            second_pass = f"_{second_pass}"  # here we give up if the second pass still starts with a digit. TODO: come up with better solution
        return second_pass
    return string_in
