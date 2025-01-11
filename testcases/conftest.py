import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from datetime import datetime
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


@pytest.fixture()
def setup():
    logger = LogGen.loggen()
    # Path to your geckodriver and Firefox browser binary
    geckodriver_path = ReadConfig.getfirefoxdriverpath()
    firefox_binary_path = ReadConfig.getfirefoxbinarypath()

    # Set Firefox options to specify binary location
    options = Options()
    options.binary_location = firefox_binary_path

    # Create the Service object with geckodriver path
    serv_obj = Service(geckodriver_path)

    # Initialize WebDriver with service and options
    driver = webdriver.Firefox(service=serv_obj, options=options)

    logger.info("Launching firefox browser.........")

    return driver


# Specifying report folder location and save report with timestamp
@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime(
        "%d-%m-%Y %H-%M-%S") + ".html"
