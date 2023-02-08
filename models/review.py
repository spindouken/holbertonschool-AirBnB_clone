#!/usr/bin/python3
"""
This is a module containing the subclass Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class is a subclass of BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""
