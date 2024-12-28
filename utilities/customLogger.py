import logging


class LogGen:

    @staticmethod
    def loggen():
        path = '.\\logs\\search_feature.log'
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        file_handler = logging.FileHandler(path,mode='w')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        return logger
