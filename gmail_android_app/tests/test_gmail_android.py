import pytest
import time
from appium import webdriver
import unittest

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from gmail_android_app.common.driver_manager import DriverManager
from gmail_android_app.pageobjects.base_test import BaseTest
from gmail_android_app.pageobjects.inbox_page import InboxPage
from gmail_android_app.pageobjects.welcome_page import WelcomePage



@pytest.mark.smoke
class GmailAppTestAndroid():

    def test_gmail_login(self):

        # click 'GOT IT' button in welcome page
        welcomepage = WelcomePage()
        inbox_page = InboxPage(driver=welcomepage.driver)
        welcomepage.click_welcome_tour_got_it()

        # add an email address
        welcomepage.setup_email_address()

        # click Google icon to setup gmail account
        welcomepage.click_google_to_setup_gmail_account()

        # fill in gamil account
        welcomepage.fill_in_email(self.test_accounts[0]["email"])

        # fill in password
        welcomepage.fill_in_password(self.test_accounts[0]["password"])

        # accept some terms
        welcomepage.click_i_agree_button()

        welcomepage.click_more_button()

        welcomepage.click_accept_button()

        # enter Gmail
        welcomepage.click_take_me_to_gmail()

        # click Next button in welcome wizzard
        inbox_page.click_next_in_inbox_page()

        #  click OK button in welcome wizzard
        inbox_page.click_ok_in_inbox_page()

        # click Main menu
        inbox_page.open_main_menu()

        # asseert to enter Gmail box
        self.assertTrue(inbox_page.check_text_of_menu_title("Gmail"), 'not enter Gmail')