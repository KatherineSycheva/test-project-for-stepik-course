import pytest

from pages.locators import LoginPageLocators
from pages.login_page import LoginPage
from service.UserCreator import UserCreator


def setup_page(browser):
    page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
    page.open()
    return page


def test_guest_see_login_form(browser):
    """Checks whether login form is presented on the page"""
    login_page = setup_page(browser)
    assert login_page.is_element_present(*LoginPageLocators.LOGIN_FORM), \
        "Login form is not presented"


def test_guest_see_register_form(browser):
    """Checks whether register form is presented on the page"""
    login_page = setup_page(browser)
    assert login_page.is_element_present(*LoginPageLocators.REGISTER_FORM), \
        "Register form is not presented"


def test_register_new_user(browser):
    """New user registration test. Should be message about success registration"""
    user = UserCreator.with_credentials_from_property()
    login_page = setup_page(browser)
    login_page.register_new_user(user)
    assert login_page.is_element_present(*LoginPageLocators.MESSAGE_SUCCESS), \
        f"Can't registrate user {user.name}"


def test_login_user(browser):
    """Login registered user"""
    user = UserCreator.with_credentials_from_property()
    login_page = setup_page(browser)
    login_page.login(user)
    assert login_page.is_element_present(*LoginPageLocators.MESSAGE_SUCCESS), \
        f"Can't login user {user.name}"
