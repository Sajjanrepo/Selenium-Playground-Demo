from selenium.webdriver.common.by import By

class searchbox_and_row_count:
    search_xpath = "//input[@type='search']"
    table_rows_xpath = "//table[@id='example']/tbody/tr"
    confirm_msg_xpath = "//div[@id='example_info']"
    def __init__(self, driver):
        self.driver = driver

    def search(self, search_key):
        self.driver.find_element(By.XPATH, self.search_xpath).send_keys(search_key)

    def row_count(self):
        if self.driver.find_element(By.XPATH,self.confirm_msg_xpath).is_displayed():
            return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))




