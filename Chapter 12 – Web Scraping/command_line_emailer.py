#!python

from selenium import webdriver
import time,sys
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get(r'https:\\gmail.com')

if len(sys.argv) > 4:
    loginForm = browser.find_element_by_id('identifierId')
    loginForm.send_keys(input("Please enter Your email"))
    dalejButton =  browser.find_element_by_class_name('RveJvd.snByac')
    dalejButton.click()

    time.sleep(1)
    passForm = browser.find_element_by_css_selector('input[type="password"]')
    passForm.send_keys(input("Please enter Your password"))
    dalejButton =  browser.find_element_by_class_name('RveJvd.snByac')
    dalejButton.click()

    time.sleep(2)
    sendEmailButton = browser.find_element_by_class_name("T-I.T-I-KE.L3")
    sendEmailButton.click()

    time.sleep(3)
    sendTo = browser.find_element_by_id(":am")
    sendTo.send_keys(sys.argv[1])


    subject = browser.find_element_by_id(":a4")
    subject.send_keys(sys.argv[2])


    text = browser.find_element_by_id(":b9")
    text.send_keys(sys.argv[3])

    send = browser.find_element_by_id(":9u")
    send.click()

    time.sleep(1)
    browser.quit()

