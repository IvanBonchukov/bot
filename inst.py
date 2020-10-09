from time import sleep
from selenium import webdriver

class signUp:

    def __init__(self):
        pass

    def startInsta(self, name,password):
        # запуск браузера
        browser = webdriver.Firefox()
        browser.get('https://www.instagram.com/')
        browser.implicitly_wait(5)

        # вход на страницу
        # name - ("test_testbot")
        # password - ("qwerty12345")

        usernameInput = browser.find_element_by_css_selector("input[name='username']")
        passwordInput = browser.find_element_by_css_selector("input[name='password']")
        usernameInput.send_keys(name)
        passwordInput.send_keys(password)
        loginButton = browser.find_element_by_xpath("//button[@type='submit']")
        loginButton.click()

        browser.implicitly_wait(15)
        sleep(5)

        sign_button = browser.find_element_by_css_selector("button[class = 'sqdOP yWX7d    y3zKF     ']")
        sign_button.click()
        sleep(5)

    def sign(self):
        pass

class instaInteraction:

    #функции для взаемодейтсвие с инстаграмом

    def __init__(self):
        pass

    def goDirect(self):
        pass

    def goHome(self):
        pass

    def goMessage(self):
        pass

    def checkMessage(self):
        pass

    def goProfile(self):
        pass


sUp = signUp()
sUp.startInsta("test_testbot", "qwerty12345")