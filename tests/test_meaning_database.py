"""
Tests for the refactored MeaningDatabase class.
"""

import unittest
import os
import numpy as np
from src.meaning_database import MeaningDatabase

class TestMeaningDatabase(unittest.TestCase):

    def setUp(self):
        self.db_path = "test_meaning_database.db"
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.db = MeaningDatabase(self.db_path)

    def tearDown(self):
        self.db.close()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_store_and_get_concept(self):
        """
        Tests that a concept can be stored and retrieved.
        """
        text = "divine love"

        concept_id = self.db.store_concept(text)
        self.assertIsInstance(concept_id, int)

        retrieved_concept = self.db.get_concept(text)
        self.assertIsNotNone(retrieved_concept)
        self.assertEqual(retrieved_concept['concept_text'], text)

    def test_natural_query(self):
        """
        Tests the natural language query functionality.
        """
        text1 = "divine love"
        text2 = "divine justice"

        self.db.store_concept(text1)
        self.db.store_concept(text2)

        results = self.db.natural_query("what is divine love?")

        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0]['concept_text'], text1)

if __name__ == '__main__':
    unittest.main()
