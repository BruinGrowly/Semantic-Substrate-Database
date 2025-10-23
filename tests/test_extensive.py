"""
Extensive tests for the refactored meaning-based database system.
"""

import unittest
import os
from src.meaning_database import MeaningDatabase
from src.meaning_model import MeaningModel
from src.ice_framework import ThoughtType, ContextDomain

class TestExtensive(unittest.TestCase):

    def setUp(self):
        self.db_path = "test_extensive.db"
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.db = MeaningDatabase(self.db_path)
        self.model = MeaningModel()

    def tearDown(self):
        self.db.close()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    # 1. MeaningModel Edge Cases
    def test_model_empty_string(self):
        """Test MeaningModel with an empty string."""
        coords = self.model.calculate_coordinates("", "biblical")
        self.assertEqual(coords, {'love': 0.5, 'justice': 0.5, 'power': 0.5, 'wisdom': 0.5})

    def test_model_stop_words_only(self):
        """Test MeaningModel with a string containing only stop words."""
        text = "what is the"
        coords = self.model.calculate_coordinates(text, "biblical")
        # It should fall back to using all words if no meaningful words are found
        self.assertNotEqual(coords, {'love': 0.5, 'justice': 0.5, 'power': 0.5, 'wisdom': 0.5})

    def test_model_punctuation(self):
        """Test that punctuation is handled correctly."""
        text1 = "divine love."
        text2 = "divine love"
        coords1 = self.model.calculate_coordinates(text1, "biblical")
        coords2 = self.model.calculate_coordinates(text2, "biblical")
        self.assertEqual(coords1, coords2)

    # 2. Database Robustness
    def test_db_different_contexts(self):
        """Test storing the same text in different contexts."""
        text = "power"
        context1 = "biblical"
        context2 = "business"

        id1 = self.db.store_concept(text, context1)
        id2 = self.db.store_concept(text, context2)

        self.assertNotEqual(id1, id2)

        concept1 = self.db.get_concept(text, context1)
        concept2 = self.db.get_concept(text, context2)

        self.assertNotEqual(concept1['love'], concept2['love'])

    def test_db_query_non_existent(self):
        """Test querying for a concept that doesn't exist."""
        results = self.db.natural_query("non existent concept")
        self.assertEqual(len(results), 0)

    # 3. Advanced Semantic Search
    def test_advanced_semantic_search_ordering(self):
        """Tests that search results are ordered by semantic similarity."""
        concepts = [
            "divine love and eternal grace",
            "the grace of the lord",
            "righteous justice and holy law",
            "the power of faith"
        ]
        for concept in concepts:
            self.db.store_concept(concept, "biblical")

        query = "grace"
        results = self.db.natural_query(query, "biblical")

        self.assertEqual(len(results), 4)
        self.assertEqual(results[0]['concept_text'], "the grace of the lord")
        self.assertEqual(results[1]['concept_text'], "divine love and eternal grace")

    # 4. ICE Framework Variations
    def test_ice_thought_variations(self):
        """Test processing thoughts with different ICE parameters."""
        thought_love = "How can I be more compassionate?"
        thought_justice = "What is the right thing to do?"

        id_love = self.db.process_thought(thought_love, ThoughtType.PRACTICAL_WISDOM, ContextDomain.PERSONAL)
        id_justice = self.db.process_thought(thought_justice, ThoughtType.THEOLOGICAL_QUESTION, ContextDomain.BIBLICAL)

        coords_love = self.db._get_coordinates_by_id(id_love)
        coords_justice = self.db._get_coordinates_by_id(id_justice)

        self.assertTrue(coords_love['love'] > coords_love['justice'])
        self.assertTrue(coords_justice['justice'] > coords_justice['love'])

    # 5. Metric Verification
    def test_metric_storage_and_retrieval(self):
        """Test that all calculated metrics are stored correctly."""
        text = "test concept for metrics"
        context = "educational"

        coords = self.model.calculate_coordinates(text, context)
        expected_resonance = self.model.divine_resonance(coords)
        expected_distance = self.model.distance_from_jehovah(coords)
        expected_balance = self.model.biblical_balance(coords)

        self.db.store_concept(text, context)
        concept = self.db.get_concept(text, context)

        self.assertAlmostEqual(concept['divine_resonance'], expected_resonance)
        self.assertAlmostEqual(concept['distance_from_jehovah'], expected_distance)
        self.assertAlmostEqual(concept['biblical_balance'], expected_balance)

if __name__ == '__main__':
    unittest.main()
