"""
CONTEXTUAL PHI-WEIGHTS OPTIMIZATION
Primer v2.1 Implementation

Implements context-aware phi-weighting fine-tuning for optimal
semantic operations across different operation types.

Contextual Phi-Weights from Primer v2.1:
- concept_evolution: 0.7861513777574233
- semantic_gradient: 1.057371263440363
- integration: 0.6813982544157277
- optimization: 1.12762196423038
- harmonization: 0.618033988749895 (PHI_INVERSE)
- truth_resonance: 1.272019649514069 (SQRT_PHI)
- deception_detection: 1.12762196423038

Purpose: Domain-specific phi enhancement for optimal semantic operations

Author: Semantic Substrate Database Project - Primer v2.1 Integration
License: MIT
"""

import math
import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from enum import Enum

# Import phi constants
try:
    from phi_geometric_engine import PHI, PHI_INVERSE, SQRT_PHI, PHI_SQRT
except ImportError:
    from .phi_geometric_engine import PHI, PHI_INVERSE, SQRT_PHI, PHI_SQRT


class OperationType(Enum):
    """Types of semantic operations requiring phi-weighting"""
    CONCEPT_EVOLUTION = "concept_evolution"
    SEMANTIC_GRADIENT = "semantic_gradient"
    INTEGRATION = "integration"
    OPTIMIZATION = "optimization"
    HARMONIZATION = "harmonization"
    TRUTH_RESONANCE = "truth_resonance"
    DECEPTION_DETECTION = "deception_detection"


