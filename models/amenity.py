#!/usr/bin/python3
'''
Amenity module to add Amenity name
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
        '''
        A class that inherits from the BaseModel class
        it adds the Amenity details
        it has one Public class attributes:
        name
        '''
        name = ""
