from selenium.webdriver.common.by import By

from gmail_android_app.common.utilities import click_element, wait_for_element
from gmail_android_app.pageobjects.basic_page import BasicPage

next_button_xpath = "//*[@text='Next']"
ok_button_xpath = "//*[@text='OK']"
main_menu_xpath = "//android.widget.ImageButton[@content-desc='Open navigation drawer']"
title_main_menu_xpath = "//*[@text='Gmail']"


class InboxPage(BasicPage):

    def click_next_in_inbox_page(self):
        click_element(self.driver, (By.XPATH, next_button_xpath))

    def click_ok_in_inbox_page(self):
        click_element(self.driver, (By.XPATH, ok_button_xpath))

    def open_main_menu(self):
        click_element(self.driver, (By.XPATH, main_menu_xpath))

    def check_text_of_menu_title(self, expected_text):
        wait_for_element(self.driver, (By.XPATH, title_main_menu_xpath))
        actual_title_text = self.driver.find_element_by_xpath(title_main_menu_xpath).text
        return actual_title_text == expected_text
