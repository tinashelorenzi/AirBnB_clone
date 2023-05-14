#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def tearDown(self):
        del self.state

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "name"))

    def test_initialization(self):
        self.assertIsInstance(self.state, State)
        self.assertEqual(self.state.name, "")

    def test_str_representation(self):
        string = str(self.state)
        self.assertIsInstance(string, str)
        self.assertIn("[State]", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)

    def test_save_method(self):
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

    def test_to_dict_method(self):
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)
        self.assertIsInstance(state_dict["id"], str)


if __name__ == "__main__":
    unittest.main()
