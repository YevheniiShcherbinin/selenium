from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import signinpage


class Header_navigation:

    def __init__(self, driver):

        self.driver = driver
        self.search_locator = '//*[@id="gatsby-focus-wrapper"]/div/header/div/button/svg/path'
        self.LogOut_locator = '//*[@id="gatsby-focus-wrapper"]/div/headerdiv/div[4]'
        self.sign_in_locator = signinpage.Login.login_button

    def Go_to_search(self, time = 10):
        self.driver.find_element(By.XPATH, self.search_locator).click()
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, self.LogOut_locator)),
                                                      message=f"Search {self.search_locator} has not been opened")
    def Log_out(self, time = 10):
        self.driver.find_element(By.XPATH, self.LogOut_locator).click()
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.sign_in_locator)),
                                                      message=f"Failed to logout via {self.sign_in_locator}")
