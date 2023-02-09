#!/usr/bin/python3
"""User Class Test Cases"""
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_init(self):
        self.assertEqual(User, type(User()))

    def test_email_type(self):
        self.assertEqual(str, type(User.email))

    def test_password_type(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_type(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_type(self):
        self.assertEqual(str, type(User.last_name))


if __name__ == "__main__":
    unittest.main()
