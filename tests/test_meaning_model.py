"""
Tests for the MeaningModel class.
"""

import unittest
from src.meaning_model import MeaningModel
from src.context_profiles import BIBLICAL_CONTEXT_PROFILE

class TestMeaningModel(unittest.TestCase):

    def setUp(self):
        self.model = MeaningModel()
        self.context_profile = BIBLICAL_CONTEXT_PROFILE

    def test_calculate_coordinates_deterministic(self):
        """
        Tests that the coordinate generation is deterministic.
        """
        text = "love"

        coords1 = self.model.calculate_coordinates(text, self.context_profile)
        coords2 = self.model.calculate_coordinates(text, self.context_profile)

        self.assertEqual(coords1, coords2)

    def test_calculate_coordinates_different_text(self):
        """
        Tests that different text produces different coordinates.
        """
        text1 = "love"
        text2 = "justice"

        coords1 = self.model.calculate_coordinates(text1, self.context_profile)
        coords2 = self.model.calculate_coordinates(text2, self.context_profile)

        self.assertNotEqual(coords1, coords2)

    def test_semantic_distance(self):
        """
        Tests the semantic distance calculation.
        """
        coords1 = {'love': 0.1, 'justice': 0.2, 'power': 0.3, 'wisdom': 0.4}
        coords2 = {'love': 0.5, 'justice': 0.6, 'power': 0.7, 'wisdom': 0.8}

        distance = self.model.semantic_distance(coords1, coords2)

        self.assertAlmostEqual(distance, 0.8, places=5)

    def test_divine_resonance(self):
        """
        Tests the divine resonance calculation.
        """
        anchor_point = {'love': 1.0, 'justice': 1.0, 'power': 1.0, 'wisdom': 1.0}
        zero_point = {'love': 0.0, 'justice': 0.0, 'power': 0.0, 'wisdom': 0.0}

        resonance_anchor = self.model.divine_resonance(anchor_point)
        self.assertAlmostEqual(resonance_anchor, 1.0, places=5)

        resonance_zero = self.model.divine_resonance(zero_point)
        self.assertAlmostEqual(resonance_zero, 0.0, places=5)

if __name__ == '__main__':
    unittest.main()
