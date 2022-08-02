import logging


def set_log_level(level=logging.DEBUG):
    ox_logger = logging.getLogger("ox_logger")
    ox_logger.setLevel(level)
    for handler in ox_logger.handlers:
        handler.setLevel(level)
