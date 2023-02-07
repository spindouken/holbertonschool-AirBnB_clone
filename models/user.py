#!/usr/bin/python3

"""
Module containing subclass: User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class represents user &
    is a subclass of BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
