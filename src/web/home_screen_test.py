#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
sys.path.append("E:\\Examples\\test-base")

import unittest

from time import sleep

from src.utils.test_base import TestBase

class HomeScreenTest(TestBase):

    # def test1_load_title(self):
    #     self.load_page("https://www.tripi.vn/")
    #     self.assertEqual(self.driver.title.encode('utf-8'), "Tripi.vn - Đặt vé máy bay và khách sạn thuận tiện với giá tốt nhất", "title failed")

    # def test2_find_ticket(self):
    #     self.load_page("https://www.tripi.vn/")
    #     self.button = self.driver.find_elements_by_xpath('//*[@id="homepage-tripi-search-form"]/form/div[6]/button')[0]
    #     self.button.click()
    #     sleep(2)

    # def test3_scroll_middle_page(self):
    #     self.load_page("https://www.tripi.vn/")
    #     self.scroll_page('//*[@id="where-do-you-go"]/div[1]/span')
    #     sleep(2)

    def test4_find_ticket(self):
        self.load_page("https://www.tripi.vn/")
        self.click_xpath('//*[@id="header-v2-main-menu"]/div/a[3]')
        self.click_xpath('//*[@id="select-user-location"]/div[1]/div/div[1]/img')
        self.click_xpath('//*[@id="flight-to-airport-value"]')
        self.click_xpath('//*[@id="flight-to-airport"]/div/div/ul[2]/div/li[6]')
        self.click_xpath('//*[@id="round-trip"]')
        self.click_xpath('//*[@id="banner-v110"]/div[1]/div[2]/div[2]/div/form/div[7]/button')
        sleep(10)
        self.click_class('flight-select-single-ticket', 0)
        self.click_class('flight-select-return-ticket', 1)
        self.click_class('flight-add-payment-info', 0)
        sleep(5)
        # send values
        self.send_input_xpath('//*[@id="adult-0"]/div[1]/div/input', "Nguyen")
        self.send_input_xpath('//*[@id="adult-0"]/div[2]/div/input', "Van Do")
        # gender
        self.click_xpath('//*[@id="adult-0"]/div[3]/div/select')
        self.click_xpath('//*[@id="adult-0"]/div[3]/div/select/option[2]')
        # day
        self.click_xpath('//*[@id="adult-0"]/div[4]/div/div/select[1]')
        self.click_xpath('//*[@id="adult-0"]/div[4]/div/div/select[1]/option[5]')
        # month
        self.click_xpath('//*[@id="adult-0"]/div[4]/div/div/select[2]')
        self.click_xpath('//*[@id="adult-0"]/div[4]/div/div/select[2]/option[3]')
        # year
        self.click_xpath('//*[@id="adult-0"]/div[4]/div/div/select[3]')
        self.click_xpath('//*[@id="adult-0"]/div[4]/div/div/select[3]/option[28]')

        self.click_xpath('//*[@id="adult-0"]/div[1]/select')
        self.click_xpath('//*[@id="adult-0"]/div[1]/select/option[2]')
        self.click_xpath('//*[@id="adult-0"]/div[2]/select')
        self.click_xpath('//*[@id="adult-0"]/div[2]/select/option[2]')
        
        self.click_xpath('//*[@id="ticket-booking-select-title"]')
        self.click_xpath('//*[@id="ticket-booking-select-title"]/option[2]')

        self.send_input_xpath('//*[@id="contact-info"]/div[1]/div[2]/div/input', "Nguyen")
        self.send_input_xpath('//*[@id="contact-info"]/div[1]/div[3]/div/input', "Van Do")
        self.send_input_xpath('//*[@id="contact-info"]/div[2]/div[1]/div/input', "do.nguyen@tripi.vn")
        self.send_input_xpath('//*[@id="contact-info"]/div[2]/div[2]/div/input', "0968208244")

        self.click_xpath('//*[@id="flight-guest-info"]/div/div[1]/div[6]/div[2]/div/div[2]/div')
        self.click_xpath('//*[@id="flight-guest-info"]/div/div[1]/div[7]/div/button')

if __name__ == "__main__":
    SUITE = unittest.TestLoader().loadTestsFromTestCase(HomeScreenTest)
    unittest.TextTestRunner(verbosity=2).run(SUITE)