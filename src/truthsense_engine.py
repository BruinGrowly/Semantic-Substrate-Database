"""
TRUTHSENSE DECEPTION DETECTION SYSTEM
Primer v2.1 Implementation

Identifies diabolical subversion patterns using optimized phi-analysis
across all frameworks. Implements spiritual warfare-grade truth verification.

Core Capabilities:
- Truth resonance detection
- Deception pattern identification (truth_wrapping, historical_drift, etc.)
- Framework violation detection
- Risk assessment classification
- Worship direction verification

Author: Semantic Substrate Database Project - Primer v2.1 Integration
License: MIT
"""

import math
import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field
from enum import Enum

# Import required components
try:
    from meaning_model import MeaningModel
    from phi_geometric_engine import GoldenSpiral, PHI, GOLDEN_ANGLE_DEG
except ImportError:
    from .meaning_model import MeaningModel
    from .phi_geometric_engine import GoldenSpiral, PHI, GOLDEN_ANGLE_DEG


class RiskLevel(Enum):
    """Risk classification levels for doctrines and teachings"""
    NO_RISK = "no_risk"
    LOW_RISK = "low_risk"
    MEDIUM_RISK = "medium_risk"
    HIGH_RISK = "high_risk"
    EXTREME_RISK = "extreme_risk"


class DeceptionPattern(Enum):
    """Types of deception patterns detectable by TruthSense"""
    TRUTH_WRAPPING = "truth_wrapping"
    HISTORICAL_DRIFT = "historical_drift"
    WORSHIP_REDIRECT = "worship_redirect"
    COMPLEXITY_OBFUSCATION = "complexity_obfuscation"
    FRAMEWORK_VIOLATION = "framework_violation"
    LOV_VIOLATION = "lov_framework_violation"
    GOD_SUBVERSION = "god_framework_subversion"


@dataclass
class TruthResonanceResult:
    """Results from truth resonance detection"""
    surface_truth: float  # 0.0-1.0 surface level truth content
    deep_truth: float  # 0.0-1.0 core truth alignment
    phi_harmony: float  # 0.0-1.0 golden ratio harmony score
    anchor_distance: float  # Distance from Anchor Point A (1,1,1,1)
    divine_resonance: float  # 0.0-1.0 alignment with divine perfection
    biblical_alignment: float  # 0.0-1.0 alignment with biblical standards
    deception_indicators: List[DeceptionPattern] = field(default_factory=list)
    risk_level: RiskLevel = RiskLevel.NO_RISK
    analysis_details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SubversionIndicator:
    """Individual indicator of potential subversion"""
    pattern: DeceptionPattern
    severity: float  # 0.0-1.0
    description: str
    evidence: List[str] = field(default_factory=list)
    phi_analysis: Optional[float] = None


