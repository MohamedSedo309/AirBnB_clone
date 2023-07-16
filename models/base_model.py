#!/usr/bin/python3
"""Define Base Model class"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Creating the base model class"""

    def __init__(self, *arg, **kwargs):
        """
        init new base model
        """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def save(self):
        """update the updateded at field"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return the dictionary of an intstance"""
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
    
    def __str__(self):
        """string represntation for instance"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
