"""
MeaningModel: The Core of the 4D Meaning-Based System

This class is responsible for all calculations related to the 4D meaning model,
including coordinate generation, semantic distance, and divine resonance.
It is designed to be a deterministic and transparent implementation of the
principles outlined in the foundational documents.
"""
import hashlib
import math
import numpy as np
import re

class MeaningModel:
    """
    Calculates 4D meaning coordinates (Love, Justice, Power, Wisdom) for text.
    """

    def __init__(self):
        """Initializes the MeaningModel."""
        self.dimension_weights = {
            'love': 1.0,
            'justice': 1.0,
            'power': 1.0,
            'wisdom': 1.0
        }
        self.anchor_point = {'love': 1.0, 'justice': 1.0, 'power': 1.0, 'wisdom': 1.0}
        self.stop_words = set([
            "a", "about", "above", "after", "again", "against", "all", "am", "an", "and",
            "any", "are", "as", "at", "be", "because", "been", "before",
            "being", "below", "between", "both", "but", "by", "can't", "cannot",
            "could", "did", "do", "does", "doing",
            "down", "during", "each", "few", "for", "from", "further", "had",
            "has", "have", "having", "he", "her", "here", "hers", "herself", "him",
            "himself", "his", "how", "i", "if", "in", "into", "is", "it", "its", "itself",
            "me", "more", "most", "my", "myself", "no", "nor",
            "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our",
            "ours", "ourselves", "out", "over", "own", "same", "she",
            "should", "so", "some", "such", "than", "that", "the", "their", "theirs", "them",
            "themselves", "then", "there", "these", "they", "this", "those",
            "through", "to", "too", "under", "until", "up", "very", "was", "we",
            "were", "what", "when", "where", "which", "while", "who", "whom",
            "why", "with", "would", "you", "your", "yours", "yourself", "yourselves"
        ])

    def calculate_coordinates(self, text: str, context: str = "biblical") -> dict:
        """
        Calculates the 4D meaning coordinates for a given text by averaging the
        coordinates of its individual words, ignoring stop words.
        """
        words = re.findall(r'\b\w+\b', text.lower())
        meaningful_words = [word for word in words if word not in self.stop_words]

        if not meaningful_words:
            meaningful_words = words

        if not meaningful_words:
            return {'love': 0.5, 'justice': 0.5, 'power': 0.5, 'wisdom': 0.5}

        word_coords_list = []
        for word in meaningful_words:
            hash_object = hashlib.sha256(f"{word}:{context}".encode())
            hash_hex = hash_object.hexdigest()

            word_coords = {
                'love': self._hash_to_float(hash_hex[0:16]),
                'justice': self._hash_to_float(hash_hex[16:32]),
                'power': self._hash_to_float(hash_hex[32:48]),
                'wisdom': self._hash_to_float(hash_hex[48:64])
            }
            word_coords_list.append(word_coords)

        avg_coords = {
            'love': np.mean([c['love'] for c in word_coords_list]),
            'justice': np.mean([c['justice'] for c in word_coords_list]),
            'power': np.mean([c['power'] for c in word_coords_list]),
            'wisdom': np.mean([c['wisdom'] for c in word_coords_list])
        }

        return {
            'love': avg_coords['love'] * self.dimension_weights['love'],
            'justice': avg_coords['justice'] * self.dimension_weights['justice'],
            'power': avg_coords['power'] * self.dimension_weights['power'],
            'wisdom': avg_coords['wisdom'] * self.dimension_weights['wisdom']
        }

    def _hash_to_float(self, hex_string: str) -> float:
        """Converts a hexadecimal string to a float between 0 and 1."""
        return int(hex_string, 16) / (16**len(hex_string))

    def semantic_distance(self, coords1: dict, coords2: dict) -> float:
        """
        Calculates the Euclidean distance between two sets of 4D coordinates.
        """
        return math.sqrt(
            (coords1['love'] - coords2['love'])**2 +
            (coords1['justice'] - coords2['justice'])**2 +
            (coords1['power'] - coords2['power'])**2 +
            (coords1['wisdom'] - coords2['wisdom'])**2
        )

    def divine_resonance(self, coords: dict) -> float:
        """
        Calculates the divine resonance of a set of coordinates.
        """
        distance = self.semantic_distance(coords, self.anchor_point)
        return max(0, 1 - (distance / 2.0))

    def distance_from_jehovah(self, coords: dict) -> float:
        """
        Calculates the Manhattan distance from the Anchor Point (1,1,1,1).
        """
        return abs(coords['love'] - self.anchor_point['love']) + \
               abs(coords['justice'] - self.anchor_point['justice']) + \
               abs(coords['power'] - self.anchor_point['power']) + \
               abs(coords['wisdom'] - self.anchor_point['wisdom'])

    def biblical_balance(self, coords: dict) -> float:
        """
        Calculates the balance between the 4D coordinates.
        """
        values = list(coords.values())
        std_dev = np.std(values)
        return max(0, 1 - (std_dev / 0.5))

    def harmony_index(self, coords: dict) -> float:
        """
        Calculates the harmony index of a set of coordinates.
        """
        distance = self.semantic_distance(coords, self.anchor_point)
        return 1 / (1 + distance)

    def truth_sense(self, text: str, context: str = "biblical") -> float:
        """
        Calculates the truth score of a text based on its Justice coordinate.
        """
        coords = self.calculate_coordinates(text, context)
        biblical_truth_justice = 0.9
        deception_score = abs(coords['justice'] - biblical_truth_justice)
        truth_score = 1 - deception_score
        return truth_score
