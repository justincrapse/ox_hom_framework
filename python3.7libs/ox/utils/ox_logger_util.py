import logging


ox_logger = logging.getLogger('ox_logger')

def set_debug():
    ox_logger.setLevel(logging.DEBUG)

def set_info():
    ox_logger.setLevel(logging.INFO)

def set_warning():
    ox_logger.setLevel(logging.WARNING)