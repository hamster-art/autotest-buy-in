import time
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_all_elements_located((how, what))
            )
        except TimeoutException:
            return True

        return False

    def is_elements_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_elements_disappeared(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            return False
        return True
