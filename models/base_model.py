#!/usr/bin/python3
''' Model to include the main class of the project '''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    The main class which all other
    classes inheret from
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor for the main class
        attrs:
        uuid4
        create time
        update time
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        str method
        '''
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        '''
        updates the public instance attribute updated_at
        with the current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        Method to make create and update times strings
        and to  add class name to __class__ and return
        all into dict
        '''
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
