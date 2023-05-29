class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    @property
    def name(self):
        return self.__name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password