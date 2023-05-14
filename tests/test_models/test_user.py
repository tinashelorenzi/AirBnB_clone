import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_user_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_user_inheritance(self):
        user = User()
        self.assertTrue(isinstance(user, BaseModel))
