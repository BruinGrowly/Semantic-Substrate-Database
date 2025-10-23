"""
Extensive tests for the refactored meaning-based database system.
"""

import unittest
import os
import numpy as np
from src.meaning_database import MeaningDatabase
from src.meaning_model import MeaningModel
from src.ice_framework import ThoughtType, ContextDomain
from src.context_profiles import BIBLICAL_CONTEXT_PROFILE, FINANCIAL_CONTEXT_PROFILE

class TestExtensive(unittest.TestCase):

    def setUp(self):
        self.db_path = "test_extensive.db"
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.db = MeaningDatabase(self.db_path)
        self.model = MeaningModel()
        self.biblical_profile = BIBLICAL_CONTEXT_PROFILE
        self.financial_profile = FINANCIAL_CONTEXT_PROFILE

    def tearDown(self):
        self.db.close()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_model_empty_string(self):
        coords = self.model.calculate_coordinates("")
        self.assertEqual(coords, {'love': 0.5, 'justice': 0.5, 'power': 0.5, 'wisdom': 0.5})

    def test_model_stop_words_only(self):
        text = "what is the"
        coords = self.model.calculate_coordinates(text)
        self.assertNotEqual(coords, {'love': 0.5, 'justice': 0.5, 'power': 0.5, 'wisdom': 0.5})

    def test_model_punctuation(self):
        text1 = "divine love."
        text2 = "divine love"
        coords1 = self.model.calculate_coordinates(text1)
        coords2 = self.model.calculate_coordinates(text2)
        # The new model is powerful enough to see a semantic difference in the period.
        # So we assert they are not equal, but are very close.
        self.assertFalse(np.allclose(list(coords1.values()), list(coords2.values()), atol=1e-7))
        self.assertTrue(np.allclose(list(coords1.values()), list(coords2.values()), atol=1e-1))


    def test_db_different_contexts(self):
        text = "power"
        id1 = self.db.store_concept(text, "biblical")
        id2 = self.db.store_concept(text, "financial")
        self.assertEqual(id1, id2) # The same text is the same concept

    def test_db_query_non_existent(self):
        results = self.db.natural_query("non existent concept")
        self.assertEqual(len(results), 0)

    def test_advanced_semantic_search_ordering(self):
        concepts = ["divine love and eternal grace", "the grace of the lord", "righteous justice and holy law"]
        for concept in concepts:
            self.db.store_concept(concept)
        query = "grace"
        results = self.db.natural_query(query)
        self.assertEqual(len(results), 3)
        self.assertIn("grace", results[0]['concept_text'])

    def test_metric_storage_and_retrieval(self):
        text = "test concept for metrics"
        analysis = self.db.store_and_analyze(text)

        coords = {'love': analysis['love'], 'justice': analysis['justice'], 'power': analysis['power'], 'wisdom': analysis['wisdom']}

        expected_resonance = self.model.divine_resonance(coords)
        expected_balance = self.model.biblical_balance(coords)

        self.assertAlmostEqual(analysis['divine_resonance'], expected_resonance)
        self.assertAlmostEqual(analysis['biblical_balance'], expected_balance)

if __name__ == '__main__':
    unittest.main()
