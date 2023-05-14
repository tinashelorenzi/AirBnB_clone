import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_init(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
