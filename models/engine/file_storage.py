#!/usr/bin/python3
"""
    Defines the FileStorage engine.
"""
from json import loads, dumps
from ..base_model import BaseModel
from os import path


class FileStorage():
    """
        Serializes instances to a JSON file and
        deserializes JSON file to instances.

        Attributes:
            __file_path (str): path to the JSON file.
            __objects (dict): store all objects by <class name>.id.
    """
    def __init__(self, file_path="file.json"):
        """
            Creates a new FileStorage instance.
        """
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """
            Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
            Sets in __objects the obj with key <obj class name>.id.
        """
        cls_name = obj.__class__.__name__
        obj_id = obj.id
        key = "{}.{}".format(cls_name, obj_id)
        self.__objects[key] = obj

    def remove(self, key):
        """
            Removes in __objects the obj with key key, if found
            otherwise return false.
        """
        res = self.__objects.pop(key, False)
        if res is False:
            return False

    def update(self, *args):
        """
            Updates one object by its key,
            setting the attribute value.

            Args:
                arg (list(str)): Hold in this order, the key,
                                 the attribute's name and its value.
        """
        setattr(self.__objects[args[0]], args[1], args[2])

    def save(self):
        """
            Serializes __objects to the JSON file.
        """
        obj_dicts = {}

        for k, v in self.__objects.items():
            obj_dicts[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(dumps(obj_dicts))

    def reload(self):
        """
            Deserializes the JSON file to __objects.
            If the JSON file (__file_path) doesn't exist
            nothing happens.
        """
        if not path.exists(self.__file_path):
            return

        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                dicts = loads(f.read())
                if dicts is None or len(dicts) == 0:
                    return

                objs = {}
                for k, v in dicts.items():
                    objs[k] = BaseModel(**v)
                self.__objects = objs
        except Exception as err:
            pass
