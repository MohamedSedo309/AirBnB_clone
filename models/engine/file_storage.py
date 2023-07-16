#!/usr/bin/python3
"""file storage class"""
import json

class FileStorage:
    """File storage class"""
    
    __file_path = "file.json"
    __objects = {}

    
    def all(self):
        """Returns the dictionary `objects`"""
        return FileStorage.__objects

    
    def new(self, obj):
        """Sets obj.id as key in dictionary(objects)"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    
    def save(self):
        """Serializes the dictionary(objects) to the JSON file"""
        
        """
        Make a copy of __objects to enable the values to be changed to a dictionary representation. 
        This ensures __objects always stores data in a uniform format as {key : obj} and not {key : obj.to_dict()}
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(my_dict, json_file)

    
    def reload(self):
        """Deserializes JSON file to objects(dictionary)"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                FileStorage.__objects = json.load(json_file)
            for key, val in FileStorage.__objects.items():
                FileStorage.__objects[key] = FileStorage.class_dict[val["__class__"]](**val)

    class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                  "City": City, "Amenity": Amenity, "Place": Place,
                  "Review": Review}
