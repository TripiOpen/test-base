#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
sys.path.append("/home/lion/tripi/test-base")

# @author: Nguyen Van Do
# @Version: 1.0

def is_browser_console_contain_error_log(webdriver):
    # get browser console log
    # it will return a list of console log if exist
    listOfConsoleLogs = webdriver.get_log('browser')

    if (type(listOfConsoleLogs) is list):
        for log in listOfConsoleLogs:
            if (type(log) is dict) and (log['level'] == 'SEVERE'):
                    print log
                    return True
    return False
    