#!/usr/bin/python3
"""To test the FileStorage class"""
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import unittest


class Test_FileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def test_instance(self):
        """Test if storage is an instance of FileStorage"""
        self.assertTrue(isinstance(storage, FileStorage))
        self.assertTrue(issubclass(type(storage), FileStorage))

    def test_attributes(self):
        """Test all attributes"""
        self.assertTrue(getattr(storage, "_FileStorage__file_path"))
        self.assertTrue(getattr(storage, "_FileStorage__objects"))
        self.assertTrue(getattr(storage, "all"))
        self.assertTrue(getattr(storage, "new"))
        self.assertTrue(getattr(storage, "save"))
        self.assertTrue(getattr(storage, "reload"))

    def test_attrs_type(self):
        """Test the types for attributes method"""
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertEqual(type(storage._FileStorage__objects), dict)
        self.assertEqual(type(storage._FileStorage__file_path), str)
