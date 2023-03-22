#!/usr/bin/python3
"""Test the module"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test the class"""

    def __init__(self, *args, **kwargs):
        """Test the defined function """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test the defined function """
        new = self.value()
        self.assertEqual(type(new.name), str)
