#!/usr/bin/python3
"""
Test module for City class
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """TestCity class"""

    def test_instance(self):
        """Test the creation of a City instance"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """Test the instance attributes of City"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_attribute_types(self):
        """Test the attribute types of City"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)


if __name__ == "__main__":
    unittest.main()
