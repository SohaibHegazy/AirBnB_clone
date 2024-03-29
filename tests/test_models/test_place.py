#!/usr/bin/python3
'''
Test cases for place module
'''
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''
    Class to include test cases for the place Class
    '''
    def test_place_type(self):
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.place_ids, str)


if __name__ == "__main__":
    unittest.main()
