"""
Context Profiles for the Purpose-Aware MeaningModel v2.2 (with N-gram support)
"""

BIBLICAL_CONTEXT_PROFILE = {
    "name": "Biblical Context",
    "description": "A general-purpose context profile for analyzing text from a biblical perspective.",
    "love": {
        "interpretation": "Divine Love & Compassion",
        "keywords": {
            "love": 1.0, "compassion": 0.8, "grace": 0.9, "mercy": 0.8, "kindness": 0.7,
            "compassionate": 0.8
        }
    },
    "justice": {
        "interpretation": "Righteousness & Moral Law",
        "keywords": {
            "justice": 1.0, "righteousness": 0.9, "law": 0.7, "truth": 0.8, "holy": 0.8,
            "right": 0.8
        }
    },
    "power": {
        "interpretation": "Divine Power & Sovereignty",
        "keywords": {
            "power": 1.0, "sovereignty": 0.9, "almighty": 0.9, "miracle": 0.7, "authority": 0.8
        }
    },
    "wisdom": {
        "interpretation": "Divine Wisdom & Understanding",
        "keywords": {
            "wisdom": 1.0, "understanding": 0.9, "knowledge": 0.8, "discernment": 0.8, "proverbs": 0.7
        }
    }
}


FINANCIAL_CONTEXT_PROFILE = {
    "name": "Financial Institution Context",
    "description": "A context profile for analyzing financial documents, such as loan applications, with n-gram support.",
    "love": {
        "interpretation": "Fiduciary Duty & Customer Success",
        "keywords": {
            # Unigrams
            "growth": 1.0, "community": 0.8, "success": 0.8, "family": 0.7,
            "home": 0.7, "opportunity": 0.6, "dream": 0.5, "improve": 0.5,
            "build": 0.6, "support": 0.9, "relationship": 0.7, "local": 0.8,
            # N-grams (negative)
            "predatory": -1.0, "high-pressure": -0.8, "sales tactic": -0.8,
            # N-grams (positive)
            "customer success": 1.0, "community growth": 1.0, "first-time buyer": 0.8
        }
    },
    "justice": {
        "interpretation": "Fairness & Compliance",
        "keywords": {
            # Unigrams
            "fair": 1.0, "compliant": 1.0, "equitable": 0.8, "unbiased": 0.8,
            "regulation": 0.7, "access": 0.6, "transparent": 0.7,
            "responsible": 0.8, "legal": 0.9,
            # N-grams (negative)
            "questionable": -1.0, "non-compliant": -1.0, "unclear terms": -1.0,
            "legally questionable": -1.0, "hidden fees": -1.0
        }
    },
    "power": {
        "interpretation": "Financial Viability & Risk",
        "keywords": {
            # Unigrams
            "assets": 1.0, "income": 1.0, "credit": 0.9, "collateral": 0.8,
            "capital": 0.9, "profitable": 0.7, "equity": 0.8, "leverage": 0.6,
            "revenue": 0.9, "stable": 0.8, "secure": 0.8, "strong": 0.9,
            # N-grams (negative)
            "unstable income": -0.9, "high-risk": -1.0, "high risk": -1.0,
            "credit card debt": -0.7
        }
    },
    "wisdom": {
        "interpretation": "Prudence & Data-Driven Insight",
        "keywords": {
            # Unigrams
            "prudent": 1.0, "strategic": 0.8, "forecast": 0.7,
            "experienced": 0.8, "plan": 0.9, "sustainable": 0.7,
            "insight": 0.9, "analysis": 0.8, "proven": 0.8,
            # N-grams (positive)
            "data-driven": 0.9, "long-term": 0.8, "financial plan": 1.0,
            # N-grams (negative)
            "impulsive": -0.7, "quick returns": -0.8
        }
    }
}
