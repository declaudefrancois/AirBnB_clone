#!/usr/bin/python3
"""
    State tests module.
"""
from unittest import TestCase
from models.base_model import BaseModel
from models.review import Review
import datetime
import re
import json


class TestReview(TestCase):
    """
        TestCase for Review class.
    """

    def test_init(self):
        """
            New instances should have all attributes set correctly.
        """
        obj = Review()

        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj, Review)
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.text, "")
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)
        self.assertTrue(obj.created_at == obj.updated_at)

        obj1 = Review(**obj.to_dict())

        self.assertEqual(obj1.id, obj.id)
        self.assertEqual(obj1.place_id, obj.place_id)
        self.assertEqual(obj1.user_id, obj.user_id)
        self.assertEqual(obj1.text, obj.text)
        self.assertEqual(obj1.place_id, obj.place_id)
        self.assertIsInstance(obj1.created_at, datetime.datetime)
        self.assertIsInstance(obj1.updated_at, datetime.datetime)
        self.assertEqual(obj1.created_at, obj.created_at)
        self.assertTrue(obj1.created_at < obj1.updated_at)

    def test_save(self):
        """
            Should update the field updated_at.
        """
        obj = Review()
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
        obj = Review()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj.id, obj_dict["id"])
        self.assertEqual(obj.place_id, obj_dict["place_id"])
        self.assertEqual(obj.user_id, obj_dict["user_id"])
        self.assertEqual(obj.text, obj_dict["text"])
        self.assertEqual(obj.created_at.isoformat(), obj_dict["created_at"])
        self.assertEqual(obj.updated_at.isoformat(), obj_dict["updated_at"])
        self.assertEqual(obj.__class__.__name__, obj_dict['__class__'])

    def test_str(self):
        """
            [<class name>] (<self.id>) <self.__dict__> should be the human
            friendly format representation of a Review instance.
        """
        obj = Review()
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
