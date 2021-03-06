from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url, f"URL address {self.url} of Login page is incorrect"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        e = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_EMAIL)
        e.send_keys(email)
        pas1 = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_PASSWORD1)
        pas1.send_keys(password)
        pas2 = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_PASSWORD2)
        pas2.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_BUTTON_SUBMIT)
        button_submit.click()





