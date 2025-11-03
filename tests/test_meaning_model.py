"""
Tests for the MeaningModel class.
"""

import unittest
from src.meaning_model import MeaningModel
from src.baseline_biblical_substrate import BiblicalSemanticSubstrate
from src.ice_framework import ICEFramework

class TestMeaningModel(unittest.TestCase):

    def setUp(self):
        # Setup for dependency injection
        ice_framework = ICEFramework()
        semantic_engine = BiblicalSemanticSubstrate(ice_framework)
        self.model = MeaningModel(semantic_engine)
        ice_framework.meaning_model = self.model

    def test_calculate_coordinates_deterministic(self):
        """
        Tests that the coordinate generation is deterministic.
        """
        text = "love"
        context = "biblical"

        coords1 = self.model.calculate_coordinates(text, context)
        coords2 = self.model.calculate_coordinates(text, context)

        self.assertEqual(coords1, coords2)

    def test_calculate_coordinates_different_text(self):
        """
        Tests that different text produces different coordinates.
        """
        text1 = "love"
        text2 = "justice"
        context = "biblical"

        coords1 = self.model.calculate_coordinates(text1, context)
        coords2 = self.model.calculate_coordinates(text2, context)

        self.assertNotEqual(coords1, coords2)

    def test_semantic_distance(self):
        """
        Tests the semantic distance calculation.
        """
        coords1 = {'love': 0.1, 'justice': 0.2, 'power': 0.3, 'wisdom': 0.4}
        coords2 = {'love': 0.5, 'justice': 0.6, 'power': 0.7, 'wisdom': 0.8}

        distance = self.model.semantic_distance(coords1, coords2)

        # Expected distance is sqrt(4 * 0.4^2) = sqrt(0.64) = 0.8
        self.assertAlmostEqual(distance, 0.8, places=5)

    def test_divine_resonance(self):
        """
        Tests the divine resonance calculation.
        """
        anchor_point = {'love': 1.0, 'justice': 1.0, 'power': 1.0, 'wisdom': 1.0}
        zero_point = {'love': 0.0, 'justice': 0.0, 'power': 0.0, 'wisdom': 0.0}

        # Resonance with the anchor point should be 1.0
        resonance_anchor = self.model.divine_resonance(anchor_point)
        self.assertAlmostEqual(resonance_anchor, 1.0, places=5)

        # Resonance with the zero point should be 0.0
        resonance_zero = self.model.divine_resonance(zero_point)
        self.assertAlmostEqual(resonance_zero, 0.0, places=5)

    def test_harmony_index(self):
        """
        Tests the harmony index calculation.
        """
        anchor_point = {'love': 1.0, 'justice': 1.0, 'power': 1.0, 'wisdom': 1.0}
        zero_point = {'love': 0.0, 'justice': 0.0, 'power': 0.0, 'wisdom': 0.0}
        mid_point = {'love': 0.5, 'justice': 0.5, 'power': 0.5, 'wisdom': 0.5}

        # Harmony with the anchor point should be 1.0
        harmony_anchor = self.model.harmony_index(anchor_point)
        self.assertAlmostEqual(harmony_anchor, 1.0, places=5)

        # Harmony with the zero point should be 1 / (1 + sqrt(4)) = 1/3
        harmony_zero = self.model.harmony_index(zero_point)
        self.assertAlmostEqual(harmony_zero, 1/3, places=5)

        # Harmony with the mid point should be 1 / (1 + sqrt(1)) = 0.5
        harmony_mid = self.model.harmony_index(mid_point)
        self.assertAlmostEqual(harmony_mid, 0.5, places=5)

    def test_truth_sense(self):
        """
        Tests the truth sense calculation.
        """
        # A statement that is expected to have a high justice coordinate
        truthful_statement = "truth and justice are important"
        # A statement that is expected to have a low justice coordinate
        deceptive_statement = "deception and lies are good"

        # The exact coordinates will be deterministic based on the hashing algorithm,
        # but we can assert that the score for the truthful statement is high
        # and the score for the deceptive statement is low.
        truth_score = self.model.truth_sense(truthful_statement)
        deception_score = self.model.truth_sense(deceptive_statement)

        self.assertTrue(truth_score > 0.5)
        self.assertTrue(deception_score < 0.5)

    def test_calculate_growth_vector(self):
        """
        Tests the growth vector calculation.
        """
        coords = {'love': 0.2, 'justice': 0.4, 'power': 0.6, 'wisdom': 0.8}
        golden_ratio = 1.61803398875

        growth_vector = self.model.calculate_growth_vector(coords)

        self.assertAlmostEqual(growth_vector['love'], (1.0 - 0.2) * golden_ratio, places=5)
        self.assertAlmostEqual(growth_vector['justice'], (1.0 - 0.4) * golden_ratio, places=5)
        self.assertAlmostEqual(growth_vector['power'], (1.0 - 0.6) * golden_ratio, places=5)
        self.assertAlmostEqual(growth_vector['wisdom'], (1.0 - 0.8) * golden_ratio, places=5)

if __name__ == '__main__':
    unittest.main()
