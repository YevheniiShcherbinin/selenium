from signinpage import *
from headernavigation import *
from navigation import *
from findelement import *
from selenium import webdriver
import pytest


class testcase:

    def koralgotest(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://dev.koralgo.com/")

    def logintest(self):
        login = Login(driver)
        login.login()
        login.enter_credentials()
        login.login_to_app()


        nav_bar = Menu(driver)
        nav_bar.tabs_transitions(Menu.messages_locator, Menu.messaging_url)


        topmenu = Header_navigation(driver)
        topmenu.topmenu_opening()
        topmenu.Log_out()

        driver.quit()


if __name__ == "__main__":
    pytest.koralgotest(self=test())
    pytest.logintest(self=test())
