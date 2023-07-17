#!/usr/bin/python3
""" test Filestorage class """
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class FileStorage:
    """
    File storage class for serializing and deserializing model objects to and from JSON files.
    """

    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                  "City": City, "Amenity": Amenity, "Place": Place,
                  "Review": Review}

    def all(self):
        """
        Returns the dictionary of objects currently in memory.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of objects in memory.

        Args:
            obj: The object to add.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves the dictionary of objects to a JSON file.
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(my_dict, json_file)

    def reload(self):
        """
        Loads the dictionary of objects from the JSON file.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                FileStorage.__objects = json.load(json_file)
            for key, val in FileStorage.__objects.items():
                FileStorage.__objects[key] = FileStorage.class_dict[val["__class__"]](**val)
