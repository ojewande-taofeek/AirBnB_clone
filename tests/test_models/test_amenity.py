#!/usr/bin/python3
"""The unittest for class Amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """The test case for class Amenity"""

    def setUp(self):
        """Set up an instance for each method called"""
        self.amenity_1 = Amenity()

    def tearDown(self):
        """Cleans the environment after each instance"""
        del self.amenity_1

    def test_isinstance(self):
        """Test if it an instance and/or subclass"""
        self.assertTrue(isinstance(self.amenity_1, Amenity))
        self.assertTrue(isinstance(self.amenity_1, BaseModel))
        self.assertTrue(issubclass(type(self.amenity_1), Amenity))
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attr_types(self):
        """Test the type of each attribute"""
        self.assertEqual(str, type(self.amenity_1.name))

    def test_attrs(self):
        """"Test all attributes"""
        self.assertTrue(getattr(self.amenity_1, "id"))
        self.assertTrue(getattr(self.amenity_1, "created_at"))
        self.assertTrue(getattr(self.amenity_1, "updated_at"))
        self.assertTrue(getattr(self.amenity_1, "save"))
        self.assertTrue(getattr(self.amenity_1, "to_dict"))
