from model.Item import Item


class Basket:
    """Basket in online shop"""
    def __init__(self, items: list):
        """Checking that every item in items is instance of Item class"""
        for item in items:
            if not isinstance(item, Item):
                raise f"Can't create object, item {item} is not instance of Item class"
        self.__items__ = items

    def __repr__(self):
        return "\n".join(item for item in self.__items__)

    def add_item(self, item: Item):
        if isinstance(item, Item):
            self.__items__.append(item)
        else:
            raise f"Can't add item into the basket. {item} is not instance of Item class"

    def delete_item(self, item: Item):
        try:
            self.__items__.remove(item)
        except Exception:
            print(f"Can't delete item {item}")

    def get_total_price(self):
        s = 0
        for item in self.__items__:
            s += item.price
        return s