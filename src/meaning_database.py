"""
MeaningDatabase: The Consolidated, Meaning-Based Database API

This class provides a clean and powerful API for interacting with the semantic
database. It inherits from the refactored SemanticSubstrateDatabase and uses
the MeaningModel for all its operations.
"""

from .semantic_substrate_database import SemanticSubstrateDatabase
from .ice_framework import ICEFramework, ThoughtType, ContextDomain
from typing import Dict, List, Any, Optional
from . import macro_analyzer

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

    def get_semantic_overview(self) -> Dict[str, any]:
        """
        Provides a macro-level analysis of the entire database.
        """
        print("[MeaningDatabase] Generating semantic overview...")

        all_concepts = self.get_all_concepts()

        if not all_concepts:
            return {"message": "The database is empty. No overview can be generated."}

        center_of_gravity = macro_analyzer.calculate_semantic_center_of_gravity(all_concepts)
        clusters = macro_analyzer.identify_clusters_of_meaning(all_concepts)
        trends = macro_analyzer.analyze_semantic_trends(all_concepts)

        return {
            "total_concepts": len(all_concepts),
            "semantic_center_of_gravity": center_of_gravity,
            "clusters_of_meaning": clusters,
            "semantic_trends": trends
        }
