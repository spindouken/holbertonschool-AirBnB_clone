#!/usr/bin/python3
"""BaseModel module (class and its functions)"""
from datetime import datetime
import uuid
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Main superclass body
        strptime() - create datetime object from given string
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                    isoformat = "%Y-%m-%dT%H:%M:%S.%f"
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.strptime(value, isoformat))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """prints string representation of data object for printing"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates datetime and saves object"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dictionary with all object data"""
        lexicon = self.__dict__
        new_dict = {}
        new_dict["__class__"] = type(self).__name__
        for key, value in lexicon.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        return new_dict
