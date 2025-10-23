"""
Context Detector: A tool for automatically detecting the context of a text.
"""

import re
from typing import Dict, List, Any

class ContextDetector:
    """
    Analyzes a piece of text and suggests the most appropriate context profile.
    """

    def __init__(self, profiles: List[Dict[str, Any]]):
        """
        Initializes the ContextDetector with a list of available context profiles.
        """
        self.profiles = profiles

    def detect(self, text: str) -> Dict[str, Any]:
        """
        Detects the most appropriate context for a given text by scoring it
        against all available context profiles.
        """
        words = re.findall(r'\b\w+\b', text.lower())
        best_profile = None
        highest_score = -1

        for profile in self.profiles:
            score = self._score_profile(words, profile)
            if score > highest_score:
                highest_score = score
                best_profile = profile

        return best_profile

    def _score_profile(self, words: List[str], profile: Dict[str, Any]) -> float:
        """
        Scores a text against a single context profile.
        """
        score = 0.0
        for dim in ['love', 'justice', 'power', 'wisdom']:
            for keyword in profile[dim]['keywords']:
                if keyword in words:
                    score += abs(profile[dim]['keywords'][keyword])
        return score
