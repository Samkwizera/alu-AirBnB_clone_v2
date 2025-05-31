#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_init(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attributes(self):
        review = Review()
        review.place_id = "P123"
        review.user_id = "U123"
        review.text = "Great place to stay!"
        
        self.assertEqual(review.place_id, "P123")
        self.assertEqual(review.user_id, "U123")
        self.assertEqual(review.text, "Great place to stay!")


if __name__ == '__main__':
    unittest.main() 