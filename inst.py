from time import sleep
from selenium import webdriver

class signUp:

    browser = webdriver.Firefox()

    def __init__(self):
        pass

    def startInsta(self, name,password):
        # запуск браузера
        self.browser.get('https://www.instagram.com/')
        self.browser.implicitly_wait(5)

        # вход на страницу
        # name - ("test_testbot")
        # password - ("qwerty12345")

        usernameInput = self.browser.find_element_by_css_selector("input[name='username']")
        passwordInput = self.browser.find_element_by_css_selector("input[name='password']")
        usernameInput.send_keys(name)
        passwordInput.send_keys(password)
        loginButton = self.browser.find_element_by_xpath("//button[@type='submit']")
        loginButton.click()

        self.browser.implicitly_wait(15)
        sleep(5)

        sign_button = self.browser.find_element_by_css_selector("button[class = 'sqdOP yWX7d    y3zKF     ']")
        sign_button.click()
        sleep(3)

    def sign(self):
        pass

class instaInteraction(signUp):

    #функции для взаемодейтсвия с инстаграмом

    def goDirect(self):
        directButton = signUp.browser.find_element_by_css_selector("a[class = 'xWeGp']")
        directButton.click()
        sleep(3)

    def goHome(self):
        homeButton = signUp.browser.find_element_by_css_selector("div[class = 'cq2ai']")
        homeButton.click()
        sleep(3)

    def goProfile(self):
        #ProfileButton = signUp.browser.find_element_by_css_selector("div[class = 'cq2ai']")
        #ProfileButton.click()
        #sleep(3)
        pass

    def goMessage(self):
        messageButton = self.browser.find_element_by_xpath("//a[@class = '-qQT3 rOtsg']")
        messageButton.click()

    def checkMessage(self):
        pass

instInter = instaInteraction()
sUp = signUp()
sUp.startInsta("test_testbot", "qwerty12345")
instInter.goDirect()
#instInter.goHome()
instInter.goMessage()