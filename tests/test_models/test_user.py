#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
from datetime import datetime
from models.user import User


class TestUserModel(unittest.TestCase):
    """user.py tests"""
    def test_init(self):
        self.assertEqual(User, type(User()))

    def test_email(self):
        self.assertEqual(str, type(User.email))

    def test_pasword(self):
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        self.assertEqual(str, type(User.last_name))


if name == "main":
    unittest.main()
