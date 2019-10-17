from selenium.webdriver.common.by import By

from gmail_android_app.common.utilities import click_element, wait_for_element
from gmail_android_app.pageobjects.basic_page import BasicPage


class InboxPage(BasicPage):

    def click_next_in_inbox_page(self):
        click_element(self.driver, (By.XPATH, "//*[@text='Next']"))

    def click_ok_in_inbox_page(self):
        click_element(self.driver, (By.XPATH, "//*[@text='OK']"))

    def open_main_menu(self):
        click_element(self.driver, (By.XPATH,"//android.widget.ImageButton[@content-desc='Open navigation drawer']"))

    def check_text_of_menu_title(self, expected_text):
        wait_for_element(self.driver, (By.XPATH, "//*[@text='Gmail']"))
        actual_title_text = self.driver.find_element_by_xpath("//*[@text='Gmail']").text
        return actual_title_text == expected_text
