#!/usr/bin/python3
"""file storage class"""
import json

class FileStorage:
    """File storage class"""
    
    __file_path = "data.json"
    __objects = {}

    def all(self):
        """method to get all objects saved in the file"""
        return FileStorage.__objects

    def new(self, obj):
        """create new object using id """
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj
    
    def reload(self):
        """
        Deserialize the JSON file __file_path to __objects, if it exists.
        fromjson .....
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            raise FileNotFoundError("File not found: {}".format(FileStorage.__file_path))
