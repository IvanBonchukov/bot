
import re
from time import sleep
from selenium import webdriver

token = "864094920:AAH78Le5rQdNcZmsMpDHg8XHnEaVx0oCs1I" #"622233587:AAG6fg0yuZ7Zr4kj1E7yCEJcqxIogI1L_sk"
id = "538771062"


browser = webdriver.Firefox()
browser.get('https://web.telegram.org/#/login')
browser.implicitly_wait(5)

username_input = browser.find_element_by_css_selector("input[name='username']")
username_input.send_keys("test_testbot")