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
    def new(self, objs):
        """
        Sets the object with key into __objects{}
        """
        ind = "{}.{}".format(objs.__class__.__name__, objs.id)
        FileStorage.__objects[key] = objs
    def reload(self):
        """
        Deserialze json to __objects
        """
        if exist(FileStorage.__file_path):
            #Done if json file exists, recorded in file_path
            with open(FileStorage.__file_path, "r", encoding='utf-8') as doc:
                dict_from_j = load(doc)
            for key, value in dict_from_j.items():
                if key.split('.')[0] in name_class:
                    #Deserialize indeces
                    FileStorage.__objects[key] = eval(key.split('.')[0])(**value)
