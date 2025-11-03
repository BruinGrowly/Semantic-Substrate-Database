"""
Oracle Payload Generator

This module is responsible for generating the rich, insightful payload that is
appended to every concept retrieved from the MeaningDatabase. It transforms the
raw 4D coordinates into human-readable insights, warnings, and suggestions.
"""

from typing import Dict, List

def generate_oracle_payload(coords: Dict[str, float]) -> Dict[str, any]:
    """
    Generates the "oracle" payload based on a set of 4D coordinates.
    """
    insights = []
    warnings = []

    # Analyze the dominant attribute
    dominant_attribute = max(coords, key=coords.get)
    insights.append(f"This concept strongly projects '{dominant_attribute.capitalize()}'.")

    # Generate warnings based on low scores
    if coords['love'] < 0.3:
        warnings.append("Low alignment with 'Love'. May lack compassion or customer-centricity.")
    if coords['justice'] < 0.3:
        warnings.append("Potential 'Justice' deficit. Claims may be unsubstantiated or unfair.")
    if coords['power'] < 0.3:
        warnings.append("Low 'Power' score. May indicate a lack of conviction, resources, or viability.")
    if coords['wisdom'] < 0.3:
        warnings.append("Low 'Wisdom' score. The approach may be short-sighted or lack a clear plan.")

    # Generate growth suggestion
    growth_suggestion = "To improve balance, focus on strengthening the weaker coordinates. "
    if dominant_attribute == 'power' and coords['love'] < 0.5:
        growth_suggestion += "Specifically, consider how to frame the concept in a more collaborative and customer-focused way."

    return {
        "dominant_attribute": dominant_attribute.capitalize(),
        "insights": insights,
        "warnings": warnings,
        "growth_suggestion": growth_suggestion
    }
