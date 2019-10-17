from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

DEFAULT_TIMEOUT = 30

def click_element(driver, locator, timeout=DEFAULT_TIMEOUT):
    if not isinstance(locator, WebElement):
        element = wait_for_element_clickable(driver, locator, timeout)
    else:
        element = locator

    try:
        element.click()
        return element
    except TimeoutException as e:
        print(str(e))

def wait_for_element_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout, ignored_exceptions=[StaleElementReferenceException]).until(
        expected_conditions.element_to_be_clickable(locator))

def wait_for_element(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout, ignored_exceptions=[StaleElementReferenceException]).until(
        expected_conditions.presence_of_element_located(locator))
