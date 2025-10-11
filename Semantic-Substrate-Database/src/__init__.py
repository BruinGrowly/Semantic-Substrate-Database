"""
Semantic Substrate Database v2.0 - ICE-Centric Database System

A revolutionary database system that stores and queries semantic meaning using
the ICE (Intent-Context-Execution) framework with 4D divine coordinate system.
"""

from .semantic_substrate_database import SemanticSubstrateDatabase
from .ice_semantic_substrate_engine import ICESemanticSubstrateEngine
from .unified_ice_framework import UnifiedICEFramework
from .ultimate_core_engine import UltimateCoreEngine

__version__ = "2.0.0"
__author__ = "BruinGrowly"
__license__ = "MIT"

__all__ = [
    "SemanticSubstrateDatabase",
    "ICESemanticSubstrateEngine", 
    "UnifiedICEFramework",
    "UltimateCoreEngine"
]