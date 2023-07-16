#!/usr/bin/python3
"""file storage class"""
import json

class FileStorage:
    """File storage class"""
    
    __file_path = "file.json"
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
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dictionary = FileStorage.__objects
        objdict = {obj: obj_dictionary[obj].to_dict() for obj in obj_dictionary.keys()}
        with open(FileStorage.__file_path, "a") as f:
            json.dump(objdict, f)
