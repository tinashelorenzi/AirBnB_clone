#!/usr/bin/python3

"""
Modules for base model.
"""

import uuid
from datetime import datetime

class BaseModel:

    """
    class that defines all common attributes and methods for other classes.
    """

    def __init__(self):
        """
        Initialization of new instance of base class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string presentation of the instance of the  base model.
        """
        return "[{}] ({}) {}".format(type(self.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the attribute 'update_at' to current date and time.
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        Returns dictionary represantation of instance of base model.
        """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = type(self).__name__
        base_dict["create_at"] = base_dict["created_at"].isoformat()
        base_dict["update_at"] = base_dict["updated_at"].isoformat()
        return base_dict