class TruthSenseEngine:
    """
    TruthSense Deception Detection Engine

    Implements Primer v2.1 truthsense_capabilities for identifying
    diabolical subversion patterns and measuring truth resonance.
    """

    def __init__(self):
        """Initialize TruthSense engine"""
        self.meaning_model = MeaningModel()
        self.golden_spiral = GoldenSpiral()

        # Anchor Point A (1,1,1,1) - Fundamental Reality
        self.anchor_point = {
            'love': 1.0,
            'justice': 1.0,
            'power': 1.0,
            'wisdom': 1.0
        }

        # Risk thresholds from Primer v2.1
        self.risk_thresholds = {
            'phi_harmony': {
                'no_risk': 0.9,
                'low_risk': 0.7,
                'medium_risk': 0.5,
                'high_risk': 0.3,
                'extreme_risk': 0.0
            },
            'truth_divergence': {
                'truth_wrapping': 0.2,  # >80% surface, <60% deep = >20% divergence
                'worship_redirect': 0.05,  # Any redirect > 5%
                'complexity': 0.4  # High complexity with low biblical support
            }
        }

        # Jehovah-centric worship threshold
        self.jehovah_worship_threshold = 0.95

    def analyze_truth_resonance(
        self,
        text: str,
        context: str = "biblical",
        historical_forms: Optional[List[Tuple[str, str]]] = None
    ) -> TruthResonanceResult:
        """
        Comprehensive truth resonance analysis

        Args:
            text: Text to analyze
            context: Semantic context
            historical_forms: Optional list of (era, text) tuples for drift analysis

        Returns:
            TruthResonanceResult with complete analysis
        """
        # Calculate semantic coordinates
        coords = self.meaning_model.calculate_coordinates(text, context)

        # Calculate surface truth (initial impression)
        surface_truth = self._calculate_surface_truth(text, coords)

        # Calculate deep truth (core alignment)
        deep_truth = self._calculate_deep_truth(coords)

        # Calculate phi harmony score
        phi_harmony = self._calculate_phi_harmony(coords)

        # Calculate anchor distance and divine resonance
        anchor_distance = self.meaning_model.semantic_distance(coords, self.anchor_point)
        divine_resonance = self.meaning_model.divine_resonance(coords)

        # Calculate biblical alignment
        biblical_alignment = self._calculate_biblical_alignment(coords)

        # Detect deception patterns
        deception_indicators = self._detect_deception_patterns(
            text, coords, surface_truth, deep_truth, phi_harmony, historical_forms
        )

        # Classify risk level
        risk_level = self._classify_risk_level(phi_harmony, deception_indicators)

        # Compile analysis details
        analysis_details = {
            'coordinates': coords,
            'truth_divergence': abs(surface_truth - deep_truth),
            'phi_harmony_score': phi_harmony,
            'anchor_alignment': 1.0 - (anchor_distance / 2.0),
            'deception_count': len(deception_indicators),
            'historical_drift': self._analyze_historical_drift(historical_forms) if historical_forms else None
        }

        return TruthResonanceResult(
            surface_truth=surface_truth,
            deep_truth=deep_truth,
            phi_harmony=phi_harmony,
            anchor_distance=anchor_distance,
            divine_resonance=divine_resonance,
            biblical_alignment=biblical_alignment,
            deception_indicators=[ind.pattern for ind in deception_indicators],
            risk_level=risk_level,
            analysis_details=analysis_details
        )

    def _calculate_surface_truth(self, text: str, coords: Dict[str, float]) -> float:
        """
        Calculate surface-level truth content

        Measures immediate, apparent truth without deep analysis
        """
        # Count biblical keywords
        biblical_keywords = [
            'jehovah', 'god', 'jesus', 'christ', 'holy', 'spirit', 'scripture',
            'bible', 'truth', 'righteous', 'love', 'wisdom', 'justice', 'faith'
        ]

        text_lower = text.lower()
        keyword_count = sum(1 for kw in biblical_keywords if kw in text_lower)
        keyword_score = min(1.0, keyword_count / 5.0)  # Normalize to 1.0

        # Average coordinate values (higher = more positive content)
        coord_average = (coords['love'] + coords['justice'] +
                        coords['power'] + coords['wisdom']) / 4.0

        # Combine keyword presence with coordinate strength
        return (keyword_score * 0.4 + coord_average * 0.6)

    def _calculate_deep_truth(self, coords: Dict[str, float]) -> float:
        """
        Calculate deep, core truth alignment

        Measures alignment with Anchor Point A (1,1,1,1)
        """
        # Deep truth is inverse of distance from Anchor
        distance = self.meaning_model.semantic_distance(coords, self.anchor_point)
        max_distance = 2.0  # Maximum possible distance in normalized space

        return 1.0 - (distance / max_distance)

    def _calculate_phi_harmony(self, coords: Dict[str, float]) -> float:
        """
        Calculate golden ratio harmony score

        True divine patterns follow phi proportions
        """
        values = [coords['love'], coords['justice'], coords['power'], coords['wisdom']]
        values_sorted = sorted(values, reverse=True)

        if len(values_sorted) < 2 or values_sorted[0] == 0:
            return 0.5  # Neutral if insufficient data

        # Check phi ratios between successive values
        phi_deviations = []
        for i in range(len(values_sorted) - 1):
            if values_sorted[i+1] > 0:
                ratio = values_sorted[i] / values_sorted[i+1]
                # Ideal ratio is phi (1.618)
                deviation = abs(ratio - PHI) / PHI
                phi_deviations.append(deviation)

        if not phi_deviations:
            return 0.5

        # Average deviation from phi
        avg_deviation = np.mean(phi_deviations)

        # Convert to harmony score (lower deviation = higher harmony)
        harmony = max(0.0, 1.0 - avg_deviation)

        return harmony

    def _calculate_biblical_alignment(self, coords: Dict[str, float]) -> float:
        """
        Calculate alignment with biblical standards

        Combines balance, resonance, and absolute values
        """
        # Biblical balance (harmony across dimensions)
        balance = self.meaning_model.biblical_balance(coords)

        # Divine resonance (closeness to Anchor A)
        resonance = self.meaning_model.divine_resonance(coords)

        # Absolute strength (average coordinate value)
        strength = (coords['love'] + coords['justice'] +
                   coords['power'] + coords['wisdom']) / 4.0

        # Weighted combination
        return (balance * 0.3 + resonance * 0.4 + strength * 0.3)

    def _detect_deception_patterns(
        self,
        text: str,
        coords: Dict[str, float],
        surface_truth: float,
        deep_truth: float,
        phi_harmony: float,
        historical_forms: Optional[List[Tuple[str, str]]]
    ) -> List[SubversionIndicator]:
        """
        Detect specific deception patterns per Primer v2.1
        """
        indicators = []

        # Pattern 1: Truth Wrapping
        truth_divergence = abs(surface_truth - deep_truth)
        if surface_truth > 0.8 and deep_truth < 0.6:
            indicators.append(SubversionIndicator(
                pattern=DeceptionPattern.TRUTH_WRAPPING,
                severity=truth_divergence,
                description=f"High surface truth ({surface_truth:.2f}) masking low deep truth ({deep_truth:.2f})",
                evidence=[
                    f"Surface truth: {surface_truth:.2%}",
                    f"Deep truth: {deep_truth:.2%}",
                    f"Divergence: {truth_divergence:.2%}"
                ],
                phi_analysis=phi_harmony
            ))

        # Pattern 2: Historical Drift
        if historical_forms and len(historical_forms) > 1:
            drift_score = self._analyze_historical_drift(historical_forms)
            if drift_score > 0.3:
                indicators.append(SubversionIndicator(
                    pattern=DeceptionPattern.HISTORICAL_DRIFT,
                    severity=drift_score,
                    description=f"Significant deviation from biblical foundations ({drift_score:.1%})",
                    evidence=[f"Drift from original: {drift_score:.2%}"],
                    phi_analysis=None
                ))

        # Pattern 3: Worship Redirect
        worship_alignment = self._detect_worship_redirect(text, coords)
        if worship_alignment < self.jehovah_worship_threshold:
            indicators.append(SubversionIndicator(
                pattern=DeceptionPattern.WORSHIP_REDIRECT,
                severity=1.0 - worship_alignment,
                description=f"Worship not exclusively directed to Jehovah ({worship_alignment:.1%})",
                evidence=[
                    f"Jehovah-centric alignment: {worship_alignment:.2%}",
                    f"Threshold: {self.jehovah_worship_threshold:.2%}"
                ],
                phi_analysis=coords['love']  # Love axis should point to Anchor
            ))

        # Pattern 4: Complexity Obfuscation
        complexity_score = self._calculate_complexity(text)
        if complexity_score > 0.7 and deep_truth < 0.5:
            indicators.append(SubversionIndicator(
                pattern=DeceptionPattern.COMPLEXITY_OBFUSCATION,
                severity=complexity_score * (1.0 - deep_truth),
                description=f"High complexity ({complexity_score:.1%}) obscuring simple truth",
                evidence=[
                    f"Complexity: {complexity_score:.2%}",
                    f"Deep truth: {deep_truth:.2%}"
                ],
                phi_analysis=phi_harmony
            ))

        # Pattern 5: Framework Violation
        framework_balance = min(coords['love'], coords['justice'],
                               coords['power'], coords['wisdom'])
        if framework_balance < 0.3:
            indicators.append(SubversionIndicator(
                pattern=DeceptionPattern.FRAMEWORK_VIOLATION,
                severity=1.0 - framework_balance,
                description="Imbalance in fundamental LJPW framework",
                evidence=[f"Minimum axis value: {framework_balance:.2%}"],
                phi_analysis=phi_harmony
            ))

        return indicators

    def _detect_worship_redirect(self, text: str, coords: Dict[str, float]) -> float:
        """
        Detect if worship is redirected away from Jehovah alone

        Returns: 0.0-1.0, where 1.0 = exclusive Jehovah worship
        """
        text_lower = text.lower()

        # Jehovah-centric indicators
        jehovah_indicators = ['jehovah', 'yahweh', 'father', 'god alone', 'one god']
        jehovah_score = sum(1 for ind in jehovah_indicators if ind in text_lower)

        # Redirect indicators (worship directed elsewhere)
        redirect_indicators = [
            'trinity', 'three persons', 'god the son', 'holy ghost person',
            'worship jesus', 'pray to mary', 'saint'
        ]
        redirect_score = sum(1 for ind in redirect_indicators if ind in text_lower)

        # Calculate alignment
        if jehovah_score + redirect_score == 0:
            # No worship language detected
            return 1.0  # Neutral - not applicable

        # Ratio of Jehovah-centric to total worship language
        alignment = jehovah_score / (jehovah_score + redirect_score)

        # Boost by love coordinate (should point toward Anchor A)
        love_boost = coords['love']

        return (alignment * 0.7 + love_boost * 0.3)

    def _calculate_complexity(self, text: str) -> float:
        """
        Calculate text complexity score

        Higher score = more complex/obscure language
        """
        words = text.split()
        if not words:
            return 0.0

        # Average word length
        avg_word_length = np.mean([len(word) for word in words])
        length_score = min(1.0, avg_word_length / 10.0)

        # Sentence complexity (words per sentence - rough approximation)
        sentence_count = max(1, text.count('.') + text.count('!') + text.count('?'))
        words_per_sentence = len(words) / sentence_count
        sentence_complexity = min(1.0, words_per_sentence / 30.0)

        # Philosophical/technical jargon
        complex_terms = [
            'ontological', 'epistemological', 'metaphysical', 'transcendent',
            'immanent', 'substantive', 'consubstantial', 'hypostatic'
        ]
        jargon_count = sum(1 for term in complex_terms if term in text.lower())
        jargon_score = min(1.0, jargon_count / 3.0)

        # Combined complexity
        return (length_score * 0.3 + sentence_complexity * 0.4 + jargon_score * 0.3)

    def _analyze_historical_drift(
        self,
        historical_forms: List[Tuple[str, str]]
    ) -> float:
        """
        Analyze drift from original biblical teaching

        Args:
            historical_forms: List of (era, text) tuples in chronological order

        Returns:
            Drift score 0.0-1.0 (0 = no drift, 1 = complete divergence)
        """
        if not historical_forms or len(historical_forms) < 2:
            return 0.0

        # Calculate coordinates for each historical form
        coord_series = []
        for era, text in historical_forms:
            coords = self.meaning_model.calculate_coordinates(text, "biblical")
            coord_series.append((era, coords))

        # Calculate drift from original to most recent
        original_coords = coord_series[0][1]
        current_coords = coord_series[-1][1]

        drift_distance = self.meaning_model.semantic_distance(
            original_coords, current_coords
        )

        # Normalize to 0-1 scale
        max_drift = 2.0  # Maximum possible drift in normalized space
        drift_score = min(1.0, drift_distance / max_drift)

        return drift_score

    def _classify_risk_level(
        self,
        phi_harmony: float,
        deception_indicators: List[SubversionIndicator]
    ) -> RiskLevel:
        """
        Classify overall risk level based on phi harmony and deception patterns
        """
        # Primary classification by phi harmony
        if phi_harmony >= 0.9 and len(deception_indicators) == 0:
            return RiskLevel.NO_RISK
        elif phi_harmony >= 0.7 and len(deception_indicators) <= 1:
            return RiskLevel.LOW_RISK
        elif phi_harmony >= 0.5:
            return RiskLevel.MEDIUM_RISK
        elif phi_harmony >= 0.3:
            return RiskLevel.HIGH_RISK
        else:
            return RiskLevel.EXTREME_RISK

    def rapid_risk_assessment(
        self,
        text: str,
        context: str = "biblical"
    ) -> Dict[str, Any]:
        """
        Rapid risk assessment per Primer v2.1 testing_protocols_enhanced

        Quick initial screening before deep analysis
        """
        coords = self.meaning_model.calculate_coordinates(text, context)

        # Quick checks
        surface_truth = self._calculate_surface_truth(text, coords)
        phi_harmony = self._calculate_phi_harmony(coords)
        worship_alignment = self._detect_worship_redirect(text, coords)
        complexity = self._calculate_complexity(text)

        # Initial risk classification
        needs_deep_analysis = (
            phi_harmony < 0.7 or
            worship_alignment < 0.95 or
            complexity > 0.6
        )

        return {
            'surface_truth': surface_truth,
            'phi_harmony': phi_harmony,
            'worship_alignment': worship_alignment,
            'complexity': complexity,
            'needs_deep_analysis': needs_deep_analysis,
            'initial_risk': self._classify_risk_level(phi_harmony, [])
        }


