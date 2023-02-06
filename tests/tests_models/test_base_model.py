#!/usr/bin/python3
"""based unit test"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class testBasedBaseModel(unittest.TestCase):
    """
    based placeholder text
    """
    def test_init_proper(self):
        pass
   
    def test_created(self):
        based = BaseModel()
        self.assertIsInstance(based.created_at, datetime)

    def test_updated(self):
        based = BaseModel()
        self.assertIsInstance(based.updated_at, datetime)

    def test_str(self):
        pass

    def test_save(self):
        pass

    def test_dict(self):
        pass

if __name__ == '__main__':
    unittest.main()
