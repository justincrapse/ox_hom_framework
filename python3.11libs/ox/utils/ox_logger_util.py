import logging


def set_log_level(level=logging.DEBUG):
    """
    0 - not set
    10 - debug
    20 - info
    30 - warning
    40 - error
    50 - critical
    """
    ox_logger = logging.getLogger("ox_logger")
    ox_logger.setLevel(level)
    for handler in ox_logger.handlers:
        handler.setLevel(level)
