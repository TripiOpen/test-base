# @author: Nguyen Van Do
# @Version: 1.0

import unittest

from selenium import webdriver
from time import sleep
from utils import is_browser_console_contain_error_log

class TestBase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        try:
            self.check_browser_console_error()
        except Exception:
            raise
        finally:
            self.driver.close()

    def load_page(self, url):
        self.driver.get(url)
        sleep(1)
        self.check_browser_console_error()

    def check_browser_console_error(self):
        self.assertFalse(is_browser_console_contain_error_log(self.driver))
