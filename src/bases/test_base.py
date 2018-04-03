# @author: Nguyen Van Do
# @Version: 1.0

import unittest

from selenium import webdriver
from utils import is_browser_console_contain_error_log

class TestBase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def load_page(self, url):
        pass

    def check_browser_console_error(self):
        self.assertFalse(is_browser_console_contain_error_log(self.driver))