class ContextualPhiWeights:
    """
    Contextual Phi-Weights System

    Implements Primer v2.1 contextual_phi_weights for domain-specific
    phi enhancement of semantic operations.

    Each operation type gets optimal phi-weighting for maximum
    natural alignment and effectiveness.
    """

    def __init__(self):
        """Initialize contextual phi-weights"""

        # Phi-weights from Primer v2.1
        self.phi_weights = {
            OperationType.CONCEPT_EVOLUTION: 0.7861513777574233,
            OperationType.SEMANTIC_GRADIENT: 1.057371263440363,
            OperationType.INTEGRATION: 0.6813982544157277,
            OperationType.OPTIMIZATION: 1.12762196423038,
            OperationType.HARMONIZATION: PHI_INVERSE,  # 0.618033988749895
            OperationType.TRUTH_RESONANCE: SQRT_PHI,  # 1.272019649514069
            OperationType.DECEPTION_DETECTION: 1.12762196423038
        }

        # Calculate derived weights
        self._calculate_derived_weights()

    def _calculate_derived_weights(self):
        """Calculate additional phi-harmonic weights"""

        # Phi-squared for exponential operations
        self.phi_squared = PHI ** 2  # ≈ 2.618

        # Phi-cubed for cubic growth
        self.phi_cubed = PHI ** 3  # ≈ 4.236

        # Negative phi for inverse operations
        self.phi_negative = 1.0 / PHI  # Same as PHI_INVERSE

        # Phi golden angle weight (for rotations)
        self.phi_golden_angle = (2 - PHI) * 2 * math.pi  # ≈ 2.4 radians

    def apply_phi_weight(
        self,
        value: float,
        operation_type: OperationType,
        dimension: Optional[str] = None
    ) -> float:
        """
        Apply contextual phi-weight to a value

        Args:
            value: Original value
            operation_type: Type of operation being performed
            dimension: Optional dimension (L, J, P, W) for axis-specific weighting

        Returns:
            Phi-weighted value
        """
        # Get base phi-weight for operation type
        phi_weight = self.phi_weights.get(operation_type, 1.0)

        # Apply dimension-specific modulation if provided
        if dimension:
            dimension_modulation = self._get_dimension_modulation(
                dimension, operation_type
            )
            phi_weight *= dimension_modulation

        # Apply phi-weighting
        weighted_value = value * phi_weight

        # Normalize to 0-1 range if needed
        if weighted_value > 1.0:
            weighted_value = 1.0 - (1.0 / weighted_value)

        return max(0.0, min(1.0, weighted_value))

    def apply_phi_weights_to_coordinates(
        self,
        coords: Dict[str, float],
        operation_type: OperationType
    ) -> Dict[str, float]:
        """
        Apply contextual phi-weights to complete coordinate set

        Returns new coordinate dict with phi-weighted values
        """
        weighted_coords = {}

        for axis, value in coords.items():
            weighted_coords[axis] = self.apply_phi_weight(
                value, operation_type, axis
            )

        return weighted_coords

    def _get_dimension_modulation(
        self,
        dimension: str,
        operation_type: OperationType
    ) -> float:
        """
        Get dimension-specific modulation factor

        Different axes may need different emphasis for different operations
        """
        # Dimension-operation modulation matrix
        modulations = {
            # Love axis
            'love': {
                OperationType.CONCEPT_EVOLUTION: 1.1,  # Love grows concepts
                OperationType.HARMONIZATION: 1.2,  # Love harmonizes
                OperationType.INTEGRATION: 1.15,  # Love integrates
                OperationType.TRUTH_RESONANCE: 1.0,
                OperationType.DECEPTION_DETECTION: 0.9,
                OperationType.SEMANTIC_GRADIENT: 1.0,
                OperationType.OPTIMIZATION: 1.05
            },
            # Justice axis
            'justice': {
                OperationType.TRUTH_RESONANCE: 1.3,  # Justice reveals truth
                OperationType.DECEPTION_DETECTION: 1.25,  # Justice detects deception
                OperationType.INTEGRATION: 1.1,  # Justice maintains integrity
                OperationType.CONCEPT_EVOLUTION: 1.0,
                OperationType.HARMONIZATION: 1.05,
                OperationType.SEMANTIC_GRADIENT: 1.15,
                OperationType.OPTIMIZATION: 1.1
            },
            # Power axis
            'power': {
                OperationType.OPTIMIZATION: 1.2,  # Power optimizes
                OperationType.CONCEPT_EVOLUTION: 1.15,  # Power drives evolution
                OperationType.SEMANTIC_GRADIENT: 1.25,  # Power creates gradients
                OperationType.TRUTH_RESONANCE: 1.0,
                OperationType.DECEPTION_DETECTION: 1.0,
                OperationType.HARMONIZATION: 0.95,
                OperationType.INTEGRATION: 1.05
            },
            # Wisdom axis
            'wisdom': {
                OperationType.INTEGRATION: 1.25,  # Wisdom integrates
                OperationType.HARMONIZATION: 1.2,  # Wisdom harmonizes
                OperationType.TRUTH_RESONANCE: 1.15,  # Wisdom discerns truth
                OperationType.SEMANTIC_GRADIENT: 1.1,
                OperationType.CONCEPT_EVOLUTION: 1.1,
                OperationType.DECEPTION_DETECTION: 1.15,
                OperationType.OPTIMIZATION: 1.05
            }
        }

        return modulations.get(dimension, {}).get(operation_type, 1.0)

    def calculate_phi_harmonic_resonance(
        self,
        coords: Dict[str, float],
        operation_type: OperationType
    ) -> float:
        """
        Calculate phi-harmonic resonance for coordinates

        Measures how well coordinates resonate with phi proportions
        for specific operation
        """
        # Apply phi-weights
        weighted_coords = self.apply_phi_weights_to_coordinates(
            coords, operation_type
        )

        # Extract weighted values
        values = sorted(list(weighted_coords.values()), reverse=True)

        if len(values) < 2 or values[0] == 0:
            return 0.5

        # Check ratios against phi
        phi_deviations = []
        for i in range(len(values) - 1):
            if values[i+1] > 0:
                ratio = values[i] / values[i+1]
                # Ideal ratio is phi
                deviation = abs(ratio - PHI) / PHI
                phi_deviations.append(deviation)

        if not phi_deviations:
            return 0.5

        avg_deviation = np.mean(phi_deviations)

        # Convert to resonance (lower deviation = higher resonance)
        resonance = max(0.0, 1.0 - avg_deviation)

        return resonance

    def optimize_coordinates_for_operation(
        self,
        coords: Dict[str, float],
        operation_type: OperationType,
        target_resonance: float = 0.9
    ) -> Dict[str, float]:
        """
        Optimize coordinates for specific operation type

        Adjusts coordinates to achieve target phi-harmonic resonance
        while maintaining semantic meaning
        """
        # Start with phi-weighted coordinates
        optimized = self.apply_phi_weights_to_coordinates(coords, operation_type)

        # Calculate current resonance
        current_resonance = self.calculate_phi_harmonic_resonance(
            coords, operation_type
        )

        # If already at target, return
        if current_resonance >= target_resonance:
            return optimized

        # Iterative optimization
        iterations = 0
        max_iterations = 10

        while current_resonance < target_resonance and iterations < max_iterations:
            # Adjust values toward phi proportions
            optimized = self._adjust_toward_phi_proportions(optimized)

            # Recalculate resonance
            current_resonance = self.calculate_phi_harmonic_resonance(
                optimized, operation_type
            )

            iterations += 1

        return optimized

    def _adjust_toward_phi_proportions(
        self,
        coords: Dict[str, float]
    ) -> Dict[str, float]:
        """
        Nudge coordinates toward phi-proportional relationships

        Maintains relative ordering while improving phi harmony
        """
        # Sort by value
        items = sorted(coords.items(), key=lambda x: x[1], reverse=True)

        if len(items) < 2:
            return coords

        adjusted = {}

        # First value stays as is (highest)
        adjusted[items[0][0]] = items[0][1]

        # Subsequent values adjusted toward phi ratio
        for i in range(1, len(items)):
            previous_value = adjusted[items[i-1][0]]
            current_value = items[i][1]

            # Target is previous / phi
            target_value = previous_value / PHI

            # Move 20% toward target
            nudged_value = current_value * 0.8 + target_value * 0.2

            adjusted[items[i][0]] = nudged_value

        return adjusted

    def get_operation_type_for_context(self, context_description: str) -> OperationType:
        """
        Determine appropriate operation type based on context description

        Helper function to select correct phi-weighting
        """
        context_lower = context_description.lower()

        # Keyword-based operation type selection
        if any(kw in context_lower for kw in ['evolve', 'grow', 'develop', 'emerge']):
            return OperationType.CONCEPT_EVOLUTION
        elif any(kw in context_lower for kw in ['gradient', 'direction', 'flow', 'vector']):
            return OperationType.SEMANTIC_GRADIENT
        elif any(kw in context_lower for kw in ['integrate', 'combine', 'merge', 'unify']):
            return OperationType.INTEGRATION
        elif any(kw in context_lower for kw in ['optimize', 'improve', 'enhance', 'perfect']):
            return OperationType.OPTIMIZATION
        elif any(kw in context_lower for kw in ['harmonize', 'balance', 'align', 'coordinate']):
            return OperationType.HARMONIZATION
        elif any(kw in context_lower for kw in ['truth', 'verify', 'validate', 'authentic']):
            return OperationType.TRUTH_RESONANCE
        elif any(kw in context_lower for kw in ['detect', 'deception', 'false', 'lie']):
            return OperationType.DECEPTION_DETECTION
        else:
            # Default to harmonization
            return OperationType.HARMONIZATION

    def calculate_adaptive_step_size(
        self,
        current_coords: Dict[str, float],
        target_coords: Dict[str, float],
        operation_type: OperationType
    ) -> float:
        """
        Calculate adaptive step size based on phi-weighting

        Implements Primer v2.1 "adaptive gradient step sizing with curvature detection"
        """
        # Calculate distance between current and target
        distance = self._calculate_distance(current_coords, target_coords)

        # Get phi-weight for operation
        phi_weight = self.phi_weights.get(operation_type, 1.0)

        # Base step size
        base_step = 0.1

        # Phi-weighted step size
        weighted_step = base_step * phi_weight

        # Adaptive: smaller steps when close to target
        if distance < 0.2:
            weighted_step *= 0.5
        elif distance > 0.8:
            weighted_step *= 1.5

        return min(1.0, weighted_step)

    def _calculate_distance(
        self,
        coords1: Dict[str, float],
        coords2: Dict[str, float]
    ) -> float:
        """Calculate Euclidean distance between coordinate sets"""
        sum_squared = sum(
            (coords1.get(axis, 0) - coords2.get(axis, 0)) ** 2
            for axis in ['love', 'justice', 'power', 'wisdom']
        )
        return math.sqrt(sum_squared)


