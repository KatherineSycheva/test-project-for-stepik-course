from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Ожидаем, что есть текст о том что корзина пуста
    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), "Message 'basket is empty' is " \
                                                                                     "not presented"

    # Ожидаем, что в корзине нет товаров
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "Items in basket are presented but " \
                                                                                 "should not be"
