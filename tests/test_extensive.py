"""
Extensive tests for the refactored meaning-based database system.
"""

import unittest
import os
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
        coords = self.model.calculate_coordinates("", self.biblical_profile)
        self.assertEqual(coords, {'love': 0.5, 'justice': 0.5, 'power': 0.5, 'wisdom': 0.5})

    def test_model_stop_words_only(self):
        text = "what is the"
        coords = self.model.calculate_coordinates(text, self.biblical_profile)
        self.assertNotEqual(coords, {'love': 0.5, 'justice': 0.5, 'power': 0.5, 'wisdom': 0.5})

    def test_model_punctuation(self):
        text1 = "divine love."
        text2 = "divine love"
        coords1 = self.model.calculate_coordinates(text1, self.biblical_profile)
        coords2 = self.model.calculate_coordinates(text2, self.biblical_profile)
        self.assertEqual(coords1, coords2)

    def test_db_different_contexts(self):
        text = "power"
        id1 = self.db.store_concept(text, self.biblical_profile)
        id2 = self.db.store_concept(text, self.financial_profile)
        self.assertNotEqual(id1, id2)
        concept1 = self.db.get_concept(text, self.biblical_profile["name"])
        concept2 = self.db.get_concept(text, self.financial_profile["name"])
        self.assertNotEqual(concept1['love'], concept2['love'])

    def test_db_query_non_existent(self):
        results = self.db.natural_query("non existent concept", self.biblical_profile)
        self.assertEqual(len(results), 0)

    def test_advanced_semantic_search_ordering(self):
        concepts = ["divine love and eternal grace", "the grace of the lord", "righteous justice and holy law"]
        for concept in concepts:
            self.db.store_concept(concept, self.biblical_profile)
        query = "grace"
        results = self.db.natural_query(query, self.biblical_profile)
        self.assertEqual(len(results), 3)
        self.assertIn("grace", results[0]['concept_text'])

    def test_ice_thought_variations(self):
        thought_love = "How can I be more compassionate?"
        thought_justice = "What is the right thing to do?"
        id_love = self.db.process_thought(thought_love, ThoughtType.PRACTICAL_WISDOM, ContextDomain.PERSONAL, self.biblical_profile)
        id_justice = self.db.process_thought(thought_justice, ThoughtType.THEOLOGICAL_QUESTION, ContextDomain.BIBLICAL, self.biblical_profile)
        coords_love = self.db._get_coordinates_by_id(id_love)
        coords_justice = self.db._get_coordinates_by_id(id_justice)
        self.assertTrue(coords_love['love'] > 0.5)
        self.assertTrue(coords_justice['justice'] > 0.5)

    def test_metric_storage_and_retrieval(self):
        text = "test concept for metrics"
        coords = self.model.calculate_coordinates(text, self.biblical_profile)
        expected_resonance = self.model.divine_resonance(coords)
        expected_distance = self.model.distance_from_jehovah(coords)
        expected_balance = self.model.biblical_balance(coords)
        self.db.store_concept(text, self.biblical_profile)
        concept = self.db.get_concept(text, self.biblical_profile["name"])
        self.assertAlmostEqual(concept['divine_resonance'], expected_resonance)
        self.assertAlmostEqual(concept['distance_from_jehovah'], expected_distance)
        self.assertAlmostEqual(concept['biblical_balance'], expected_balance)

if __name__ == '__main__':
    unittest.main()
