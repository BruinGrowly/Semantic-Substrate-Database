"""
Tests for the refactored MeaningDatabase class.
"""

import unittest
import os
from src.meaning_database import MeaningDatabase
from src.ice_framework import ThoughtType, ContextDomain

class TestMeaningDatabase(unittest.TestCase):

    def setUp(self):
        self.db_path = "test_meaning_database.db"
        # Ensure the old database file is removed before each test
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
        context = "biblical"

        concept_id = self.db.store_concept(text, context)
        self.assertIsInstance(concept_id, int)

        retrieved_concept = self.db.get_concept(text, context)
        self.assertIsNotNone(retrieved_concept)
        self.assertEqual(retrieved_concept['concept_text'], text)

    def test_natural_query(self):
        """
        Tests the natural language query functionality.
        """
        text1 = "divine love"
        text2 = "divine justice"
        context = "biblical"

        self.db.store_concept(text1, context)
        self.db.store_concept(text2, context)

        # Use a query that is semantically closer to text1
        results = self.db.natural_query("what is divine love?", context)

        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        # The first result should be the most semantically similar
        self.assertEqual(results[0]['concept_text'], text1)

    def test_process_thought(self):
        """
        Tests the ICE framework integration for processing thoughts.
        """
        thought = "How can I show God's love to my neighbor?"
        thought_type = ThoughtType.SPIRITUAL_GUIDANCE
        domain = ContextDomain.PERSONAL

        concept_id = self.db.process_thought(thought, thought_type, domain)
        self.assertIsInstance(concept_id, int)

        # To verify, we'll get the concept by its text, which is the thought itself
        retrieved_concept = self.db.get_concept(thought, domain.value)
        self.assertIsNotNone(retrieved_concept)
        self.assertEqual(retrieved_concept['id'], concept_id)

if __name__ == '__main__':
    unittest.main()
