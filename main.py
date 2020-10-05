from time import sleep
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.instagram.com/')
browser.implicitly_wait(5)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("test_testbot")
password_input.send_keys("qwerty12345")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

browser.implicitly_wait(15)
sleep(5)
sign_button = browser.find_element_by_css_selector("button[class = 'sqdOP yWX7d    y3zKF     ']")
sign_button.click()