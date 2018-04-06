#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import sys
sys.path.append(os.getcwd())

# @author: Nguyen Van Do
# @Version: 1.0

import unittest

from selenium import webdriver
from time import sleep
from utils import is_browser_console_contain_error_log
class TestBase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/home/lion/tripi/test-base/chromedriver")

    def tearDown(self):
        self.driver.close()

    def load_page(self, url):
        self.driver.get(url)
        sleep(1)

    def check_browser_console_error(self):
        self.assertFalse(is_browser_console_contain_error_log(self.driver))

    # Utils functions
    def click_xpath(self, xpath):
        self.button = self.driver.find_element_by_xpath(xpath)
        self.button.click()
        sleep(2)
        return self.button

    def scroll_page(self, toElement):
        self.driver.execute_script("")

    
