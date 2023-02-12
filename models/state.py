#!/usr/bin.python3
"""
    Defines The State Class model.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        Represents a state (Country).

        Atttributes:
            name (str): The state's name.
    """
    def __init__(self, *args, **kwargs):
        """
            Instanciates a new State.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
