from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        """Click button add to basket"""
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_item_in_the_basket(self):
        """Checks whether text 'Added to basket' is presented on the page"""
        if not self.is_element_present(*ProductPageLocators.ITEM_ADDED_TEXT):
            assert self.is_element_present(
                *ProductPageLocators.ITEM_ADDED_TEXT), "'Added to basket' message is not presented"
        else:
            item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
            item_add_text = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TEXT)
            assert item_name.text == item_add_text.text, \
                f"Item name '{item_add_text.text}' in message 'added to basket' message is incorrect"

    def should_be_correct_basket_cost(self):
        """Checks whether item's cost in basket is equal item's cost on the Product page"""
        if not self.is_element_present(*ProductPageLocators.BASKET_COST):
            assert self.is_element_present(*ProductPageLocators.BASKET_COST), \
                "'Your basket total' message is not presented"
        else:
            item_cost = self.browser.find_element(*ProductPageLocators.ITEM_COST)
            basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST)
            assert item_cost.text == basket_cost.text, \
                f"Basket cost '{basket_cost.text}' in 'Your basket total' message is incorrect"

    def should_not_be_success_message_item_added_text(self):
        """Checks whether message 'added to basket' is not presented on the page"""
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_TEXT), \
            "Success message \"added to basket\" is presented, but should not be"

    def should_message_disappeared_item_added_text(self):
        """Checks whether text 'added to basket' disappeared"""
        assert not self.is_disappeared(*ProductPageLocators.ITEM_ADDED_TEXT), \
            "Success message \"added to basket\" should disappeared, but it didn't"
