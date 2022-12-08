"""
these are defaults and should not be added to here. place and load your own defaults someplace else. these will load whenever ox is imported.
"""
import logging


from ox.constants.ox_conf import sesh_vars
from ox.utils import session_utils
from ox.utils.ox_logger_util import *
from ox.base_objects.ox_node import OXNode

session_utils.set_session_variable(var_name=sesh_vars.LOAD_USER_PRESETS, value=True)
ox_logger = logging.getLogger("ox_logger")
ox_log_handler = logging.StreamHandler()
ox_log_handler.setLevel(logging.WARNING)
ox_log_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
ox_log_handler.setFormatter(ox_log_formatter)
ox_logger.addHandler(ox_log_handler)
ox_logger.setLevel(logging.WARNING)
