#!/usr/bin/python3
""" test city """
import unittest
from models.city import City
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.city.name = "San Francisco"
        self.city.state_id = "CA"
        self.city.save()

    def tearDown(self):
        del self.city

    def test_inheritance(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "San Francisco")
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "CA")

    def test_save_method(self):
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        old_created_at = self.city.created_at
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.created_at, old_created_at)
        self.assertNotEqual(self.city.updated_at, old_updated_at)
        self.assertTrue(datetime.now().second - self.city.updated_at.second < 2)

    def test_to_dict_method(self):
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertTrue("name" in city_dict)
        self.assertTrue("state_id" in city_dict)
        self.assertTrue("__class__" in city_dict)
        self.assertEqual(city_dict["name"], "San Francisco")
        self.assertEqual(city_dict["state_id"], "CA")
        self.assertEqual(city_dict["__class__"], "City")

    def test_new_instance_from_dict(self):
        city_dict = self.city.to_dict()
        new_city = City(**city_dict)
        self.assertIsInstance(new_city, City)
        self.assertEqual(new_city.id, self.city.id)
        self.assertEqual(new_city.created_at, self.city.created_at)
        self.assertEqual(new_city.updated_at, self.city.updated_at)
        self.assertEqual(new_city.name, self.city.name)
        self.assertEqual(new_city.state_id, self.city.state_id)


if __name__ == '__main__':
    unittest.main()
