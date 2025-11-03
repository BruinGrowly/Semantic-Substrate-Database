"""
Integration Test for the Meaning-Based Database System
"""

import unittest
import os
import subprocess
import sys
from src.meaning_database import MeaningDatabase
from src.meaning_model import MeaningModel
from src.baseline_biblical_substrate import BiblicalSemanticSubstrate
from src.ice_framework import ICEFramework

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.db_path = "test_integration.db"
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

    def test_database_and_model_integration(self):
        """
        Tests the integration between the database and the meaning model.
        """
        text = "divine love"
        context = "biblical"
        
        concept_id = self.db.store_concept(text, context)
        retrieved_concept = self.db.get_concept(text, context)
        
        self.assertIsNotNone(retrieved_concept)
        self.assertEqual(retrieved_concept['concept_text'], text)
        
        results = self.db.natural_query("what is divine love?", context)
        self.assertEqual(results[0]['concept_text'], text)

    def test_financial_analyzer_example(self):
        """
        Tests that the financial analyzer example runs without errors.
        """
        # The financial analyzer example is in the examples/ directory
        example_path = os.path.join(os.path.dirname(__file__), '..', 'examples', 'financial_analyzer.py')
        
        # Run the example as a subprocess
        result = subprocess.run([sys.executable, example_path], capture_output=True, text=True)
        
        # Check that the process completed successfully
        self.assertEqual(result.returncode, 0, f"Financial analyzer example failed with error: {result.stderr}")

if __name__ == '__main__':
    unittest.main()
