from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

game_link = "https://gabrielecirulli.github.io/2048/"
browser = webdriver.Firefox()
browser.get(game_link)

html = browser.find_element_by_tag_name("html")
time.sleep(3)
while True:
    html.send_keys(Keys.UP)
    html.send_keys(Keys.RIGHT)
    html.send_keys(Keys.DOWN)
    html.send_keys(Keys.LEFT)