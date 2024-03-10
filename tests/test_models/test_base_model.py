'''
Test cases for base_model module
'''
import time
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    Class for test cases for the BaseModel class
    '''

    def test_base_model_init(self):
        '''
        Test cases to pass intialization values to BaseModel Class
        '''
        bm1 = BaseModel()
        bm2 = BaseModel(id=str(uuid.uuid4()), name="My Trip", cost="High")
        self.assertNotEqual(bm1, bm2)
        self.assertEqual(bm2.name, "My Trip")
        self.assertEqual(bm2.cost, "High")
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2.id, str)
        self.assertIsInstance(bm2.name, str)
        self.assertIsInstance(bm2.cost, str)
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_str(self):
        '''
        Test cases to test the string representation
        '''
        bm1 = BaseModel()
        test_str = f"[{bm1.__class__.__name__}] ({bm1.id}) {bm1.__dict__}"
        self.assertEqual(bm1.__str__(), test_str)


    def test_save(self):
        '''
        Test cases to test save method in base_model
        '''
        bm1 = BaseModel()
        time.sleep(1)
        bm1.save()
        time_diff = bm1.updated_at - bm1.created_at
        self.assertGreater(abs(time_diff.total_seconds()), 1)
    
    def test_save_no_arg_passed(self):
        '''
        Test cases to test save method when no arg is passed
        expected (self)
        '''
        with self.assertRaises(TypeError) as error:
            BaseModel.save()
        self.assertEqual(str(error.exception), "save() missing 1 required positional argument: 'self'")

    def test_save_many_arg(self):
        '''
        Test cases to test save method when many arg is passed
        expected (self)
        '''
        with self.assertRaises(TypeError) as error:
            BaseModel.save(self, 1)
        self.assertEqual(str(error.exception), "save() takes 1 positional argument but 2 were given")

    def test_to_dict(self):
        '''
        Test cases to test to_dict method
        '''
        bm1 = BaseModel()
        bm2_id = str(uuid.uuid4())
        bm2_t = str(datetime.now())
        bm2 = BaseModel(id=bm2_id, created_at=bm2_t, updated_at=bm2_t,
                        name="My Trip", cost="High")
        bm1_dict = bm1.to_dict()
        bm2_dict = bm2.to_dict()
        self.assertIn('id', bm1_dict.keys())
        self.assertIsInstance(bm1_dict, dict)
        self.assertIn('id', bm2_dict.keys())
        self.assertIsInstance(bm2_dict, dict)
        self.assertIn('My Trip', bm2_dict.values())

if __name__ == "__main__":
    unittest.main()
