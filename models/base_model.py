#!/usr/bin/python3
"""placeholder text"""
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self):
        """Placeholder"""
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
