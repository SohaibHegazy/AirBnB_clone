#!/usr/bin/python3
'''
Review module to add Review details
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    A class that inherits from the BaseModel class
    it adds the Review details
    it has Three Public class attributes:
    place_id => empty string: it will be the Place.id
    user_id => empty string: it will be the User.id
    text => 
    '''
    place_id = ""
    user_id = ""
    text = ""
