import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


@pytest.mark.login_guest
def test_guest_should_see_login_link(browser):
    """Checks whether guest sees login link on the main page"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.login_guest
def test_guest_can_go_to_login_page(browser):
    """Checks whether guest can go to the login page from the main page"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.login_guest
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Checks whether guest sees an empty basket when he opens basket page from the main page"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_basket_is_empty()
