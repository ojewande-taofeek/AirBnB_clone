#!/usr/bin/python3
"""The unittest for class Review"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """The test case for review"""

    def setUp(self):
        """Set up an instance of Review for each method"""
        self.review_1 = Review()

    def tearDown(self):
        """Delete the instance after each method"""
        del self.review_1

    def test_instance(self):
        """Test if it in an instance and/or subclass"""
        self.assertTrue(isinstance(self.review_1, Review))
        self.assertTrue(isinstance(self.review_1, BaseModel))
        self.assertTrue(issubclass(type(self.review_1), Review))
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attr_types(self):
        """Test the attriutes types"""
        self.assertEqual(str, type(self.review_1.text))
        self.assertEqual(str, type(self.review_1.place_id))
        self.assertEqual(str, type(self.review_1.user_id))
        self.assertEqual("", self.review_1.user_id)
        self.assertEqual("", self.review_1.user_id)
        self.assertEqual("", self.review_1.user_id)

    def test_attr(self):
        """Test the inherited attributes from BaseModel"""
        self.assertTrue(getattr(self.review_1, "id"))
        self.assertTrue(getattr(self.review_1, "created_at"))
        self.assertTrue(getattr(self.review_1, "updated_at"))
        self.assertTrue(getattr(self.review_1, "save"))
        self.assertTrue(getattr(self.review_1, "to_dict"))
