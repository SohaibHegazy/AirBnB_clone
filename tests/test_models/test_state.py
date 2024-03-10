#!/usr/bin/python3
'''
Test cases for state module
'''
import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''
    Class to include test cases for the State Class
    '''
    def test_state_type(self):
        state = State()
        self.assertIsInstance(state.name, str)


if __name__ == "__main__":
    unittest.main()
