import logging
from logging.config import fileConfig
from pathlib import Path


class Singleton:
    __instance = None
    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance == None:
            Singleton.__instance = self
            LOGGING_CONFIG = Path(__file__).parent / 'logging_config.ini'
            fileConfig(LOGGING_CONFIG)
        else:
            pass

    def get_logger(self, value):
        logger = logging.getLogger(value)
        return logger
