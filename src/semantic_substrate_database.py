"""
SEMANTIC SUBSTRATE DATABASE v3.1 - Purpose-Aware

This version is updated to work with the context-aware MeaningModel,
accepting context profiles to perform purpose-driven analysis.
"""

import sqlite3
import json
import math
from typing import Dict, List, Tuple, Optional, Any, Union
from datetime import datetime
from .meaning_model import MeaningModel

class SemanticSubstrateDatabase:
    """
    The refactored Semantic Database Engine, now purpose-aware.
    """

    def __init__(self, db_path: str = "semantic_substrate.db"):
        """Initialize the semantic database"""
        self.db_path = db_path
        self.conn = None
        self.meaning_model = MeaningModel()
        self._initialize_database()

        print(f"[SEMANTIC DB] Initialized at {db_path}")
        print(f"[SEMANTIC DB] Using Purpose-Aware MeaningModel.")

    def _initialize_database(self):
        """Create database schema."""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS semantic_coordinates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                concept_text TEXT NOT NULL,
                context TEXT NOT NULL,
                love REAL NOT NULL,
                power REAL NOT NULL,
                wisdom REAL NOT NULL,
                justice REAL NOT NULL,
                divine_resonance REAL,
                distance_from_jehovah REAL,
                biblical_balance REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(concept_text, context)
            )
        """)

        cursor.execute("CREATE INDEX IF NOT EXISTS idx_concept_text ON semantic_coordinates(concept_text)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_context ON semantic_coordinates(context)")

        self.conn.commit()
        print("[SEMANTIC DB] Database schema initialized")

    def store_concept(self, text: str, context_profile: Dict[str, Any]) -> int:
        """
        Store a concept with coordinates calculated by the purpose-aware MeaningModel.
        """
        context_name = context_profile.get("name", "default")
        coords = self.meaning_model.calculate_coordinates(text, context_profile)
        return self._store_concept_with_coordinates(text, context_name, coords)

    def _store_concept_with_coordinates(self, text: str, context: str, coords: Dict[str, float]) -> int:
        """
        Stores a concept with the given coordinates.
        """
        cursor = self.conn.cursor()

        divine_resonance = self.meaning_model.divine_resonance(coords)
        distance_from_jehovah = self.meaning_model.distance_from_jehovah(coords)
        biblical_balance = self.meaning_model.biblical_balance(coords)

        cursor.execute("""
            INSERT INTO semantic_coordinates
            (concept_text, context, love, power, wisdom, justice,
             divine_resonance, distance_from_jehovah, biblical_balance, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(concept_text, context) DO UPDATE SET
                love=excluded.love,
                power=excluded.power,
                wisdom=excluded.wisdom,
                justice=excluded.justice,
                divine_resonance=excluded.divine_resonance,
                distance_from_jehovah=excluded.distance_from_jehovah,
                biblical_balance=excluded.biblical_balance,
                updated_at=CURRENT_TIMESTAMP
        """, (text, context, coords['love'], coords['power'], coords['wisdom'], coords['justice'],
              divine_resonance, distance_from_jehovah, biblical_balance))

        cursor.execute("SELECT id FROM semantic_coordinates WHERE concept_text = ? AND context = ?", (text, context))
        concept_id = cursor.fetchone()[0]

        self.conn.commit()
        return concept_id

    def get_concept(self, text: str, context: str) -> Optional[dict]:
        """
        Retrieves a concept from the database.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM semantic_coordinates WHERE concept_text = ? AND context = ?", (text, context))
        row = cursor.fetchone()
        return dict(row) if row else None

    def _get_coordinates_by_id(self, concept_id: int) -> Optional[Dict[str, float]]:
        """Helper to get coordinates by ID"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT love, power, wisdom, justice FROM semantic_coordinates WHERE id = ?", (concept_id,))
        row = cursor.fetchone()
        if row:
            return {'love': row[0], 'power': row[1], 'wisdom': row[2], 'justice': row[3]}
        return None

    def search_semantic(self, query_text: str, context_profile: Dict[str, Any], limit: int = 10) -> List[dict]:
        """
        Semantic search: Analyze query and find similar concepts using a context profile.
        """
        context_name = context_profile.get("name", "default")
        query_coords = self.meaning_model.calculate_coordinates(query_text, context_profile)

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM semantic_coordinates WHERE context = ?", (context_name,))

        results = []
        for row in cursor.fetchall():
            concept = dict(row)
            coords = {'love': concept['love'], 'power': concept['power'], 'wisdom': concept['wisdom'], 'justice': concept['justice']}
            distance = self.meaning_model.semantic_distance(query_coords, coords)
            concept['semantic_distance'] = distance
            results.append(concept)

        results.sort(key=lambda x: x['semantic_distance'])

        for result in results:
            result['semantic_similarity'] = 1.0 - (result['semantic_distance'] / 2.0)

        return results[:limit]

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
