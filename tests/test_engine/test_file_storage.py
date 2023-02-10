#!/usr/bin/python3
"""
    Defines the tests for The FileStorage
    storage engine class.
"""
from models import FileStorage
from models.base_model import BaseModel
from unittest import TestCase
from os import path, remove


class TestFileStoarage(TestCase):
    """
        Test class for FileStorage.
    """
    def setUp(self):
        """
            Runs Before each tests.
        """
        objs = []
        for i in range(5):
            objs.append(BaseModel())
        self.objs = objs

        f_path = "test_file.json"
        self.f_path = f_path
        self.storage = FileStorage(f_path)
        if path.isfile(f_path):
            remove(f_path)

    def test_new_and_all(self):
        """
            Tests FilesStorage new and all methods.
        """
        _objs = self.storage.all()
        self.assertIsInstance(_objs, dict)
        self.assertEqual(len(_objs), 0)

        for o in self.objs:
            self.storage.new(o)

        _objs = self.storage.all()
        self.assertIsInstance(_objs, dict)
        self.assertEqual(len(_objs), len(self.objs))

        for k in _objs.keys():
            found = False
            for obj in self.objs:
                if obj.id == _objs[k].id:
                    found = True
                    break
            self.assertTrue(found)

    def test_save_and_reload(self):
        """
            Tests FileStorage save and reload methods.
        """
        self.assertTrue(not path.isfile(self.f_path))
        self.storage.reload()
        self.assertEqual(0, len(self.storage.all()))

        for o in self.objs:
            self.storage.new(o)
        self.storage.save()
        self.assertTrue(path.isfile(self.f_path))

        storage1 = FileStorage(self.f_path)
        storage1.reload()
        self.assertEqual(len(storage1.all()), len(self.objs))

        objs = self.storage.all()
        r_objs = storage1.all()
        for key in r_objs.keys():
            self.assertEqual(r_objs[key].id, objs[key].id)
            self.assertEqual(r_objs[key].created_at, objs[key].created_at)
            self.assertTrue(r_objs[key].updated_at > objs[key].updated_at)
