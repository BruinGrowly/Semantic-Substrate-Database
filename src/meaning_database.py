"""
MeaningDatabase: The Consolidated, Meaning-Based Database API

This class provides a clean and powerful API for interacting with the semantic
database. It inherits from the refactored SemanticSubstrateDatabase and uses
the MeaningModel for all its operations.
"""

from .semantic_substrate_database import SemanticSubstrateDatabase
from .ice_framework import ICEFramework, ThoughtType, ContextDomain
from typing import Dict, List, Any, Optional

class MeaningDatabase(SemanticSubstrateDatabase):
    """
    The primary interface for the meaning-based database.
    """

    def __init__(self, db_path: str = "semantic_database.db", meaning_model: Optional[Any] = None):
        """Initializes the MeaningDatabase."""
        from .meaning_model import MeaningModel
        from .baseline_biblical_substrate import BiblicalSemanticSubstrate

        super().__init__(db_path, meaning_model)

        if meaning_model:
            self.meaning_model = meaning_model
            self.ice_framework = ICEFramework(self.meaning_model)
        else:
            # Standard setup
            self.ice_framework = ICEFramework()
            semantic_engine = BiblicalSemanticSubstrate(self.ice_framework)
            self.meaning_model = MeaningModel(semantic_engine)
            self.ice_framework.meaning_model = self.meaning_model

        print("[MeaningDatabase] Initialized.")

    def natural_query(self, query: str, context: str = "biblical", limit: int = 10) -> List[dict]:
        """
        Performs a semantic search using natural language.
        """
        print(f"[MeaningDatabase] Performing natural language query: '{query}'")
        return self.search_semantic(query, context, limit)

    def process_thought(self, thought: str, thought_type: ThoughtType, domain: ContextDomain) -> int:
        """
        Processes a thought through the ICE framework and stores it as a concept.
        """
        print(f"[MeaningDatabase] Processing thought: '{thought}'")
        ice_result = self.ice_framework.process_thought(
            primary_thought=thought,
            thought_type=thought_type,
            domain=domain
        )

        # The ICE framework returns coordinates as a tuple, but our model expects a dict.
        exec_coords_tuple = ice_result['execution_coordinates']
        coords = {
            'love': exec_coords_tuple[0],
            'justice': exec_coords_tuple[1],
            'power': exec_coords_tuple[2],
            'wisdom': exec_coords_tuple[3]
        }

        # Store the concept with the ICE-generated coordinates.
        concept_id = self._store_concept_with_coordinates(thought, domain.value, coords)

        return concept_id
