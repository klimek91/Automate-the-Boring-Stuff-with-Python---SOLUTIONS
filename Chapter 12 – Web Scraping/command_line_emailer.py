#!python

from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get(r'https:\\gmail.com')


loginForm = browser.find_element_by_id('identifierId')
loginForm.send_keys(input("Please enter Your email")) #input("Please enter Your email")
dalejButton =  browser.find_element_by_class_name('RveJvd.snByac')
dalejButton.click()

time.sleep(1)
passForm = browser.find_element_by_css_selector('input[type="password"')
passForm.send_keys(input("Please enter Your password")) #input("Please enter Your password")
dalejButton =  browser.find_element_by_class_name('RveJvd.snByac')
dalejButton.click()