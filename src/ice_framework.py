"""
ICE Framework v2.0 - MeaningModel Integrated

This refactored version of the ICE Framework is tightly integrated with the
MeaningModel, ensuring all operations are grounded in the deterministic,
4D meaning-based coordinate system.
"""

from typing import Dict, Tuple
from enum import Enum
from .meaning_model import MeaningModel

class ThoughtType(Enum):
    """Categories of human thoughts that can be processed through ICE"""
    DIVINE_INSPIRATION = "divine_inspiration"
    BIBLICAL_UNDERSTANDING = "biblical_understanding"
    PRACTICAL_WISDOM = "practical_wisdom"
    EMOTIONAL_EXPERIENCE = "emotional_experience"
    THEOLOGICAL_QUESTION = "theological_question"
    SPIRITUAL_GUIDANCE = "spiritual_guidance"

class ContextDomain(Enum):
    """Domains where thoughts can be executed"""
    BIBLICAL = "biblical"
    EDUCATIONAL = "educational"
    BUSINESS = "business"
    PERSONAL = "personal"

class ICEFramework:
    """
    The refactored ICE (Intent Context Execution) Framework.
    This version is simpler, more powerful, and fully integrated with the MeaningModel.
    """

    def __init__(self):
        self.meaning_model = MeaningModel()
        self.dimension_emphasis = {
            'Intent': {'love': 0.9, 'justice': 0.7, 'power': 0.6, 'wisdom': 0.8},
            'Context': {'love': 0.6, 'justice': 0.8, 'power': 0.5, 'wisdom': 0.9},
            'Execution': {'love': 0.5, 'justice': 0.7, 'power': 0.9, 'wisdom': 0.6}
        }

    def process_thought(self, primary_thought: str, thought_type: ThoughtType, domain: ContextDomain) -> Dict[str, any]:
        """
        Main ICE processing - convert human thought to meaningful execution.
        """
        print(f"ICE PROCESSING: '{primary_thought}'")

        # Phase 1: Intent
        base_coords = self.meaning_model.calculate_coordinates(primary_thought, domain.value)
        intent_coords = self._apply_emphasis(base_coords, 'Intent')

        # Phase 2: Context
        # In this version, the context phase is a pass-through, but it can be expanded.
        context_coords = self._apply_emphasis(intent_coords, 'Context')

        # Phase 3: Execution
        execution_coords = self._apply_emphasis(context_coords, 'Execution')

        # Determine execution strategy based on the dominant dimension of the coordinates.
        execution_strategy = self._get_execution_strategy(execution_coords)
        
        divine_alignment = self.meaning_model.divine_resonance(execution_coords)

        cycle_analysis = self.cycle_analysis(intent_coords, context_coords, execution_coords)

        return {
            'intent_coordinates': intent_coords,
            'context_coordinates': context_coords,
            'execution_coordinates': execution_coords,
            'execution_strategy': execution_strategy,
            'divine_alignment': divine_alignment,
            'cycle_analysis': cycle_analysis
        }

    def _apply_emphasis(self, coords: Dict[str, float], phase: str) -> Dict[str, float]:
        """
        Applies dimensional emphasis weights for a given phase.
        """
        emphasis_weights = self.dimension_emphasis[phase]
        emphasized_coords = {}
        for dimension, value in coords.items():
            emphasized_coords[dimension] = value * emphasis_weights[dimension]
        return emphasized_coords

    def _get_execution_strategy(self, coords: Dict[str, float]) -> str:
        """
        Determines the execution strategy based on the dominant coordinate.
        """
        dominant_dimension = max(coords, key=coords.get)
        
        strategy_map = {
            'love': "compassionate_engagement",
            'justice': "righteous_intervention",
            'power': "authoritative_guidance",
            'wisdom': "wisdom_counseling"
        }
        
        return strategy_map.get(dominant_dimension, "balanced_ministry")

    def cycle_analysis(self, intent_coords: Dict[str, float], context_coords: Dict[str, float], execution_coords: Dict[str, float]) -> Dict[str, any]:
        """
        Performs a cycle analysis of the ICE process.
        """
        overall_effectiveness = self._calculate_overall_effectiveness(intent_coords, context_coords, execution_coords)
        dimensional_performance = self._calculate_dimensional_performance(intent_coords, context_coords, execution_coords)

        return {
            'overall_effectiveness': overall_effectiveness,
            'dimensional_performance': dimensional_performance
        }

    def _calculate_overall_effectiveness(self, intent_coords: Dict[str, float], context_coords: Dict[str, float], execution_coords: Dict[str, float]) -> float:
        """
        Calculates the overall effectiveness of the ICE cycle.
        """
        intent_strength = sum(intent_coords.values()) / len(intent_coords)
        context_clarity = sum(context_coords.values()) / len(context_coords)
        execution_effectiveness = sum(execution_coords.values()) / len(execution_coords)

        return 0.3 * intent_strength + 0.3 * context_clarity + 0.4 * execution_effectiveness

    def _calculate_dimensional_performance(self, intent_coords: Dict[str, float], context_coords: Dict[str, float], execution_coords: Dict[str, float]) -> Dict[str, float]:
        """
        Calculates the dimensional performance of the ICE cycle.
        """
        performance = {}
        for dimension in intent_coords:
            performance[dimension] = 0.4 * intent_coords[dimension] + 0.3 * context_coords[dimension] + 0.3 * execution_coords[dimension]
        return performance
