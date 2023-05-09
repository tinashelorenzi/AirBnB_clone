#!/usr/bin/python3
"""The class instance from the BaseModel"""
from models.base_model import BaseModel

class User(BaseModel):
	"""
	Represents a user object
	Attrib:
		email (string): Email of user.
		first_name (string): First name of user
		last_name (string): Last name of user
		password (string): Plain text passcode for user
	"""
	email = ""
	first_name = ""
	last_name = ""
	password = ""

