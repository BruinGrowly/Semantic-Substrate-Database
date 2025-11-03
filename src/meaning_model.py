"""
MeaningModel: The Core of the 4D Meaning-Based System

This class is responsible for all calculations related to the 4D meaning model,
including coordinate generation, semantic distance, and divine resonance.
It is designed to be a deterministic and transparent implementation of the
principles outlined in the foundational documents.
"""
import math
import numpy as np
from src.baseline_biblical_substrate import BiblicalSemanticSubstrate

class MeaningModel:
    """
    Calculates 4D meaning coordinates (Love, Justice, Power, Wisdom) for text,
    leveraging the BiblicalSemanticSubstrate for nuanced, domain-specific analysis.
    """

    def __init__(self, semantic_engine: BiblicalSemanticSubstrate):
        """Initializes the MeaningModel."""
        self.semantic_engine = semantic_engine
        self.anchor_point = {'love': 1.0, 'justice': 1.0, 'power': 1.0, 'wisdom': 1.0}

    def calculate_coordinates(self, text: str, context: str = "biblical") -> dict:
        """
        Calculates the 4D meaning coordinates for a given text using the
        BiblicalSemanticSubstrate engine.
        """
        biblical_coords = self.semantic_engine.analyze_concept(text, context)
        return {
            'love': biblical_coords.love,
            'justice': biblical_coords.justice,
            'power': biblical_coords.power,
            'wisdom': biblical_coords.wisdom
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

    def truth_sense(self, text: str, context: str = "biblical") -> float:
        """
        Calculates the 'truth sense' of a text by measuring its semantic
        distance from the concept of 'divine truth'.
        """
        text_coords = self.calculate_coordinates(text, context)
        truth_coords = self.calculate_coordinates("divine truth", "biblical")
        distance = self.semantic_distance(text_coords, truth_coords)
        return max(0.0, 1.0 - distance)
