#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        self.storage.new(self.model)
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main() 