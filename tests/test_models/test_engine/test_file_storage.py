#!/usr/bin/python3
"""testing file storage module"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """placeholder text"""
    def setUp(self):
        self.file_storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        obj = BaseModel()
        self.file_storage.new(obj)
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(obj, objects["BaseModel.{}".format(obj.id)])

    def test_new(self):
        obj = BaseModel()
        self.file_storage.new(obj)
        objects = self.file_storage.all()
        self.assertEqual(obj, objects["BaseModel.{}".format(obj.id)])

    def test_save(self):
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        self.file_storage.__objects = {}
        self.file_storage.reload()
        objects = self.file_storage.all()
        self.assertEqual(obj.to_dict(),
                         objects["BaseModel.{}".format(obj.id)].to_dict())


if __name__ == "__main__":
    unittest.main()
