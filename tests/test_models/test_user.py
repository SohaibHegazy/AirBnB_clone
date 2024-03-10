#!/usr/bin/python3
'''
Test cases for user module
'''
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''
    Class to include test cases for the User Class
    '''
    def test_user_type(self):
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)


if __name__ == "__main__":
    unittest.main()
