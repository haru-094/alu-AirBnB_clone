#!/usr/bin/python3
"""
This module defines the BaseModel class, which serves as the base class
for all other models in the AirBnB clone project.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        
        Args:
            *args: Unused.
            **kwargs: Dictionary representation of the instance attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Register the new object with storage engine
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates updated_at and saves the instance database registry 
        to the JSON file.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a JSON-serializable dictionary mapping of the object."""
        res_dict = self.__dict__.copy()
        res_dict['__class__'] = self.__class__.__name__
        
        if isinstance(res_dict.get('created_at'), datetime):
            res_dict['created_at'] = res_dict['created_at'].isoformat()
            
        if isinstance(res_dict.get('updated_at'), datetime):
            res_dict['updated_at'] = res_dict['updated_at'].isoformat()
            
        return res_dict