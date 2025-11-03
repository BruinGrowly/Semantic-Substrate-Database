"""
Macro-Analysis Engine

This module provides functions for analyzing the entire semantic landscape of a
MeaningDatabase. It calculates high-level insights such as the "Semantic
Center of Gravity" and identifies "Clusters of Meaning."
"""

from typing import Dict, List
import numpy as np
from sklearn.cluster import KMeans

def calculate_semantic_center_of_gravity(concepts: List[dict]) -> Dict[str, float]:
    """
    Calculates the average 4D coordinates for a list of concepts.
    """
    if not concepts:
        return {'love': 0.0, 'justice': 0.0, 'power': 0.0, 'wisdom': 0.0}

    avg_coords = {
        'love': np.mean([c['love'] for c in concepts]),
        'justice': np.mean([c['justice'] for c in concepts]),
        'power': np.mean([c['power'] for c in concepts]),
        'wisdom': np.mean([c['wisdom'] for c in concepts])
    }

    return avg_coords

def identify_clusters_of_meaning(concepts: List[dict], num_clusters: int = 3) -> Dict[str, any]:
    """
    Identifies clusters of meaning within a list of concepts using K-Means.
    """
    if not concepts or len(concepts) < num_clusters:
        return {}

    coords_matrix = np.array([[c['love'], c['justice'], c['power'], c['wisdom']] for c in concepts])

    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    kmeans.fit(coords_matrix)

    clusters = {}
    for i in range(num_clusters):
        clusters[f"cluster_{i}"] = {
            "center": {
                'love': kmeans.cluster_centers_[i][0],
                'justice': kmeans.cluster_centers_[i][1],
                'power': kmeans.cluster_centers_[i][2],
                'wisdom': kmeans.cluster_centers_[i][3]
            },
            "concepts": []
        }

    for i, label in enumerate(kmeans.labels_):
        clusters[f"cluster_{label}"]["concepts"].append(concepts[i]['concept_text'])

    return clusters

def analyze_semantic_trends(concepts: List[dict]) -> Dict[str, any]:
    """
    Analyzes how the semantic center of gravity has shifted over time.
    """
    if not concepts:
        return {}

    # Sort concepts by creation time
    concepts.sort(key=lambda x: x['created_at'])

    # For simplicity, we'll just compare the first half to the second half
    midpoint = len(concepts) // 2

    first_half = concepts[:midpoint]
    second_half = concepts[midpoint:]

    if not first_half or not second_half:
        return {"message": "Not enough data to analyze trends."}

    center_first_half = calculate_semantic_center_of_gravity(first_half)
    center_second_half = calculate_semantic_center_of_gravity(second_half)

    trend = {
        'love': center_second_half['love'] - center_first_half['love'],
        'justice': center_second_half['justice'] - center_first_half['justice'],
        'power': center_second_half['power'] - center_first_half['power'],
        'wisdom': center_second_half['wisdom'] - center_first_half['wisdom']
    }

    return {
        "period_1_center": center_first_half,
        "period_2_center": center_second_half,
        "trend": trend
    }
