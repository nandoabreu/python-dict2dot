#! /usr/bin/env python
import logging


class Logger:
    def __init__(self, name: str = 'dict2dot.Dict2Dot', log_level: str = 'DEBUG'):
        logging.basicConfig(format='%(asctime)s %(name)s:%(lineno)-3d [%(levelname)s] %(message)s')
        logger = logging.getLogger(name)
        logger.setLevel(log_level)

        self.logger = logger

    def get_logger(self):
        return self.logger
