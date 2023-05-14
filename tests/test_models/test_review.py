import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_init(self):
        r = Review()
        self.assertIsInstance(r, Review)
        self.assertIsInstance(r, BaseModel)
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")

        r = Review(place_id="abc", user_id="def", text="ghi")
        self.assertEqual(r.place_id, "abc")
        self.assertEqual(r.user_id, "def")
        self.assertEqual(r.text, "ghi")

    def test_to_dict(self):
        r = Review()
        d = r.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "Review")
        self.assertEqual(d["place_id"], "")
        self.assertEqual(d["user_id"], "")
        self.assertEqual(d["text"], "")
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
