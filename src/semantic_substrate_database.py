"""
SEMANTIC SUBSTRATE DATABASE v4.2 - With Definitive Type Conversion

This version includes a definitive, low-level fix to the database connection
to guarantee that all REAL columns are correctly handled as floats.
"""

import sqlite3
import numpy as np
from typing import Dict, List, Optional

from .meaning_model import MeaningModel

def convert_real_to_float(value):
    """Definitive converter to handle REAL data type issues."""
    try:
        # First, try to decode if it's a byte string
        if isinstance(value, bytes):
            value = value.decode('utf-8')
        return float(value)
    except (ValueError, TypeError, UnicodeDecodeError):
        # Fallback for any conversion error
        return 0.0

class SemanticSubstrateDatabase:
    """
    The definitive Semantic Database Engine, with guaranteed data type correctness.
    """

    def __init__(self, db_path: str = "semantic_substrate.db"):
        self.db_path = db_path
        self.conn = None
        self.meaning_model = MeaningModel()
        self._initialize_database()
        print(f"[SEMANTIC DB] Initialized at {db_path}")
        print(f"[SEMANTIC DB] Using Definitive MeaningModel v4.0 with Sentence Embeddings.")

    def _initialize_database(self):
        """Create database schema with a definitive type converter."""
        # Definitive Fix: Register a custom converter for the REAL type
        sqlite3.register_converter("REAL", convert_real_to_float)

        # Use PARSE_DECLTYPES to ensure the converter is used
        self.conn = sqlite3.connect(self.db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        self.conn.row_factory = sqlite3.Row
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS semantic_coordinates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                concept_text TEXT NOT NULL UNIQUE,
                context TEXT,
                love REAL NOT NULL,
                power REAL NOT NULL,
                wisdom REAL NOT NULL,
                justice REAL NOT NULL,
                embedding BLOB
            )
        """)

        self.conn.commit()
        print("[SEMANTIC DB] Database schema initialized with definitive type converter.")

    def store_concept(self, text: str, context: str = None) -> int:
        """Stores a concept with coordinates and embedding."""
        coords = self.meaning_model.calculate_coordinates(text)
        embedding = self.meaning_model.model.encode(text)

        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO semantic_coordinates (concept_text, context, love, power, wisdom, justice, embedding)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(concept_text) DO UPDATE SET
                love=excluded.love,
                power=excluded.power,
                wisdom=excluded.wisdom,
                justice=excluded.justice,
                embedding=excluded.embedding
        """, (text, context, coords['love'], coords['power'], coords['wisdom'], coords['justice'], embedding.tobytes()))

        cursor.execute("SELECT id FROM semantic_coordinates WHERE concept_text = ?", (text,))
        concept_id = cursor.fetchone()[0]
        self.conn.commit()
        return concept_id

    def get_concept(self, text: str) -> Optional[dict]:
        """Retrieves a concept from the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM semantic_coordinates WHERE concept_text = ?", (text,))
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

    def search_semantic(self, query_text: str, limit: int = 10) -> List[dict]:
        """Performs a true semantic search using vector similarity."""
        query_embedding = self.meaning_model.model.encode(query_text)

        cursor = self.conn.cursor()
        cursor.execute("SELECT id, concept_text, love, power, wisdom, justice, embedding FROM semantic_coordinates")

        results = []
        for row in cursor.fetchall():
            concept = dict(row)
            db_embedding = np.frombuffer(row['embedding'], dtype=np.float32)
            similarity = self.meaning_model._cosine_similarity(query_embedding, db_embedding)
            concept['semantic_similarity'] = similarity
            results.append(concept)

        results.sort(key=lambda x: x['semantic_similarity'], reverse=True)
        return results[:limit]

    def close(self):
        if self.conn:
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
