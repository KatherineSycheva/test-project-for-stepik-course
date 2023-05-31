import pytest

from pages.locators import MainPageLocators, BasketPageLocators
from pages.main_page import MainPage
from pages.basket_page import BasketPage


def setup_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    return page


@pytest.mark.login_guest
def test_guest_sees_login_link(browser):
    """Checks whether guest sees login link on the main page"""
    main_page = setup_page(browser)
    assert main_page.is_element_present(*MainPageLocators.LOGIN_LINK), \
        f"Login link isn't presented on the page"


@pytest.mark.login_guest
def test_guest_goes_to_login_page(browser):
    """Checks whether guest can go to the login page from the main page"""
    main_page = setup_page(browser)
    main_page.go_to_login_page()
    assert "login" in browser.current_url, \
        f"URL address {browser.current_url} of Login page is incorrect"