#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
sys.path.append("/home/lion/tripi/test-base")

import unittest

from time import sleep

from src.utils.test_base import TestBase

class HomeScreenTest(TestBase):

    def test1_load_title(self):
        self.load_page("https://www.tripi.vn/")
        self.assertEqual(self.driver.title.encode('utf-8'), "Tripi.vn - Đặt vé máy bay và khách sạn thuận tiện với giá tốt nhất", "title failed")

    def test2_find_ticket(self):
        self.load_page("https://vnexpress.net/")
        # self.driver.fullscreen_window()
        submit_button = self.driver.find_elements_by_xpath("[//input[@name='btnK']")[0]
        
        sleep(2)

if __name__ == "__main__":
    SUITE = unittest.TestLoader().loadTestsFromTestCase(HomeScreenTest)
    unittest.TextTestRunner(verbosity=2).run(SUITE)