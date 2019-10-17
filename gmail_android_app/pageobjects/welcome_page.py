import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from gmail_android_app.common.utilities import click_element, wait_for_element
from gmail_android_app.pageobjects.basic_page import BasicPage


class WelcomePage(BasicPage):

    def click_welcome_tour_got_it(self):
        self.driver.find_element_by_id("com.google.android.gm:id/welcome_tour_got_it").click()

    def setup_email_address(self):
        self.driver.find_element_by_id("com.google.android.gm:id/setup_addresses_add_another").click()

    def click_google_to_setup_gmail_account(self):
        self.driver.find_element_by_xpath("//*[@text='Google']").click()

    def fill_in_email(self, account):
        wait_for_element(self.driver, (By.ID, "identifierId"))
        self.driver.find_element_by_id("identifierId").send_keys(account)
        click_element(self.driver, (By.ID, "identifierNext"))

    def fill_in_password(self, passwd):
        wait_for_element(self.driver, (By.ID, "password"))
        self.driver.find_element_by_id("password").send_keys(passwd)
        click_element(self.driver,(By.ID, "passwordNext"))

    def click_i_agree_button(self):
        click_element(self.driver, (By.XPATH, "//*[@text='I agree']"))

    def click_more_button(self):
        click_element(self.driver, (By.XPATH, "//*[@text='MORE']"))

    def click_accept_button(self):
        click_element(self.driver, (By.XPATH, "//*[@text='ACCEPT']"))

    def click_take_me_to_gmail(self):
        click_element(self.driver, (By.XPATH, "//*[@text='TAKE ME TO GMAIL']"))
        try:
            click_element(self.driver, (By.XPATH, "//*[@text='OK']"), 10)
            #hard code for flake issue - have to wait for 1 second
            time.sleep(1)

            click_element(self.driver, (By.XPATH, "//*[@text='TAKE ME TO GMAIL']"), 10)
            #hard code for flake issue - have to wait for 1 second
            time.sleep(1)
        except TimeoutException as e:
            print(e)
