#!/usr/bin/python3
"""To test the BaseModel Class"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
from io import StringIO
from contextlib import redirect_stdout


class TestBaseModel(unittest.TestCase):
    """The class for the BaseModel unit testing"""

    def setUp(self):
        """Create an instance for each test"""
        self.base_1 = BaseModel()

    def tearDown(self):
        """Clean the instance after each test"""
        del self.base_1

    def test_instance(self):
        """Check if an object is an instance of BaseModel"""
        # base_1 = BaseModel()
        self.assertTrue(isinstance(self.base_1, BaseModel))
        self.assertTrue(type(self.base_1), BaseModel)
        self.assertTrue(isinstance(self.base_1, object))

    def test_attributes(self):
        """Test the attributes of BaseModel as instantiated"""
        self.assertTrue(getattr(self.base_1, "id"))
        self.assertTrue(getattr(self.base_1, "created_at"))
        self.assertTrue(getattr(self.base_1, "updated_at"))

    def test_attributes_values(self):
        """To test the BaseModel attibutes values as instantiated"""
        # base_1 = BaseModel()
        expected_id = "{}\n".format(self.base_1.id)
        expected_updated_at = "{}\n".format(self.base_1.updated_at)
        expected_created_at = "{}\n".format(self.base_1.created_at)
        with StringIO() as buf_id, redirect_stdout(buf_id):
            print(self.base_1.id)
            gotten_id = buf_id.getvalue()
            self.assertEqual(expected_id, gotten_id)
        with StringIO() as buf_updated_at, redirect_stdout(buf_updated_at):
            print(self.base_1.updated_at)
            gotten_updated_at = buf_updated_at.getvalue()
            self.assertEqual(expected_updated_at, gotten_updated_at)
        with StringIO() as buf_created_at, redirect_stdout(buf_created_at):
            print(self.base_1.created_at)
            gotten_created_at = buf_created_at.getvalue()
            self.assertEqual(expected_created_at, gotten_created_at)

    def test_attributes_types(self):
        """To test the BaseModel attibutes types instantiated"""
        # base_1 = BaseModel()
        self.assertEqual(type(self.base_1.id), str)
        self.assertEqual(type(self.base_1.created_at), datetime)
        self.assertEqual(type(self.base_1.updated_at), datetime)

    def test_save(self):
        """Tests if an instance is updated with a new time"""
        # base_1 = BaseModel()
        self.base_1.save()
        self.assertNotEqual(self.base_1.created_at, self.base_1.updated_at)

    def test_to_dict(self):
        """Tests if an instance is converted to dict"""
        # base_1 = BaseModel()
        base_1_dict = self.base_1.to_dict()
        self.assertEqual(str, type(base_1_dict["updated_at"]))
        self.assertEqual(str, type(base_1_dict["created_at"]))
        self.assertEqual(str, type(base_1_dict["id"]))
        self.assertEqual(str, type(base_1_dict["__class__"]))
        self.assertEqual(base_1_dict["__class__"], "BaseModel")

    def test_str(self):
        """Test the string representation"""
        # base_1 = BaseModel()
        expected = "[BaseModel] ({}) {}\n".\
                   format(self.base_1.id, self.base_1.__dict__)
        with StringIO() as buffer, redirect_stdout(buffer):
            print(self.base_1)
            gotten = buffer.getvalue()
            self.assertEqual(expected, gotten)

    def test_kwargs(self):
        """Test for keyworded arguments"""
        # base_1 = BaseModel()
        base_1_json = self.base_1.to_dict()
        base_1_new = BaseModel(**base_1_json)
        self.assertFalse(self.base_1 is base_1_new)
        self.assertEqual(type(base_1_new.updated_at), datetime)
        self.assertEqual(type(base_1_new.created_at), datetime)
        self.assertEqual(type(base_1_new.id), str)
