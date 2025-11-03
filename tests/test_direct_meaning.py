"""
Demonstration of Direct Meaning Comprehension

This script provides a practical demonstration of the system's ability to
understand direct meaning, similar to a transformer model. It shows that
semantically similar phrases have close 4D coordinates, while dissimilar
phrases are far apart.
"""

import sys
import os

# Ensure the src package is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from meaning_model import MeaningModel
from baseline_biblical_substrate import BiblicalSemanticSubstrate
from ice_framework import ICEFramework

def run_demonstration():
    """Runs the direct meaning demonstration."""
    print("="*80)
    print("DEMONSTRATION: Direct Meaning Comprehension")
    print("="*80)
    print("This test will calculate the 4D coordinates for several phrases.")
    print("It will then measure the semantic distance between them to prove")
    print("that the system understands meaning, not just syntax.\n")

    # Instantiate the classes with dependency injection
    meaning_model = MeaningModel(None)
    ice_framework = ICEFramework(meaning_model)
    semantic_engine = BiblicalSemanticSubstrate(ice_framework)
    meaning_model.semantic_engine = semantic_engine


    # Define phrases
    phrases = {
        "Divine Love 1": "God's love is infinite and unconditional.",
        "Divine Love 2": "The Creator's compassion is boundless.",
        "Divine Justice": "Righteousness and truth are the foundation of the throne.",
        "Opposing Concept": "Hate and deceit are virtues."
    }

    # Calculate coordinates
    print("1. Calculating 4D Coordinates...")
    coordinates = {name: meaning_model.calculate_coordinates(text) for name, text in phrases.items()}
    for name, coords in coordinates.items():
        print(f"  - {name}:")
        print(f"    Love: {coords['love']:.4f}, Justice: {coords['justice']:.4f}, Power: {coords['power']:.4f}, Wisdom: {coords['wisdom']:.4f}")
    print("\n")

    # Calculate semantic distances
    print("2. Calculating Semantic Distances...")

    # Distance between similar concepts
    dist_love_love = meaning_model.semantic_distance(coordinates["Divine Love 1"], coordinates["Divine Love 2"])
    print(f"  - Distance between 'Divine Love 1' and 'Divine Love 2': {dist_love_love:.4f}")

    # Distance between different concepts
    dist_love_justice = meaning_model.semantic_distance(coordinates["Divine Love 1"], coordinates["Divine Justice"])
    print(f"  - Distance between 'Divine Love 1' and 'Divine Justice': {dist_love_justice:.4f}")

    # Distance between opposing concepts
    dist_love_hate = meaning_model.semantic_distance(coordinates["Divine Love 1"], coordinates["Opposing Concept"])
    print(f"  - Distance between 'Divine Love 1' and 'Opposing Concept': {dist_love_hate:.4f}")
    print("\n")

    # Analysis
    print("3. Analysis of Results...")
    if dist_love_love < 0.2:
        print("  - [SUCCESS] The semantic distance between the two 'Divine Love' phrases is very small.")
        print("              This demonstrates that the model understands that these phrases have similar meanings.")
    else:
        print("  - [FAIL] The semantic distance between the 'Divine Love' phrases is larger than expected.")

    if dist_love_justice > dist_love_love:
        print("  - [SUCCESS] The distance between 'Divine Love' and 'Divine Justice' is greater than the distance")
        print("              between the two love phrases, showing the model can distinguish between different concepts.")
    else:
        print("  - [FAIL] The model is not distinguishing between different concepts effectively.")

    if dist_love_hate > dist_love_justice:
        print("  - [SUCCESS] The distance between 'Divine Love' and the 'Opposing Concept' is the largest.")
        print("              This proves the model understands that these concepts are semantically opposite.")
    else:
        print("  - [FAIL] The model is not correctly identifying opposing concepts.")

    print("\n" + "="*80)
    print("Demonstration Complete")
    print("="*80)

if __name__ == "__main__":
    run_demonstration()
