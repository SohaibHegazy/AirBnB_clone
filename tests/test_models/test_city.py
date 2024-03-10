#!/usr/bin/python3
'''
Test cases for city module
'''
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    '''
    Class to include test cases for the City Class
    '''
    def test_city_type(self):
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)


if __name__ == "__main__":
    unittest.main()
