from pages.product_page import ProductPage
from pages.basket_page import BasketPage



def setup_browser(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    return page


def test_guest_add_product_to_basket(browser):
    """If product name is presented on the basket page, test pass"""
    page = setup_browser(browser)
    page.add_item_to_basket()
    product_name = page.get_product_name()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    products = basket.get_products_in_basket()
    assert product_name in products, \
        f"There is no product named {product_name} in basket"


