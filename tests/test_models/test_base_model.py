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
        based = BaseModel()
        self.assertIn(based.id, str(based))

    def test_save(self):
        bm = BaseModel()
        create = bm.created_at
        update = bm.updated_at
        bm.save()
        self.assertEqual(bm.created_at, create)
        self.assertNotEqual(bm.updated_at, update)

    def test_update(self):
        based = BaseModel()
        self.assertIsInstance(based.updated_at, datetime)

    def test_dict(self):
        based = BaseModel()
        basedDict = based.to_dict()
        self.assertIsInstance(basedDict, dict)
        self.assertIsInstance(basedDict["updated_at"], str)
        self.assertIsInstance(basedDict["created_at"], str)

if __name__ == '__main__':
    unittest.main()
