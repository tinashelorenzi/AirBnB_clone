import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        expected = f"[BaseModel] ({self.model.id}) {{}}"
        self.assertEqual(str(self.model), expected)

    def test_save(self):
        prev_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(prev_updated_at, self.model.updated_at)

    def test_to_dict(self):
        expected = {
            'id': self.model.id,
            '__class__': 'BaseModel',
            'created_at': self.model.created_at.isoformat(),
            'updated_at': self.model.updated_at.isoformat()
        }
        self.assertDictEqual(self.model.to_dict(), expected)
