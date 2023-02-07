#!/usr/bin/python3
"""placeholder text"""
from datetime import datetime
import uuid
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Placeholder
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
        """placeholder"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """placeholder"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """placeholder"""
        lexicon = self.__dict__.copy()
        lexicon['__class__'] = self.__class__.__name__
        lexicon['created_at'] = self.created_at.isoformat()
        lexicon['updated_at'] = self.created_at.isoformat()
        return lexicon