class BiblicalSafeguards:
    """
    Biblical Safeguards System

    Implements non-negotiable biblical standards and rejection criteria
    per Primer v2.1
    """

    def __init__(self):
        """Initialize biblical safeguards"""
        self.non_negotiable_standards = [
            "Jehovah alone is God (Deuteronomy 6:4)",
            "Worship Jehovah your God and serve only him (Matthew 4:10)",
            "Jesus Christ is God's Son and our mediator (1 Timothy 2:5)",
            "Holy Spirit is God's power and presence (Acts 1:8)",
            "Scripture as ultimate authority (2 Timothy 3:16-17)"
        ]

        self.rejection_criteria = [
            "Any doctrine redirecting worship from Jehovah alone",
            "Teachings contradicting Jesus' own statements",
            "Doctrines built primarily on philosophical reasoning",
            "Complex systems obscuring simple biblical truth",
            "Historical developments significantly deviating from apostolic teaching",
            "Framework corruption or imbalance"
        ]

    def verify_safeguards(
        self,
        text: str,
        truth_result: TruthResonanceResult
    ) -> Tuple[bool, List[str]]:
        """
        Verify text against biblical safeguards

        Returns:
            (passes: bool, violations: List[str])
        """
        violations = []

        # Check worship direction
        if DeceptionPattern.WORSHIP_REDIRECT in truth_result.deception_indicators:
            violations.append("Worship not exclusively directed to Jehovah alone")

        # Check for complexity obfuscation
        if DeceptionPattern.COMPLEXITY_OBFUSCATION in truth_result.deception_indicators:
            violations.append("Complex systems obscuring simple biblical truth")

        # Check for historical drift
        if DeceptionPattern.HISTORICAL_DRIFT in truth_result.deception_indicators:
            violations.append("Significant deviation from apostolic teaching")

        # Check framework balance
        if DeceptionPattern.FRAMEWORK_VIOLATION in truth_result.deception_indicators:
            violations.append("Framework corruption or imbalance")

        # Check overall alignment
        if truth_result.biblical_alignment < 0.6:
            violations.append("Insufficient biblical alignment")

        passes = len(violations) == 0
        return (passes, violations)
