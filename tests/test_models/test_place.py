#!/usr/bin/python3
"""The unitest for class Place"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """The test case for class Place"""

    def setUp(self):
        """Create an instance of Place"""
        self.place_1 = Place()

    def tearDown(self):
        """"Cleans the environemnt after each method"""
        del self.place_1

    def test_isinstance(self):
        """Test if it is an instance and/or subclass"""
        self.assertTrue(isinstance(self.place_1, Place))
        self.assertTrue(isinstance(self.place_1, BaseModel))
        self.assertTrue(issubclass(type(self.place_1), Place))
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attr_types(self):
        """Test the type of each attribute"""
        self.assertEqual(list, type(self.place_1.amenity_ids))
        self.assertEqual(str, type(self.place_1.city_id))
        self.assertEqual(str, type(self.place_1.description))
        self.assertEqual(float, type(self.place_1.latitude))
        self.assertEqual(float, type(self.place_1.longitude))
        self.assertEqual(int, type(self.place_1.max_guest))
        self.assertEqual(str, type(self.place_1.name))
        self.assertEqual(int, type(self.place_1.number_bathrooms))
        self.assertEqual(str, type(self.place_1.user_id))
        self.assertEqual(int, type(self.place_1.number_rooms))
        self.assertEqual(int, type(self.place_1.price_by_night))

    def test_attrs(self):
        """Test attributes inherited from BaseModel"""
        self.assertTrue(getattr(self.place_1, "id"))
        self.assertTrue(getattr(self.place_1, "created_at"))
        self.assertTrue(getattr(self.place_1, "updated_at"))
