#!/usr/bin/python3
"""The unittest for class City"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """The test case for class City"""

    def setUp(self):
        """Create an instance of City for each method"""
        self.city_1 = City()

    def tearDown(self):
        """"Cleans the environment after each method"""
        del self.city_1

    def test_instance(self):
        """Test if it is an insatnce and/or subclass"""
        self.assertTrue(isinstance(self.city_1, City))
        self.assertTrue(isinstance(self.city_1, BaseModel))
        self.assertTrue(issubclass(type(self.city_1), City))
        self.assertTrue(issubclass(City, BaseModel))

    def test_attr_type(self):
        """Test the type of each attribute"""
        self.assertEqual(str, type(self.city_1.state_id))
        self.assertEqual(str, type(self.city_1.name))

    def test_attr(self):
        """Tests attributes of the instance"""
        self.assertTrue(getattr(self.city_1, "id"))
        self.assertTrue(getattr(self.city_1, "created_at"))
        self.assertTrue(getattr(self.city_1, "updated_at"))
