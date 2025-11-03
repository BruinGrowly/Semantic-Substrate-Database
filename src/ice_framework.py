"""
ICE Framework v2.0 - MeaningModel Integrated

This refactored version of the ICE Framework is tightly integrated with the
MeaningModel, ensuring all operations are grounded in the deterministic,
4D meaning-based coordinate system.
"""

from typing import Dict, Tuple
from enum import Enum

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

    def __init__(self, meaning_model=None):
        self.meaning_model = meaning_model

    def process_thought(self, primary_thought: str, thought_type: ThoughtType, domain: ContextDomain) -> Dict[str, any]:
        """
        Main ICE processing - convert human thought to meaningful execution.
        """
        print(f"ICE PROCESSING: '{primary_thought}'")

        # The core of the new ICE framework is to use the MeaningModel to get the
        # coordinates for the thought. The context is now a direct input to the model.
        intent_coords = self.meaning_model.calculate_coordinates(primary_thought, domain.value)

        # The execution coordinates are the same as the intent coordinates in this simplified model.
        # The logic can be expanded here if needed (e.g., applying context-based transformations).
        execution_coords = intent_coords

        # Determine execution strategy based on the dominant dimension of the coordinates.
        execution_strategy = self._get_execution_strategy(execution_coords)
        
        divine_alignment = self.meaning_model.divine_resonance(execution_coords)

        return {
            'execution_coordinates': (execution_coords['love'], execution_coords['justice'], execution_coords['power'], execution_coords['wisdom']),
            'execution_strategy': execution_strategy,
            'divine_alignment': divine_alignment
        }

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
