#!/usr/bin/python3
'''
Test cases for file_storage module
'''
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    '''
    Class for test cases for the FileStorage class
    '''
    def test_file_storage_type(self):
        '''
        Tests for the file storage
        '''
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_file_storage_attrs_type(self):
        '''
        Tests for the file storage attributes
        '''
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all_method(self):
        '''
        Tests for the all method
        '''
        self.assertIsInstance(models.storage.all(), dict)
        with self.assertRaises(TypeError):
            models.storage.all(self, 1)

    def test_new_method(self):
        '''
        Tests for the new method
        '''
        base_model = BaseModel()
        models.storage.new(base_model)
        self.assertIn(base_model, models.storage.all().values())
        user = User()
        models.storage.new(user)
        self.assertIn(user, models.storage.all().values())
        state = State()
        models.storage.new(state)
        self.assertIn(state, models.storage.all().values())
        city = City()
        models.storage.new(city)
        self.assertIn(city, models.storage.all().values())
        place = Place()
        models.storage.new(place)
        self.assertIn(place, models.storage.all().values())
        amenity = Amenity()
        models.storage.new(amenity)
        self.assertIn(amenity, models.storage.all().values())
        review = Review()
        models.storage.new(review)
        self.assertIn(review, models.storage.all().values())

    def test_new_more_arg(self):
        with self.assertRaises(TypeError):
            models.storage.new(User(), 1)

    def test_save_method(self):
        '''
        Tests for the save method
        '''
        base_model = BaseModel()
        models.storage.new(base_model)
        user = User()
        models.storage.new(user)
        state = State()
        models.storage.new(state)
        city = City()
        models.storage.new(city)
        place = Place()
        models.storage.new(place)
        amenity = Amenity()
        models.storage.new(amenity)
        review = Review()
        models.storage.new(review)
        models.storage.save()
        with open("file.json", 'r') as file:
            file_read = file.read()
            self.assertIn("BaseModel" + "." + base_model.id, file_read)
            self.assertIn("User" + "." + user.id, file_read)
            self.assertIn("State" + "." + state.id, file_read)
            self.assertIn("City" + "." + city.id, file_read)
            self.assertIn("Place" + "." + place.id, file_read)
            self.assertIn("Amenity" + "." + amenity.id, file_read)
            self.assertIn("Review" + "." + review.id, file_read)

    def test_save_no_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_save_more_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(User(), 1)

    def test_reload_method(self):
        '''
        Tests for the reload method
        '''
        obj = FileStorage._FileStorage__objects
        base_model = BaseModel()
        models.storage.new(base_model)
        user = User()
        models.storage.new(user)
        state = State()
        models.storage.new(state)
        city = City()
        models.storage.new(city)
        place = Place()
        models.storage.new(place)
        amenity = Amenity()
        models.storage.new(amenity)
        review = Review()
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        with open("file.json", 'r') as file:
            self.assertIn("BaseModel" + "." + base_model.id, obj)
            self.assertIn("User" + "." + user.id, obj)
            self.assertIn("State" + "." + state.id, obj)
            self.assertIn("City" + "." + city.id, obj)
            self.assertIn("Place" + "." + place.id, obj)
            self.assertIn("Amenity" + "." + amenity.id, obj)
            self.assertIn("Review" + "." + review.id, obj)

    def test_reload_more_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(User(), 1)

    def test_reload_more_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
