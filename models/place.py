#!/usr/bin/python3
'''
Place module to add Place name
'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''
    A class that inherits from the BaseModel class
    it adds the Place details
    it has eleven Public class attributes:
    city_id => empty string: it will be the City.id
    user_id => empty string: it will be the User.id
    name
    description
    number_rooms => 0
    number_bathrooms => 0
    max_guest => 0
    price_by_night => 0
    latitude => 0.0
    longitude => 0.0
    amenity_ids => empty list: it will be the list of Amenity.id
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
