from selenium import webdriver
from selenium.webdriver.common.by import By


class Menu:
    navigation_menu_locator = '//*[@id="path-1"]'
    account_profile_locator = '//*[@id="gatsby-focus-wrapper"]/div/header/div/div[2]/div[2]/a[1]'
    bookings_locator = '//*[@id="gatsby-focus-wrapper"]/header/div/div[2]/div[2]/a[2]'
    settings_locator = '//*[@id="gatsby-focus-wrapper"]/header/div/div[2]/div[2]/a[3]'
    settings_password_locator = '//*[@id="gatsby-focus-wrapper"]/main/div/div/div[2]/div[1]/div/a[2]'
    settings_profile_locator = '//*[@id="gatsby-focus-wrapper"]/main/div/div/div[2]/div[1]/div/a[3]'
    sign_in_locator = '//*[@id="gatsby-focus-wrapper"]/div/header/div/div[4]/a[1]'

    navigation_menu_url = "https://dev.koralgo.com/search"
    account_profile_url = "https://dev.koralgo.com/customers/search-profile"
    bookings_url = "https://dev.koralgo.com/customers/bookings"
    settings_url = "https://dev.koralgo.com/customers/settings/email"
    settings_password_url = "https://dev.koralgo.com/customers/settings/password"
    settings_profile_url = "https://dev.koralgo.com/customers/settings/profile-info"
    sign_in_url = "https://dev.koralgo.com/signin/"

    def __init__(self, driver):
        self.driver = driver

    def page_switches(self, tablocator, tablink):
        self.driver.find_element(By.XPATH, tablocator).click()
        url = self.driver.current_url
        assert tablink == url, ('Transition to ' + str(tablink) + ' not happened!')
