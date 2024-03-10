#!/usr/bin/python3
'''
City module to add city name and state id
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    A class that inherits from the BaseModel class
    it adds the city details
    it has two Public class attributes:
    name
    state id => will be State.id
    '''
    name = ""
    state_id = ""
