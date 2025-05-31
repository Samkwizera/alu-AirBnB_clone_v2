#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_init(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attributes(self):
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")


if __name__ == '__main__':
    unittest.main() 