#!/usr/bin.python3
"""
    Defines The User Class model.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        Represents a user of HBNB.

        Atttributes:
            email (str): user's email.
            password (str); user's password.
            first_name (str): user's firstname.
            last_name (str): user's lastname.
    """
    def __init__(self, *args, **kwargs):
        """
            Instanciates a new User.
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
