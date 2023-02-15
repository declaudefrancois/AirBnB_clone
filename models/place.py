#!/usr/bin.python3
"""
    Defines The Place Class model.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Represents a Place (for location) in a City.

        Atttributes:
            name (str): The city's name.
            user_id (str): The Place's owner.
            city_id (str): The id of the City's state.
            description (str): description.
            number_rooms (int): Number of rooms.
            number_bathrooms (int): Number of bathrooms.
            max_guest (int): Max number of guests.
            price_by_night (int): Price by night.
            latitude (int): Place's latitude.
            longitude (int): Place's longitude.
            amenity_ids (list(str)): Available amenities.
    """
    def __init__(self, *args, **kwargs):
        """
            Instanciates a new Place.
        """
        self.name = ""
        self.description = ""
        self.city_id = ""
        self.user_id = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__(*args, **kwargs)
