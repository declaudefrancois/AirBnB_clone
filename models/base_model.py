#!/usr/bin/python3
"""
    Base model class module, contain the BaseModel class
    definition.
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    """

    def __init__(self):
        """
            Creates a new instance.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

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
        """
        self.updated_at = datetime.now()
