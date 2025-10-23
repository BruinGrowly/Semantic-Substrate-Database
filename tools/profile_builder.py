"""
Context Profile Builder: A tool for creating new context profiles.
"""

import json
import sys

def build_profile(profile_data: dict):
    """
    Builds a new context profile from a dictionary and saves it to a file.
    """
    filename = f"{profile_data['name'].lower().replace(' ', '_')}_profile.json"
    with open(filename, 'w') as f:
        json.dump(profile_data, f, indent=4)

    print(f"--- Profile successfully built and saved to '{filename}' ---")
    return filename

def main():
    """
    A simple demonstration of the profile builder.
    """
    # In a real CLI, this would come from interactive input.
    # For this non-interactive environment, we define it directly.
    healthcare_profile = {
        "name": "Healthcare Context",
        "description": "A context for analyzing healthcare-related text.",
        "love": {
            "interpretation": "Patient Care & Empathy",
            "keywords": {"care": 1.0, "empathy": 1.0, "healing": 0.8}
        },
        "justice": {
            "interpretation": "Equity & Access",
            "keywords": {"equity": 1.0, "access": 1.0, "fairness": 0.8}
        },
        "power": {
            "interpretation": "Efficacy & Treatment Strength",
            "keywords": {"effective": 1.0, "cure": 0.9, "treatment": 0.8}
        },
        "wisdom": {
            "interpretation": "Diagnosis & Medical Knowledge",
            "keywords": {"diagnosis": 1.0, "research": 0.8, "knowledge": 0.9}
        }
    }

    build_profile(healthcare_profile)

if __name__ == "__main__":
    main()
