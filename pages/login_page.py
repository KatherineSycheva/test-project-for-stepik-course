from model.User import User
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, browser, url):
        super(LoginPage, self).__init__(browser, url)

    def register_new_user(self, user: User):
        """Registration of a new user"""
        new_user_email = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_EMAIL)
        new_user_email.send_keys(user.name)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_PASSWORD1)
        password1.send_keys(user.password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_PASSWORD2)
        password2.send_keys(user.password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_BUTTON_SUBMIT)
        button_submit.click()

    def login(self, user: User):
        """Login with existing user"""
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(user.name)
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(user.password)
        button_enter = self.browser.find_element(*LoginPageLocators.ENTER_BUTTON)
        button_enter.click()





