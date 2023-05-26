from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        """Checks whether login page has necessary forms"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Checks whether url correct (should be 'login' in url)"""
        assert "login" in self.url, f"URL address {self.url} of Login page is incorrect"

    def should_be_login_form(self):
        """Checks whether login form is presented on the page"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """Checks whether register form is presented on the page"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        """Registration of a new user"""
        new_user_email = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_EMAIL)
        new_user_email.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_PASSWORD1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_PASSWORD2)
        password2.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER_NEW_USER_BUTTON_SUBMIT)
        button_submit.click()





