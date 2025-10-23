"""
MeaningDatabase v5.2: Definitive API with Final Bug Fixes
"""

from .semantic_substrate_database import SemanticSubstrateDatabase
from .context_detector import ContextDetector
from .context_profiles import BIBLICAL_CONTEXT_PROFILE, FINANCIAL_CONTEXT_PROFILE
from .ice_framework import ThoughtType, ContextDomain
from typing import Dict, List, Any, Optional

class MeaningDatabase(SemanticSubstrateDatabase):
    """
    The primary, simplified interface for the deep semantic database, now with
    final bug fixes and automatic context detection.
    """

    def __init__(self, db_path: str = "semantic_database.db"):
        """Initializes the definitive MeaningDatabase."""
        super().__init__(db_path)
        self.context_detector = ContextDetector([BIBLICAL_CONTEXT_PROFILE, FINANCIAL_CONTEXT_PROFILE])
        print("[MeaningDatabase] API v5.2 Initialized with Automatic Context Detection.")

    def natural_query(self, query: str, limit: int = 10) -> List[dict]:
        """
        Performs a true semantic search using natural language.
        """
        print(f"[MeaningDatabase] Performing deep semantic search for: '{query}'")
        return self.search_semantic(query, limit)

    def store_and_analyze(self, text: str, context: str = None) -> Dict[str, Any]:
        """
        Stores a concept and returns its full 4D meaning profile.
        """
        print(f"[MeaningDatabase] Storing and analyzing: '{text}'")
        concept_id = self.store_concept(text, context)
        concept_row = self.get_concept(text)

        coords = self._get_coordinates_by_id(concept_id)

        analysis = dict(concept_row)
        analysis['divine_resonance'] = self.meaning_model.divine_resonance(coords)
        analysis['biblical_balance'] = self.meaning_model.biblical_balance(coords)

        return analysis

    def analyze_with_auto_context(self, text: str) -> Dict[str, Any]:
        """
        Analyzes a text using the best-detected context profile.
        """
        profile = self.context_detector.detect(text)
        print(f"[MeaningDatabase] Auto-detected context: '{profile['name']}'")

        # We need to re-calculate the coordinates with the detected profile
        # However, the new MeaningModel is context-agnostic, so we just store
        return self.store_and_analyze(text, profile['name'])
