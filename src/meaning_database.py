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

    def __init__(self, db_path: str = "semantic_database.db"):
        """Initializes the MeaningDatabase."""
        super().__init__(db_path)
        self.ice_framework = ICEFramework()
        print("[MeaningDatabase] Initialized with ICE Framework.")

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
