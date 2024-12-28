import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + '\\configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getfirefoxdriverpath():
        firefox_driver = config.get('commonInfo', 'geckodriver_path')
        return firefox_driver

    @staticmethod
    def getfirefoxbinarypath():
        firefox_binary = config.get('commonInfo', 'firefox_path')
        return firefox_binary
