#!/usr/bin/python3
'''
Test cases for review module
'''
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''
    Class to include test cases for the Review Class
    '''
    def test_review_type(self):
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)


if __name__ == "__main__":
    unittest.main()
