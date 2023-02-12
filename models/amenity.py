#!/usr/bin.python3
"""
    Defines The Amenity model.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Represents an Amenity available in a place.

        Atttributes:
            name (str): The amenity's name.
    """
    def __init__(self, *args, **kwargs):
        """
            Instanciates a new Amenity.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
