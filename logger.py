import os
import logging


def init_logger():
    global logger
    level = logging.DEBUG if os.environ.get('DEBUG', False) else logging.INFO
    logging.basicConfig(
        level=level, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger()


logger = init_logger()
