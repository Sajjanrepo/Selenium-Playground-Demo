from pageObjects.searchbox_and_row_count import searchbox_and_row_count
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from time import sleep
import os


class Test_Search_Feature:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    key = "New York"

    def test_searchbox_and_row_count(self, setup):
        self.logger.info("******* Starting qa_selenium_test **********")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.logger.info("Opening Application")
        self.driver.maximize_window()

        self.logger.info("Performing searchbox operation")
        self.logger.info(f"Calculating number of rows for {self.key}")

        self.num_of_row = searchbox_and_row_count(self.driver)
        self.num_of_row.search(self.key)
        self.total_row = self.num_of_row.row_count()
        sleep(2)

        if self.total_row == 5:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "search_box_pass.png")
            self.logger.info(f"Number of rows Equal to {self.total_row}")
            self.logger.info("Test Case Passed")
            self.logger.info("Closing Browser..........")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "search_box_fail.png")
            self.logger.info(f"Number of rows Equal to {self.total_row}")
            self.logger.error("The test case failed")
            self.logger.info("Closing Browser..........")
            self.driver.close()
            assert False

        self.logger.info("******* End of qa_selenium_test **********")
