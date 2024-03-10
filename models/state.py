#!/usr/bin/python3
'''
State module to add state name
'''
from models.base_model import BaseModel


class State(BaseModel):
    '''
    A class that inherits from the BaseModel class
    it adds the state details
    it has one Public class attributes:
    name
    '''
    name = ""
