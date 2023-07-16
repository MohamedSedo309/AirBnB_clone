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
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """update the updateded at field"""
        self.updated_at = datetime.today()
        models.storage.save()

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
