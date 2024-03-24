#!/usr/bin/python3
""""The unittest for class State"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """The test case for class State"""

    def setUp(self):
        """Set up the environment for State instance"""
        self.state_1 = State()

    def tearDown(self):
        """Cleans the environment after each method"""
        del self.state_1

    def test_isinstance(self):
        """Tests if instance and/or subclass"""
        self.assertTrue(isinstance(self.state_1, State))
        self.assertTrue(issubclass(type(self.state_1), State))
        self.assertTrue(issubclass(State, BaseModel))

    def test_attr_type(self):
        """Test the type of attribute"""
        self.assertEqual(str, type(self.state_1.name))

    def test_attributes(self):
        """Test the attributes"""
        self.state_1.name = "Osun"
        self.assertTrue(getattr(self.state_1, "name"))
        self.assertTrue(getattr(self.state_1, "id"))
        self.assertTrue(getattr(self.state_1, "created_at"))
        self.assertTrue(getattr(self.state_1, "updated_at"))
        self.assertTrue(getattr(self.state_1, "save"))
        self.assertTrue(getattr(self.state_1, "to_dict"))
