#!/usr/bin/python3
"""Define Base Model class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Creating the base model class"""
    def __init__(self, *args, **kwargs):
        """
        init new base model
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            _format = "%Y-%m-%dT%H:%M:%S.%f"
            self.created_at = datetime.strptime(self.created_at, _format)
            self.updated_at = datetime.strptime(self.updated_at, _format)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    

    def save(self):
        """update the updateded at field"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return the dictionary of an intstance"""
        new_dict = {}
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                new_dict[k] = v.isoformat()
            else:
                new_dict[k] = v
        new_dict["__class__"] = type(self).__name__
        return new_dict
    
    def __str__(self):
        """string represntation for instance"""
        classname = type(self).__name__
        iid = self.id
        i_dic = self.__dict__
        return "[{}] ({}) {}".format(classname, iid, i_dic)
