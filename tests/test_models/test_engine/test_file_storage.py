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
        self.file_storage_tester.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """
        Testing reload.
        """
        FileStorage.clear()
        storage.reload()
        self.assertTrue(len(storage.all()) > 0)


if __name__ == "__main__":
    unittest.main()
