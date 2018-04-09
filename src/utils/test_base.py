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
from selenium.webdriver.common.action_chains import ActionChains

from utils import is_browser_console_contain_error_log

class TestBase(unittest.TestCase):

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument("--test-type")
        self.driver = webdriver.Chrome("E:\\Examples\\test-base\\chromedriver.exe", chrome_options=self.options)

    def tearDown(self):
        self.driver.close()

    def load_page(self, url):
        self.driver.fullscreen_window()
        sleep(2)
        self.driver.get(url)
        sleep(2)

    def check_browser_console_error(self):
        self.assertFalse(is_browser_console_contain_error_log(self.driver))

    # Utils functions
    def click_xpath(self, xpath):
        self.button = self.driver.find_element_by_xpath(xpath)
        self.button.click()
        sleep(2)

    def click_class(self, className, index):
        self.element = self.driver.find_elements_by_class_name(className)[index]
        self.element.click()
        sleep(2)

    def send_input_class(self, className, values):
        self.element = self.driver.find_elements_by_class_name(className)[0]
        ActionChains(self.driver).send_keys_to_element(self.element, values).perform()
        sleep(2)
        
    def send_input_xpath(self, xpath, values):
        self.element = self.driver.find_element_by_xpath(xpath)
        ActionChains(self.driver).send_keys_to_element(self.element, values).perform()
        sleep(2)

    def scroll_page(self, xpath):
        self.element = self.driver.find_element_by_xpath(xpath)
        self.driver.fullscreen_window()
        ActionChains(self.driver).move_to_element(self.element).perform()
        sleep(2)

