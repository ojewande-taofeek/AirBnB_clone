#!/usr/bin/python3
"""The unittest for class User"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests the class User"""

    def setUp(self):
        """Set the environment for user"""
        self.user_1 = User()

    def tearDown(self):
        """Deletes the user_1 instance after each method"""
        del self.user_1

    def test_instance(self):
        """"Tests if is an instance"""
        self.assertTrue(isinstance(self.user_1, User))
        self.assertTrue(issubclass(type(self.user_1), User))
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Test if User has an attribute"""
        """
            self.assertTrue(getattr(self.user_1.__class__, "email"))
            self.asserTrue(getattr(self.user_1, "password"))
            self.asserTrue(getattr(self.user_1, "first_name"))
            self.asserTrue(getattr(self.user_1, "last_name"))
        """
        self.assertTrue(getattr(self.user_1, "updated_at"))
