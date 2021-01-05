from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    # Проверка сообщения о том, что товар добавлен в корзину.
    # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили
    def should_be_correct_item_in_the_basket(self):
        if self.is_element_present(*ProductPageLocators.ITEM_ADDED_TEXT) == False:
            assert self.is_element_present(
                *ProductPageLocators.ITEM_ADDED_TEXT), "'Added to basket' message is not presented"
        else:
            item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
            item_add_text = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TEXT)
            assert item_name.text == item_add_text.text, f"Item name '{item_add_text.text}' in message 'added to basket' message is incorrect"


    # Стоимость корзины совпадает с ценой товара.
    def should_be_correct_basket_cost(self):
        if self.is_element_present(*ProductPageLocators.BASKET_COST) == False:
            assert self.is_element_present(*ProductPageLocators.BASKET_COST), "'Your basket total' message is not presented"
        else:
            item_cost = self.browser.find_element(*ProductPageLocators.ITEM_COST)
            basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST)
            assert item_cost.text == basket_cost.text, f"Basket cost '{basket_cost.text}' in 'Your basket total' message is incorrect"


