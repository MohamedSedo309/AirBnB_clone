#!/usr/bin/python3
""" testing Amenity """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()
        self.amenity.name = "Wifi"
        self.amenity.save()

    def tearDown(self):
        del self.amenity

    def test_inheritance(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "Wifi")

    def test_save_method(self):
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        old_created_at = self.amenity.created_at
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, old_created_at)
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)
        self.assertTrue(datetime.now().second - self.amenity.updated_at.second < 2)

    def test_to_dict_method(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertTrue("name" in amenity_dict)
        self.assertTrue("__class__" in amenity_dict)
        self.assertEqual(amenity_dict["name"], "Wifi")
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_new_instance_from_dict(self):
        amenity_dict = self.amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)
        self.assertIsInstance(new_amenity, Amenity)
        self.assertEqual(new_amenity.id, self.amenity.id)
        self.assertEqual(new_amenity.created_at, self.amenity.created_at)
        self.assertEqual(new_amenity.updated_at, self.amenity.updated_at)
        self.assertEqual(new_amenity.name, self.amenity.name)


if __name__ == '__main__':
    unittest.main()
