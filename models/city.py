#!/usr/bin.python3
"""
    Defines The City model.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        Represents a City in a state.

        Atttributes:
            name (str): The city's name.
            state_id (str): The id of the City's state.
    """
    def __init__(self, *args, **kwargs):
        """
            Instanciates a new City.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
        self.state_id = ""
