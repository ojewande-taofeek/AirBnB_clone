#!/usr/bin/python3
"""A module that contains the class BaseModel"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """The constructor/instantiation method"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """The informal string representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
           updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values ofi
           __dict__ of the instance
        """
        new_dict = dict()
        for key, val in self.__dict__.items():
            if key == "updated_at":
                new_dict["updated_at"] \
                         = self.updated_at.isoformat()
            elif key == "created_at":
                new_dict["created_at"] \
                         = self.created_at.isoformat()
            else:
                new_dict[key] = val
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
