#!/usr/bin/python3
'''
Test cases for amenity module
'''
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''
    Class to include test cases for the Amenity Class
    '''
    def test_amenity_type(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)


if __name__ == "__main__":
    unittest.main()
