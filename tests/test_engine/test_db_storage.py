#!/usr/bin/python3
import unittest
import os
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel


class TestDBStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ['HBNB_MYSQL_USER'] = 'hbnb_test'
        os.environ['HBNB_MYSQL_PWD'] = 'hbnb_test_pwd'
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_DB'] = 'hbnb_test_db'
        os.environ['HBNB_ENV'] = 'test'
        cls.storage = DBStorage()
        cls.storage.reload()

    def setUp(self):
        self.model = BaseModel()

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        self.storage.new(self.model)
        self.storage.save()
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_delete(self):
        self.storage.new(self.model)
        self.storage.save()
        self.storage.delete(self.model)
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertNotIn(key, self.storage.all())

    def test_close(self):
        self.storage.close()
        self.assertIsNone(self.storage._DBStorage__session)


if __name__ == '__main__':
    unittest.main() 