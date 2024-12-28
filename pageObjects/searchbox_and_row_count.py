from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class searchbox_and_row_count:
    search_xpath = "//input[@type='search']"
    # table_rows_xpath = "//table[@id='example']/tbody/tr"
    confirm_msg_xpath = "//*[@id='example_info']"

    def __init__(self, driver):
        self.driver = driver

    def search(self, search_key):
        self.driver.find_element(By.XPATH, self.search_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_xpath).send_keys(search_key)

    def row_count(self):
        results_text = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.confirm_msg_xpath))).text
        return results_text
