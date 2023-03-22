#!/usr/bin/python3
"""Test the module """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test the defined class """

    def __init__(self, *args, **kwargs):
        """Test the defined class """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test the defined class"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test the defined class"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test the defined class """
        new = self.value()
        self.assertEqual(type(new.text), str)
