from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def get_products_in_basket(self):
        products = []
        for product in self.browser.find_elements(*BasketPageLocators.ITEMS_IN_BASKET):
            products.append(product.text)
        return products