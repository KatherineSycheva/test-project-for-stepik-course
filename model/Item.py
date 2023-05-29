class Item:
    """Class describes an item to add to basket"""
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def __repr__(self):
        return f"Item {self.__name}, price {self.__price}"