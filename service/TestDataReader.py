import os

from jproperties import Properties
import resources


class TestDataReader:
    properties_path = "./resources/dev.properties"
    os.getcwd()
    @staticmethod
    def read_property(key):
        test_data = Properties()
        with open(TestDataReader.properties_path, 'rb') as test_data_file:
            test_data.load(test_data_file)
        return test_data[key][0]