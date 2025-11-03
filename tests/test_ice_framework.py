"""
Tests for the ICEFramework class.
"""

import unittest
from src.ice_framework import ICEFramework, ThoughtType, ContextDomain
from src.meaning_model import MeaningModel
from src.baseline_biblical_substrate import BiblicalSemanticSubstrate

class TestICEFramework(unittest.TestCase):

    def setUp(self):
        self.meaning_model = MeaningModel(None)
        self.framework = ICEFramework(self.meaning_model)
        self.semantic_engine = BiblicalSemanticSubstrate(self.framework)
        self.meaning_model.semantic_engine = self.semantic_engine

    def test_process_thought(self):
        """
        Tests the process_thought method.
        """
        thought = "love and justice"
        thought_type = ThoughtType.BIBLICAL_UNDERSTANDING
        domain = ContextDomain.BIBLICAL

        result = self.framework.process_thought(thought, thought_type, domain)

        self.assertIn('intent_coordinates', result)
        self.assertIn('context_coordinates', result)
        self.assertIn('execution_coordinates', result)
        self.assertIn('execution_strategy', result)
        self.assertIn('divine_alignment', result)
        self.assertIn('cycle_analysis', result)

    def test_cycle_analysis(self):
        """
        Tests the cycle_analysis method.
        """
        intent_coords = {'love': 0.8, 'justice': 0.6, 'power': 0.4, 'wisdom': 0.2}
        context_coords = {'love': 0.7, 'justice': 0.7, 'power': 0.5, 'wisdom': 0.3}
        execution_coords = {'love': 0.6, 'justice': 0.8, 'power': 0.6, 'wisdom': 0.4}

        cycle_analysis = self.framework.cycle_analysis(intent_coords, context_coords, execution_coords)

        self.assertIn('overall_effectiveness', cycle_analysis)
        self.assertIn('dimensional_performance', cycle_analysis)

        # Test overall_effectiveness calculation
        intent_strength = sum(intent_coords.values()) / len(intent_coords)
        context_clarity = sum(context_coords.values()) / len(context_coords)
        execution_effectiveness = sum(execution_coords.values()) / len(execution_coords)
        expected_effectiveness = 0.3 * intent_strength + 0.3 * context_clarity + 0.4 * execution_effectiveness
        self.assertAlmostEqual(cycle_analysis['overall_effectiveness'], expected_effectiveness, places=5)

        # Test dimensional_performance calculation
        expected_performance = {}
        for dimension in intent_coords:
            expected_performance[dimension] = 0.4 * intent_coords[dimension] + 0.3 * context_coords[dimension] + 0.3 * execution_coords[dimension]

        for dimension in expected_performance:
            self.assertAlmostEqual(cycle_analysis['dimensional_performance'][dimension], expected_performance[dimension], places=5)

if __name__ == '__main__':
    unittest.main()
