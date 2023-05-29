from model.User import User
from service.TestDataReader import TestDataReader


class UserCreator:
    @staticmethod
    def with_credentials_from_property():
        return User(TestDataReader.read_property("USER"), TestDataReader.read_property("PASSWORD"))