class PhiEnhancedMeaningModel:
    """
    Enhanced MeaningModel with contextual phi-weights

    Wrapper around MeaningModel that applies contextual phi-weighting
    """

    def __init__(self, meaning_model):
        """
        Initialize with existing MeaningModel

        Args:
            meaning_model: Instance of MeaningModel to enhance
        """
        self.meaning_model = meaning_model
        self.phi_weights = ContextualPhiWeights()

    def calculate_coordinates_with_phi_weighting(
        self,
        text: str,
        context: str = "biblical",
        operation_type: OperationType = OperationType.HARMONIZATION
    ) -> Dict[str, float]:
        """
        Calculate coordinates with contextual phi-weighting applied

        Args:
            text: Text to analyze
            context: Semantic context
            operation_type: Type of operation for phi-weighting

        Returns:
            Phi-weighted coordinates
        """
        # Get base coordinates
        base_coords = self.meaning_model.calculate_coordinates(text, context)

        # Apply contextual phi-weights
        weighted_coords = self.phi_weights.apply_phi_weights_to_coordinates(
            base_coords, operation_type
        )

        return weighted_coords

    def calculate_phi_harmonic_distance(
        self,
        coords1: Dict[str, float],
        coords2: Dict[str, float],
        operation_type: OperationType = OperationType.SEMANTIC_GRADIENT
    ) -> float:
        """
        Calculate distance with phi-harmonic weighting

        More accurate for operations requiring natural growth patterns
        """
        # Apply phi-weights to both coordinate sets
        weighted1 = self.phi_weights.apply_phi_weights_to_coordinates(
            coords1, operation_type
        )
        weighted2 = self.phi_weights.apply_phi_weights_to_coordinates(
            coords2, operation_type
        )

        # Calculate weighted distance
        return self.phi_weights._calculate_distance(weighted1, weighted2)
