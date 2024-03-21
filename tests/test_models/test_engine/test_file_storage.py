#!/usr/bin/python3
"""To test the FileStorage class"""
from models.base_model import BaseModel
from models import storage
import unittest


class Test_FileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def test_all(self):
        """Test the all method"""
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        # self.assertIs(new_dict, storage.__objects)