#!/usr/bin/python3
"""
    Place tests module.
"""
from unittest import TestCase
from models.base_model import BaseModel
from models.place import Place
import datetime
import re
import json


class TestPlace(TestCase):
    """
        TestCase for Place class.
    """

    def test_init(self):
        """
            New instances should have all attributes set correctly.
        """
        obj = Place()

        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj, Place)
        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(len(obj.amenity_ids), 0)
        self.assertIsInstance(obj.amenity_ids, list)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)
        self.assertTrue(obj.created_at == obj.updated_at)

        obj1 = Place(**obj.to_dict())

        self.assertEqual(obj1.id, obj.id)
        self.assertEqual(obj1.name, obj.name)
        self.assertEqual(obj1.description, obj.description)
        self.assertEqual(obj1.user_id, obj.user_id)
        self.assertEqual(obj1.city_id, obj.city_id)
        self.assertEqual(obj1.number_rooms, obj.number_rooms)
        self.assertEqual(obj1.number_bathrooms, obj.number_bathrooms)
        self.assertEqual(obj1.max_guest, obj.max_guest)
        self.assertEqual(obj1.price_by_night, obj.price_by_night)
        self.assertEqual(obj1.latitude, obj.latitude)
        self.assertEqual(obj1.longitude, obj.longitude)
        self.assertEqual(len(obj.amenity_ids), len(obj1.amenity_ids))
        self.assertIsInstance(obj1.created_at, datetime.datetime)
        self.assertIsInstance(obj1.updated_at, datetime.datetime)
        self.assertEqual(obj1.created_at, obj.created_at)
        self.assertTrue(obj1.created_at < obj1.updated_at)

    def test_save(self):
        """
            Should update the field updated_at.
        """
        obj = Place()
        updated_at = obj.updated_at
        obj.save()

        self.assertIsInstance(obj.updated_at, datetime.datetime)
        self.assertTrue(updated_at < obj.updated_at)

    def test_to_dict(self):
        """
            Should return a dictionary containing all keys/values of
            __dict__ of the instance.
            A key __class__ must be added to this dictionary with the
            class name of the object.
            Date fields must be converted into ISO date.
        """
        obj = Place()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj.id, obj_dict["id"])
        self.assertEqual(obj.city_id, obj_dict["city_id"])
        self.assertEqual(obj.user_id, obj_dict["user_id"])
        self.assertEqual(obj.name, obj_dict["name"])
        self.assertEqual(obj.description, obj_dict["description"])
        self.assertEqual(obj.number_rooms, obj_dict["number_rooms"])
        self.assertEqual(obj.number_bathrooms, obj_dict["number_bathrooms"])
        self.assertEqual(obj.max_guest, obj_dict["max_guest"])
        self.assertEqual(obj.price_by_night, obj_dict["price_by_night"])
        self.assertEqual(obj.latitude, obj_dict["latitude"])
        self.assertEqual(obj.longitude, obj_dict["longitude"])
        self.assertEqual(len(obj.amenity_ids), len(obj_dict["amenity_ids"]))
        self.assertEqual(obj.created_at.isoformat(), obj_dict["created_at"])
        self.assertEqual(obj.updated_at.isoformat(), obj_dict["updated_at"])
        self.assertEqual(obj.__class__.__name__, obj_dict['__class__'])

    def test_str(self):
        """
            [<class name>] (<self.id>) <self.__dict__> should be the human
            friendly format representation of a Review instance.
        """
        obj = Place()
        obj_dict = obj.to_dict()
        obj_str = "{}".format(obj)

        regexp = (r"\[(?P<cls_name>.*)\] "
                  r"\((?P<obj_id>.*)\) "
                  r"(?P<obj_dict>.*)")
        m = re.match(regexp, obj_str)
        g_dict = m.groupdict()

        self.assertEqual(obj.id, g_dict['obj_id'])
        self.assertEqual(obj.__class__.__name__, g_dict['cls_name'])
        for k, v in eval(g_dict['obj_dict']).items():
            if k in ["created_at", "updated_at"]:
                self.assertEqual(obj_dict[k], v.isoformat())
            else:
                self.assertEqual(obj_dict[k], v)
