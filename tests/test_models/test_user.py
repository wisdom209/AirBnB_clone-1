#!/usr/bin/python3
"""Test this module"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Test the user class"""

    def __init__(self, *args, **kwargs):
        """Test the defined function """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test the defined function """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test the defined function """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test the defined function """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test the defined function """
        new = self.value()
        self.assertEqual(type(new.password), str)
