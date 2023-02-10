#!/usr/bin/python3
"""
    Base model class module, contain the BaseModel class
    definition.
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
        Defines all common attributes/methods for other classes.

        Attributes:
            id (str): Unique identifier.
            created_at (datetime.datetime): Creation' date.
            updated_at (datetime.datetime): Last update's date.
    """
    def __init__(self, *args, **kwargs):
        """
            Creates a new instance.
        """
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

            models.storage.new(self)

            return

        for k, v in kwargs.items():
            if k == "__class__":
                continue
            if k == "created_at":
                setattr(self, k, datetime.fromisoformat(v))
            elif k == "updated_at":
                setattr(self, k, datetime.now())
            else:
                setattr(self, k, v)

    def __str__(self):
        """
            Returns a human readable, representation
            a a BaseModel instance.
        """
        fmt = "[{}] ({}) {}"
        return fmt.format(self.__class__.__name__, self.id,
                          self.__dict__)

    def to_dict(self):
        """
            Returns the dictionary representations of
            a BaseModel instance.
        """
        obj_dict = {"__class__": self.__class__.__name__}
        for k, v in self.__dict__.items():
            if k in ["updated_at", "created_at"]:
                obj_dict[k] = v.isoformat()
            else:
                obj_dict[k] = v
        return {**obj_dict}

    def save(self):
        """
            Save the instance in the storage engine.
        """
        self.updated_at = datetime.now()
        models.storage.save()
