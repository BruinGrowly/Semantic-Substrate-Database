"""
MeaningModel v5.0: The Definitive and Correct Semantic Similarity Model

This version implements the correct mapping from cosine similarity [-1, 1] to
the 4D coordinate space [0, 1], representing the final, correct implementation
of the deep semantic model.
"""
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import Dict, List, Any

class MeaningModel:
    """
    Calculates 4D coordinates using a sentence-transformer model with the
    correct mathematical mapping to the 4D meaning space.
    """

    def __init__(self, model_name='all-MiniLM-L6-v2'):
        """
        Initializes the MeaningModel, loading the pre-trained sentence transformer.
        """
        print(f"[MeaningModel] Loading sentence transformer model '{model_name}'...")
        self.model = SentenceTransformer(model_name)
        print("[MeaningModel] Model loaded successfully.")

        self.anchor_point = {'love': 1.0, 'justice': 1.0, 'power': 1.0, 'wisdom': 1.0}
        self._generate_dimension_embeddings()

    def _generate_dimension_embeddings(self):
        """
        Generates the vector embeddings for the core concepts of each dimension.
        """
        print("[MeaningModel] Generating dimension embeddings...")
        self.dimension_embeddings = {
            'love': self.model.encode("love compassion grace mercy kindness"),
            'justice': self.model.encode("justice righteousness law truth holy right"),
            'power': self.model.encode("power sovereignty almighty miracle authority"),
            'wisdom': self.model.encode("wisdom understanding knowledge discernment proverbs")
        }
        print("[MeaningModel] Dimension embeddings generated.")

    def calculate_coordinates(self, text: str, context_profile: Dict[str, Any] = None) -> dict:
        """
        Calculates 4D coordinates by projecting the text's semantic embedding
        into the 4D meaning space with the correct normalization.
        """
        if not text or not text.strip():
            return {'love': 0.5, 'justice': 0.5, 'power': 0.5, 'wisdom': 0.5}

        text_embedding = self.model.encode(text)

        love_similarity = self._cosine_similarity(text_embedding, self.dimension_embeddings['love'])
        justice_similarity = self._cosine_similarity(text_embedding, self.dimension_embeddings['justice'])
        power_similarity = self._cosine_similarity(text_embedding, self.dimension_embeddings['power'])
        wisdom_similarity = self._cosine_similarity(text_embedding, self.dimension_embeddings['wisdom'])

        # Definitive Fix: Correctly map the [-1, 1] cosine similarity range to the [0, 1] coordinate space.
        coords = {
            'love': (love_similarity + 1) / 2,
            'justice': (justice_similarity + 1) / 2,
            'power': (power_similarity + 1) / 2,
            'wisdom': (wisdom_similarity + 1) / 2
        }

        return coords

    def _cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Calculates the cosine similarity between two vectors."""
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    def semantic_distance(self, coords1: dict, coords2: dict) -> float:
        """Calculates the Euclidean distance between two 4D coordinate sets."""
        vec1 = np.array([float(v) for v in coords1.values()])
        vec2 = np.array([float(v) for v in coords2.values()])
        return np.linalg.norm(vec1 - vec2)

    def divine_resonance(self, coords: dict) -> float:
        distance = self.semantic_distance(coords, self.anchor_point)
        return max(0, 1 - (distance / 2.0))

    def distance_from_jehovah(self, coords: dict) -> float:
        return sum(abs(coords[dim] - self.anchor_point[dim]) for dim in self.anchor_point)

    def biblical_balance(self, coords: dict) -> float:
        values = list(coords.values())
        return max(0, 1 - (np.std(values) / 0.5))
