from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FindElement:

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_xpath(self, xpath, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, xpath)),
                                                      message=f"Can't find elements by xpath {xpath}")

    def find_element_by_class(self, clas, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, clas)),
                                                      message=f"Can't find elements by class {clas}")

    def find_element_by_id(self, id, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, id)),
                                                      message=f"Can't find elements by id {id}")
