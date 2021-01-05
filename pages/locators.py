'''
Здесь хранятся внешние переменные для селекторов
'''


from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    ITEM_NAME = (By.CSS_SELECTOR, "div[class = \"col-sm-6 product_main\"] > h1")
    ITEM_ADDED_TEXT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_COST = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")
    ITEM_COST = (By.CSS_SELECTOR, "p.price_color")

