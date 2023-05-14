import unittest
import os
from models import base_model, user, place, state, city, amenity, review
from models.engine.file_storage import FileStorage

City = city.City
Amenity = amenity.Amenity
Place = place.Place
BaseModel = base_model.BaseModel
User = user.User
State = state.State
Review = review.Review

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_all(self):
        # add some objects
        self.assertEqual(len(self.storage.all()), 0)
        new_state = State(name="California")
        new_state.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1)

    # more tests...
