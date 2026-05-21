#!/usr/bin/python3
"""
This module defines the City class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines a City object linked to a State via state_id.
    """
    state_id = ""
    name = ""