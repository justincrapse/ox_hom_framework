"""
these are defaults and should not be added to here. place and load your own defaults someplace else. these will load whenever ox is imported.
"""
import logging


from ox.constants.ox_conf import sesh_vars
from ox.utils import session_utils
from ox.utils.ox_logger_util import *

session_utils.set_session_variable(var_name=sesh_vars.LOGGING_LEVEL, value=logging.WARNING)
session_utils.set_session_variable(var_name=sesh_vars.LOAD_USER_PRESETS, value=True)
ox_logger = logging.getLogger("ox_logger")
# ox_logger.addHandler(logging.StreamHandler())
