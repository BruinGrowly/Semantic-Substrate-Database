"""
MeaningModel v2.4: Final Hybrid Model with Weighted Averaging

This definitive version introduces weighted averaging, giving more importance
to contextually relevant keywords. This creates the most robust, nuanced,
and accurate model, capable of discerning signal from noise.
"""
import math
import numpy as np
import re
from typing import Dict, List, Any

class MeaningModel:
    """
    Calculates 4D coordinates using a hybrid model with weighted averaging
    for the most accurate and robust semantic analysis.
    """

    def __init__(self):
        self.anchor_point = {'love': 1.0, 'justice': 1.0, 'power': 1.0, 'wisdom': 1.0}
        self.stop_words = set([
            "a", "about", "above", "after", "again", "against", "all", "am", "an", "and",
            "any", "are", "as", "at", "be", "because", "been", "before", "being",
            "below", "between", "both", "but", "by", "can", "did", "do", "does",
            "doing", "down", "during", "each", "few", "for", "from", "further",
            "had", "has", "have", "having", "he", "her", "here", "him", "his",
            "how", "i", "if", "in", "into", "is", "it", "its", "me", "more", "most",
            "my", "no", "nor", "not", "of", "off", "on", "once", "only", "or",
            "other", "our", "out", "over", "own", "same", "she", "should", "so",
            "some", "such", "than", "that", "the", "their", "them", "then",
            "there", "these", "they", "this", "those", "through", "to", "too",
            "under", "until", "up", "very", "was", "we", "were", "what", "when",
            "where", "which", "while", "who", "whom", "why", "with", "would",
            "you", "your"
        ])

    def _hash_to_float(self, hex_string: str) -> float:
        """Converts a hexadecimal string to a float between 0 and 1."""
        return int(hex_string, 16) / (16**len(hex_string))

    def _get_base_word_coords(self, word: str) -> Dict[str, float]:
        """Gets a deterministic base coordinate for a word using hashing."""
        import hashlib
        hash_object = hashlib.sha256(word.encode())
        hash_hex = hash_object.hexdigest()
        return {
            'love': self._hash_to_float(hash_hex[0:16]),
            'justice': self._hash_to_float(hash_hex[16:32]),
            'power': self._hash_to_float(hash_hex[32:48]),
            'wisdom': self._hash_to_float(hash_hex[48:64])
        }

    def calculate_coordinates(self, text: str, context_profile: Dict[str, Any]) -> dict:
        """
        Calculates 4D coordinates using the hybrid model with weighted averaging.
        """
        words = re.findall(r'\b\w+\b', text.lower())
        meaningful_words = [word for word in words if word not in self.stop_words]

        if not meaningful_words:
            meaningful_words = words
            if not meaningful_words:
                return {'love': 0.5, 'justice': 0.5, 'power': 0.5, 'wisdom': 0.5}

        final_word_coords_list = []
        word_weights = []
        for word in meaningful_words:
            base_coords = self._get_base_word_coords(word)

            contextual_influence = {'love': 0.0, 'justice': 0.0, 'power': 0.0, 'wisdom': 0.0}
            influence_count = 0

            for dim in ['love', 'justice', 'power', 'wisdom']:
                if word in context_profile[dim]['keywords']:
                    weight = context_profile[dim]['keywords'][word]
                    contextual_influence[dim] += weight
                    influence_count += 1

            # Use a higher weight for keywords to give them more influence
            word_weights.append(1.0 if influence_count > 0 else 0.1)

            if influence_count > 0:
                total_influence = sum(abs(v) for v in contextual_influence.values())
                if total_influence > 0:
                    norm_influence = {k: v / total_influence for k, v in contextual_influence.items()}
                else:
                    norm_influence = contextual_influence

                # Blend: 30% base, 70% contextual
                final_coords = {
                    dim: max(0, (base_coords[dim] * 0.3) + (norm_influence[dim] * 0.7))
                    for dim in base_coords
                }
            else:
                final_coords = base_coords

            final_word_coords_list.append(final_coords)

        if not final_word_coords_list:
             return {'love': 0.5, 'justice': 0.5, 'power': 0.5, 'wisdom': 0.5}

        # Use the new weighted average for the final coordinates
        avg_coords = {
            'love': np.average([c['love'] for c in final_word_coords_list], weights=word_weights),
            'justice': np.average([c['justice'] for c in final_word_coords_list], weights=word_weights),
            'power': np.average([c['power'] for c in final_word_coords_list], weights=word_weights),
            'wisdom': np.average([c['wisdom'] for c in final_word_coords_list], weights=word_weights)
        }

        return avg_coords

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
