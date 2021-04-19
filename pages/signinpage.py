from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:

    login_button = ".btn t-500"

    def __init__(self, driver):
        self.driver = driver
        self.login_button = ".btn t-500"
        self.email = "yevhenii.shcherbinin.cr+21@gmail.com"
        self.password = "Pass1234"
        self.username_locator = "email"
        self.password_locator = "password"
        self.button = ".btn btn_block btn-uppercased btn_common btn_auth t-600"
        self.sign_in_toast_locator = 'toast-message'
        self.navigation_locator = 'main-menu'

    def login(self, time = 10):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CLASS_NAME, self.sign_in_toast_locator)),
                                                      message=f"Page {self.sign_in_toast_locator} has not been opened")

    def enter_credentials(self):
        self.driver.find_element(By.NAME, self.username_locator).send_keys(self.email)
        self.driver.find_element(By.NAME, self.password_locator).send_keys(self.password)

    def login_to_app(self, time = 5):
        self.driver.find_element(By.CSS_SELECTOR, self.button).click()
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.navigation_locator)),
            message=f"Failed to login, navigation bar {self.navigation_locator} not found")