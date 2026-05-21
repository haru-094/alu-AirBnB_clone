#!/usr/bin/python3
"""
This module defines the Review class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines a Review object linked to a Place and a User.
    """
    place_id = ""
    user_id = ""
    text = ""