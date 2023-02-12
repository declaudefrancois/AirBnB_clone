#!/usr/bin.python3
"""
    Defines The Review model.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Represents a Review made by a user about
        a Place.

        Atttributes:
            place_id (str): The palce's id.
            user_id (str): The user's id.
            text (str): The review's content.
    """
    def __init__(self, *args, **kwargs):
        """
            Instanciates a new User.
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
