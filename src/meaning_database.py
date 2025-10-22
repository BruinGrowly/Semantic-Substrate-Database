"""
MeaningDatabase v2.0: The Purpose-Aware Database API
"""

from .semantic_substrate_database import SemanticSubstrateDatabase
from .ice_framework import ICEFramework, ThoughtType, ContextDomain
from typing import Dict, List, Any, Optional

class MeaningDatabase(SemanticSubstrateDatabase):
    """
    The primary interface for the purpose-aware meaning-based database.
    """

    def __init__(self, db_path: str = "semantic_database.db"):
        """Initializes the MeaningDatabase."""
        super().__init__(db_path)
        self.ice_framework = ICEFramework()
        print("[MeaningDatabase] Initialized with ICE Framework.")

    def natural_query(self, query: str, context_profile: Dict[str, Any], limit: int = 10) -> List[dict]:
        """
        Performs a semantic search using natural language and a context profile.
        """
        print(f"[MeaningDatabase] Performing natural language query: '{query}' in context '{context_profile['name']}'")
        return self.search_semantic(query, context_profile, limit)

    def process_thought(self, thought: str, thought_type: ThoughtType, domain: ContextDomain, context_profile: Dict[str, Any]) -> int:
        """
        Processes a thought through the ICE framework and stores it as a concept,
        using a purpose-specific context profile.
        """
        print(f"[MeaningDatabase] Processing thought: '{thought}' in context '{context_profile['name']}'")

        # In this advanced model, the context_profile IS the context, making the
        # ICE framework's role more about structuring the input for the model.
        coords = self.meaning_model.calculate_coordinates(thought, context_profile)

        context_name = context_profile.get("name", "default")
        concept_id = self._store_concept_with_coordinates(thought, context_name, coords)

        return concept_id
