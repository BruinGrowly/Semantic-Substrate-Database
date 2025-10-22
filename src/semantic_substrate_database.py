"""
SEMANTIC SUBSTRATE DATABASE v3.0 - Meaning-Model Centric

A revolutionary database system that stores and queries semantic meaning using
the new MeaningModel with a 4D divine coordinate system. This version has been
refactored to remove all dependencies on the old, flawed engine.
"""

import sqlite3
import json
import math
from typing import Dict, List, Tuple, Optional, Any, Union
from datetime import datetime
from .meaning_model import MeaningModel

class BiblicalCoordinates:
    """
    A simple data class to hold the 4D coordinates.
    This is to maintain compatibility with the original structure.
    """
    def __init__(self, love, power, wisdom, justice):
        self.love = love
        self.power = power
        self.wisdom = wisdom
        self.justice = justice

class SemanticSubstrateDatabase:
    """
    The refactored Semantic Database Engine.

    This version uses the MeaningModel for all semantic calculations, ensuring
    that the database is truly meaning-based from the ground up.
    """

    def __init__(self, db_path: str = "semantic_substrate.db"):
        """Initialize the semantic database"""
        self.db_path = db_path
        self.conn = None
        self.meaning_model = MeaningModel()
        self._initialize_database()

        print(f"[SEMANTIC DB] Initialized at {db_path}")
        print(f"[SEMANTIC DB] Using MeaningModel for all semantic calculations.")

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

    def store_concept(self, text: str, context: str = "biblical") -> int:
        """
        Store a concept with its semantic coordinates, calculated by the MeaningModel.
        """
        coords = self.meaning_model.calculate_coordinates(text, context)
        return self._store_concept_with_coordinates(text, context, coords)

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

    def update_concept_coordinates(self, concept_id: int, coords: Dict[str, float]):
        """
        Updates the coordinates of an existing concept.
        """
        cursor = self.conn.cursor()

        divine_resonance = self.meaning_model.divine_resonance(coords)
        distance_from_jehovah = self.meaning_model.distance_from_jehovah(coords)
        biblical_balance = self.meaning_model.biblical_balance(coords)

        cursor.execute("""
            UPDATE semantic_coordinates
            SET love = ?, power = ?, wisdom = ?, justice = ?,
                divine_resonance = ?, distance_from_jehovah = ?, biblical_balance = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (coords['love'], coords['power'], coords['wisdom'], coords['justice'],
              divine_resonance, distance_from_jehovah, biblical_balance, concept_id))

        self.conn.commit()

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

    def query_by_proximity(self, target_coords_dict: dict, max_distance: float = 0.5, context: Optional[str] = None, limit: int = 10) -> List[dict]:
        """
        Find concepts near a point in semantic space.
        """
        cursor = self.conn.cursor()

        if context:
            cursor.execute("SELECT * FROM semantic_coordinates WHERE context = ?", (context,))
        else:
            cursor.execute("SELECT * FROM semantic_coordinates")

        results = []
        for row in cursor.fetchall():
            concept = dict(row)
            coords = {'love': concept['love'], 'power': concept['power'], 'wisdom': concept['wisdom'], 'justice': concept['justice']}

            distance = self.meaning_model.semantic_distance(target_coords_dict, coords)

            if distance <= max_distance:
                concept['semantic_distance'] = distance
                results.append(concept)

        results.sort(key=lambda x: x['semantic_distance'])
        return results[:limit]

    def search_semantic(self, query_text: str, context: str = "biblical", limit: int = 10) -> List[dict]:
        """
        Semantic search: Analyze query and find similar concepts.
        """
        query_coords = self.meaning_model.calculate_coordinates(query_text, context)
        results = self.query_by_proximity(query_coords, max_distance=1.0, context=context, limit=limit)

        for result in results:
            result['semantic_similarity'] = 1.0 - (result['semantic_distance'] / 2.0)

        results.sort(key=lambda x: x['semantic_similarity'], reverse=True)
        return results

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
