#!/usr/bin/python3
"""placeholder text"""
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Placeholder
        strptime() - create datetime object from given string
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """placeholder"""
        based = self.__class__.__name__
        return f"[{based}] ({self.id}) {self.__dict__}"

    def save(self):
        """placeholder"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """placeholder"""
        lexicon = self.__dict__.copy()
        lexicon['__class__'] = type(self).__name__
        lexicon['created_at'] = self.created_at.isoformat()
        lexicon['updated_at'] = self.created_at.isoformat()
        return lexicon
