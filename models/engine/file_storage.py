#!/usr/bin/python3
'''The Module to contain the storage class'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''
    class to serialize and deserialize using JSON
    '''

    __file_path = "file.json"
    __objects = {}
    all_cls = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Place": Place, "Amenity": Amenity,
               "Review": Review}

    def all(self):
        '''
        returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        sets in __objects the obj with key <obj class name>.id
        '''
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        '''
        serializes __objects to the JSON file (path: __file_path)
        '''
        save_dict = {}

        for key, value in self.__objects.items():
            save_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(save_dict, file)

    def reload(self):
        '''
        deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing. If the
        file doesn’t exist, no exception should be raised)

        all_cls = {"BaseModel": BaseModel}
        '''

        try:
            with open(self.__file_path, 'r') as file:
                new_dict = json.load(file)
            for key, value in new_dict.items():
                self.__objects[key] = self.all_cls[value['__class__']](**value)
        except FileNotFoundError:
            pass
