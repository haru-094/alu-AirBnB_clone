#!/usr/bin/python3
"""Unittests for models/base_model.py"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test fixtures"""
        self.model = BaseModel()

    def test_id_is_string(self):
        """Test that id is a string"""
        self.assertIsInstance(self.model.id, str)

    def test_id_is_unique(self):
        """Test that each instance has a unique id"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of BaseModel"""
        string = str(self.model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(self.model.id, string)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at attribute"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict_returns_dict(self):
        """Test that to_dict() returns a dictionary"""
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_class_name(self):
        """Test that to_dict() includes __class__ key"""
        obj_dict = self.model.to_dict()
        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_to_dict_created_at_is_string(self):
        """Test that created_at in to_dict() is a string"""
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict["created_at"], str)

    def test_to_dict_updated_at_is_string(self):
        """Test that updated_at in to_dict() is a string"""
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_to_dict_iso_format(self):
        """Test that datetime strings are in ISO format"""
        obj_dict = self.model.to_dict()
        created = obj_dict["created_at"]
        updated = obj_dict["updated_at"]
        # Validate ISO format by parsing
        datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f")
        datetime.strptime(updated, "%Y-%m-%dT%H:%M:%S.%f")

    def test_to_dict_contains_id(self):
        """Test that to_dict() contains the id"""
        obj_dict = self.model.to_dict()
        self.assertIn("id", obj_dict)
        self.assertEqual(obj_dict["id"], self.model.id)


if __name__ == "__main__":
    unittest.main()
