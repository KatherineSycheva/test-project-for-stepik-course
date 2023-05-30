from .base_page import BasePage
from .basket_page import BasketPage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        """Click button add to basket"""
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_to_basket_button.click()

    def click_basket_button(self):
        """Click button 'see basket'"""
        basket_button = self.browser.find_element(*ProductPageLocators.SEE_BASKET_BUTTON)
        basket_button.click()

    def get_product_name(self):
        """Returns the name of product"""
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
