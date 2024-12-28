import pytest

from pageObjects.searchbox_and_row_count import searchbox_and_row_count
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from time import sleep
import os


class Test_Search_Feature:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    Test_Data = [
        # Positive test cases
        ("New York", "5 of 5 entries (filtered from 24 total entries)", "Pass"),

        # Negative test cases
        ("RandomText123", "0 entries out of 24 total entries", "Fail"),
        ("!@#$%^&*", "0 entries out of 24 total entries", "Fail"),
        ("", "0 entries out of 24 total entries", "Fail"),
    ]

    @pytest.mark.parametrize("search_term,expected_result,Result", Test_Data)
    def test_searchbox_and_row_count(self, setup,search_term, expected_result, Result):
        self.logger.info("******* Starting qa_selenium_test **********")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.logger.info("Opening Application")
        self.driver.maximize_window()

        self.logger.info("Performing searchbox operation")
        self.logger.info(f"Showing the result for {search_term}")

        self.num_of_row = searchbox_and_row_count(self.driver)
        self.num_of_row.search(search_term)
        self.result_text = self.num_of_row.row_count()
        sleep(2)

        if expected_result in self.result_text:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "search_box_pass.png")
            self.logger.info(f"{Result} case for input: {search_term}")
            self.logger.info("Closing Browser..........")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "search_box_fail.png")
            self.logger.info(f"{Result} case for input: {search_term}")
            self.logger.info("Closing Browser..........")
            self.driver.close()
            assert False

        self.logger.info("******* End of qa_selenium_test **********")
