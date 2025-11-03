"""
Tests for the new "Oracle" features, including the enriched payload and macro-analysis.
"""

import unittest
import os
from src.meaning_database import MeaningDatabase
from src.meaning_model import MeaningModel
from src.baseline_biblical_substrate import BiblicalSemanticSubstrate
from src.ice_framework import ICEFramework

class TestOracleFeatures(unittest.TestCase):

    def setUp(self):
        self.db_path = "test_oracle_features.db"
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

        ice_framework = ICEFramework()
        semantic_engine = BiblicalSemanticSubstrate(ice_framework)
        meaning_model = MeaningModel(semantic_engine)
        ice_framework.meaning_model = meaning_model

        self.db = MeaningDatabase(self.db_path, meaning_model)

    def tearDown(self):
        self.db.close()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_oracle_payload_generation(self):
        """
        Tests that the oracle payload is correctly added to retrieved concepts.
        """
        text = "Our new marketing campaign will crush the competition."
        context = "business"

        self.db.store_concept(text, context)
        concept = self.db.get_concept(text, context)

        self.assertIn("dominant_attribute", concept)
        self.assertIn("insights", concept)
        self.assertIn("warnings", concept)
        self.assertIn("growth_suggestion", concept)

        # Check for a specific warning we'd expect
        self.assertTrue(any("Low alignment with 'Love'" in w for w in concept['warnings']))

    def test_semantic_overview(self):
        """
        Tests the get_semantic_overview method.
        """
        # Store a few concepts
        self.db.store_concept("Concept A: high love, low power", "test")
        self.db.store_concept("Concept B: low love, high power", "test")
        self.db.store_concept("Concept C: balanced", "test")

        overview = self.db.get_semantic_overview()

        self.assertIn("total_concepts", overview)
        self.assertEqual(overview['total_concepts'], 3)

        self.assertIn("semantic_center_of_gravity", overview)
        self.assertIn("love", overview['semantic_center_of_gravity'])

        self.assertIn("clusters_of_meaning", overview)

        self.assertIn("semantic_trends", overview)

if __name__ == '__main__':
    unittest.main()
