#!/usr/bin/python3
"""File Storage class rising from models"""
from json import loads, dump, dumps
from os.path import exists
from models import base_model
from models import user
from models import place
from models import state
from models import city
from models import amenity
from models import review

City = city.City
Amenity = amenity.Amenity
Place = place.Place
BaseModel = base_model.BaseModel
User = user.User
State = state.State
Review = review.Review

name_class = ["BaseModel", "City", "State", "Place", "Amenity", "Review", "User"]

class FileStorage:
    """
    Class for the file storage
    File used file.json
    Begins with empty obj
    """
    __file_path = "file.json"
    __objects = {}