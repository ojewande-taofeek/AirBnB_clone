#!/usr/bin/python3
"""File storage for instances"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    """serializes instances to a JSON file and
       deserializes JSON file to instances
    """
    __file_path = "file.json"
    __object = dict()

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
           stores a new instance in __object
        """
        obj_key = obj.__class__.__name__ + '.' + obj.id
        self.__object[obj_key] = obj

    def all(self):
        """returns the dictionary __objects"""
        return self.__object

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = dict()
        for key, obj in self.__object.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the
           JSON file (__file_path) exists ;
           otherwise, do nothing. If the file doesn’t exist, no
           exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                new_obj_dict = json.load(file)
                for key, value in new_obj_dict.items():
                    class_name = value['__class__']
                    class_name = globals()[class_name]
                    FileStorage.__object[key] = class_name(**value)
        except FileNotFoundError:
            pass
