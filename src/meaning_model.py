"""
MeaningModel v3.0: The Definitive, Transparent, and Correct Model

This final version of the model uses a simple, transparent, and powerful
keyword-scoring mechanism that is easy to debug and produces intuitive results.
"""
import math
import numpy as np
import re
from typing import Dict, List, Any

class MeaningModel:
    """
    Calculates 4D coordinates using a clear and effective keyword-scoring system.
    """

    def __init__(self):
        self.anchor_point = {'love': 1.0, 'justice': 1.0, 'power': 1.0, 'wisdom': 1.0}

    def _generate_ngrams(self, words: List[str], n: int) -> List[str]:
        ngrams = []
        for i in range(len(words) - n + 1):
            ngrams.append(" ".join(words[i:i+n]))
        return ngrams

    def calculate_coordinates(self, text: str, context_profile: Dict[str, Any]) -> dict:
        """
        Calculates 4D coordinates using a transparent keyword-scoring model.
        """
        words = re.findall(r'\b\w+\b', text.lower())

        tokens = words + self._generate_ngrams(words, 2) + self._generate_ngrams(words, 3)

        love_score = self._calculate_dimension_score(tokens, context_profile['love']['keywords'])
        justice_score = self._calculate_dimension_score(tokens, context_profile['justice']['keywords'])
        power_score = self._calculate_dimension_score(tokens, context_profile['power']['keywords'])
        wisdom_score = self._calculate_dimension_score(tokens, context_profile['wisdom']['keywords'])

        scores = {'love': love_score, 'justice': justice_score, 'power': power_score, 'wisdom': wisdom_score}

        # Normalize to a 0-1 range, where 0.5 is the neutral point
        final_coords = {}
        for dim, score in scores.items():
            # Use tanh to create a smooth, bounded normalization
            normalized_score = 0.5 * (math.tanh(score) + 1)
            final_coords[dim] = normalized_score

        return final_coords

    def _calculate_dimension_score(self, tokens: List[str], keywords: Dict[str, float]) -> float:
        score = 0.0
        for token in tokens:
            if token in keywords:
                score += keywords[token]
        return score

    def semantic_distance(self, coords1: dict, coords2: dict) -> float:
        return math.sqrt(
            (coords1['love'] - coords2['love'])**2 +
            (coords1['justice'] - coords2['justice'])**2 +
            (coords1['power'] - coords2['power'])**2 +
            (coords1['wisdom'] - coords2['wisdom'])**2
        )

    def divine_resonance(self, coords: dict) -> float:
        distance = self.semantic_distance(coords, self.anchor_point)
        return max(0, 1 - (distance / 2.0))

    def distance_from_jehovah(self, coords: dict) -> float:
        return abs(coords['love'] - self.anchor_point['love']) + \
               abs(coords['justice'] - self.anchor_point['justice']) + \
               abs(coords['power'] - self.anchor_point['power']) + \
               abs(coords['wisdom'] - self.anchor_point['wisdom'])

    def biblical_balance(self, coords: dict) -> float:
        values = list(coords.values())
        std_dev = np.std(values)
        return max(0, 1 - (std_dev / 0.5))
