#!/usr/bin/python3
"""
This module defines the Amenity class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines an Amenity object available in a Place.
    """
    name = ""