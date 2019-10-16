import pytest
import time
from appium import webdriver
import unittest

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.smoke
class GmailAppTestAndroid(unittest.TestCase):

    # define and start driver
    def test_gmail_login(self):
        caps = {
            "deviceName": "Pixel 2 API 29",
            "platformName": "Android",
            "appPackage": "com.google.android.gm",
            "appActivity": "ConversationListActivityGmail",
            "appiumVersion": "1.13.0",
            "deviceOrientation": "portrait",
            "deviceType": "phone",
            "newCommandTimeout": 600,
            "platformVersion": "10",
            "app": "/Users/mingli/autotestestexercise/mobile-test-scripts/gmail_android_app/resources/applications/android/gmail.apk",
            "autoGrantPermissions": True
        }

        driver = webdriver.Remote(desired_capabilities=caps,
                                  command_executor='http://127.0.0.1:4723/wd/hub')

        # click 'GOT IT' button in welcome page
        driver.find_element_by_id("com.google.android.gm:id/welcome_tour_got_it").click()

        # add an email address
        driver.find_element_by_id("com.google.android.gm:id/setup_addresses_add_another").click()

        # click Google icon to setup gmail account
        driver.find_element_by_xpath("//*[@text='Google']").click()

        WebDriverWait(driver, 60, ignored_exceptions=[StaleElementReferenceException]).\
            until(expected_conditions.visibility_of_element_located((By.ID,"identifierId")))

        # fill in gamil account
        driver.find_element_by_id("identifierId").send_keys("kemanli137@gmail.com")

        driver.find_element_by_id("identifierNext").click()

        WebDriverWait(driver, 30, ignored_exceptions=[StaleElementReferenceException]).until(
            expected_conditions.visibility_of_element_located((By.ID, "password")))

        # fill in password
        driver.find_element_by_id("password").send_keys("901()!qwe")

        driver.find_element_by_id("passwordNext").click()

        WebDriverWait(driver, 30, ignored_exceptions=[StaleElementReferenceException]).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[@text='I agree']")))

        # accept some terms
        driver.find_element_by_xpath("//*[@text='I agree']").click()

        WebDriverWait(driver, 30, ignored_exceptions=[StaleElementReferenceException]).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[@text='MORE']")))

        driver.find_element_by_xpath("//*[@text='MORE']").click()

        WebDriverWait(driver, 30, ignored_exceptions=[StaleElementReferenceException]).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[@text='ACCEPT']")))

        driver.find_element_by_xpath("//*[@text='ACCEPT']").click()


        # enter Gmail
        WebDriverWait(driver, 30, ignored_exceptions=[StaleElementReferenceException]).until(
            expected_conditions.visibility_of_element_located((By.XPATH,"//*[@text='TAKE ME TO GMAIL']")))

        driver.find_element_by_xpath("//*[@text='TAKE ME TO GMAIL']").click()

        try:
            WebDriverWait(driver, 10, ignored_exceptions=[StaleElementReferenceException]).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//*[@text='OK']")))

            time.sleep(1)
            driver.find_element_by_xpath("//*[@text='OK']").click()

            WebDriverWait(driver, 30, ignored_exceptions=[StaleElementReferenceException]).until(
                expected_conditions.visibility_of_element_located((By.XPATH,"//*[@text='TAKE ME TO GMAIL']")))

            time.sleep(1)
            driver.find_element_by_xpath("//*[@text='TAKE ME TO GMAIL']").click()
        except NoSuchElementException as e:
            print(e)

        WebDriverWait(driver, 30, ignored_exceptions=[StaleElementReferenceException]).\
            until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@text='Next']")))

        # click Next button in welcome wizzard
        driver.find_element_by_xpath("//*[@text='Next']").click()

        WebDriverWait(driver, 30, ignored_exceptions=[StaleElementReferenceException]).\
            until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@text='OK']")))

        #  click OK button in welcome wizzard
        driver.find_element_by_xpath("//*[@text='OK']").click()

        WebDriverWait(driver, 30, ignored_exceptions=[StaleElementReferenceException]).\
            until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.ImageButton[@content-desc='Open navigation drawer']")))

        # click Main menu
        driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Open navigation drawer']").click()

        WebDriverWait(driver, 30, ignored_exceptions=[StaleElementReferenceException]).\
            until(expected_conditions.visibility_of_element_located((By.ID, "com.google.android.gm:id/conversation_list_folder_header")))

        driver.find_element_by_xpath("//*[@content-desc='Gmail']")

        # asseert to enter Gmail box
        self.assertTrue(driver.find_element_by_xpath("//*[@text='Gmail']").text == 'Gmail', "not enter Gmail")
