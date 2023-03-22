#!/usr/bin/python3
"""Tests the amenity module"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test Amenity"""

    def __init__(self, *args, **kwargs):
        """Test initialization"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test equal names on init"""
        new = self.value()
        self.assertEqual(type(new.name), str)
