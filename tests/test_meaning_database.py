"""
Tests for the refactored MeaningDatabase class.
"""

import unittest
import os
from src.meaning_database import MeaningDatabase
from src.ice_framework import ThoughtType, ContextDomain
from src.context_profiles import BIBLICAL_CONTEXT_PROFILE

class TestMeaningDatabase(unittest.TestCase):

    def setUp(self):
        self.db_path = "test_meaning_database.db"
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.db = MeaningDatabase(self.db_path)
        self.context_profile = BIBLICAL_CONTEXT_PROFILE

    def tearDown(self):
        self.db.close()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_store_and_get_concept(self):
        """
        Tests that a concept can be stored and retrieved.
        """
        text = "divine love"

        concept_id = self.db.store_concept(text, self.context_profile)
        self.assertIsInstance(concept_id, int)

        retrieved_concept = self.db.get_concept(text, self.context_profile["name"])
        self.assertIsNotNone(retrieved_concept)
        self.assertEqual(retrieved_concept['concept_text'], text)

    def test_natural_query(self):
        """
        Tests the natural language query functionality.
        """
        text1 = "divine love"
        text2 = "divine justice"

        self.db.store_concept(text1, self.context_profile)
        self.db.store_concept(text2, self.context_profile)

        results = self.db.natural_query("what is divine love?", self.context_profile)

        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0]['concept_text'], text1)

    def test_process_thought(self):
        """
        Tests the ICE framework integration for processing thoughts.
        """
        thought = "How can I show God's love to my neighbor?"
        thought_type = ThoughtType.SPIRITUAL_GUIDANCE
        domain = ContextDomain.PERSONAL

        concept_id = self.db.process_thought(thought, thought_type, domain, self.context_profile)
        self.assertIsInstance(concept_id, int)

        retrieved_concept = self.db.get_concept(thought, self.context_profile["name"])
        self.assertIsNotNone(retrieved_concept)
        self.assertEqual(retrieved_concept['id'], concept_id)

if __name__ == '__main__':
    unittest.main()
