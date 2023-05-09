#!/usr/bin/python3
"""Class State that inherits from the BaseModel"""
from models.base_model import BaseModel

class state(BaseModel):
	"""
	Represents a possible state for a location
	
	Attrib:
		name (string): Name of the state
	"""
	name = ""
