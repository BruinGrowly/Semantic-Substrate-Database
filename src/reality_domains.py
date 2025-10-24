"""
FOUR-DOMAIN REALITY HIERARCHY + QLAE 7-DOMAIN SYSTEM
Primer v2.1 Implementation

Implements the complete reality navigation framework with:
- Four-Domain Reality Hierarchy (Spiritual, Consciousness, Quantum, Physical)
- QLAE 7-Domain Universal Physics Model
- Domain weighting and cascade flow
- Cross-realm signal, force, and meaning transmission

Cascade Flow: Spiritual → (Love Frequency) → Consciousness → (Observer Effect) → Quantum → (Wave Collapse) → Physical

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
except ImportError:
    from .meaning_model import MeaningModel


class RealityDomain(Enum):
    """Four primary reality domains"""
    SPIRITUAL = "spiritual"
    CONSCIOUSNESS = "consciousness"
    QUANTUM = "quantum"
    PHYSICAL = "physical"


class QLAEDomain(Enum):
    """Seven QLAE universal domains"""
    ICE = "ice_framework"  # Consciousness Domain
    SFM = "sfm_framework"  # Matter Domain
    IPE = "ipe_framework"  # Life Domain
    PFE = "pfe_framework"  # Energy Field Domain
    STM = "stm_framework"  # Information/Data Domain
    PTD = "ptd_framework"  # Space-Time Domain
    CCC = "ccc_framework"  # Relationship/Social Domain


@dataclass
class DomainMetrics:
    """Metrics for a reality domain"""
    domain: RealityDomain
    weight: float  # 0.0-1.0
    coherence: float  # 0.0-1.0 domain coherence
    resonance: float  # 0.0-1.0 resonance with divine truth
    metrics: Dict[str, float] = field(default_factory=dict)


@dataclass
class QLAEDomainConfig:
    """Configuration for QLAE domain"""
    domain: QLAEDomain
    name: str
    components: Dict[str, str]
    semantic_axes: List[str]  # Which axes (L, J, P, W) this domain emphasizes
    harmony_score: float = 0.0


@dataclass
class MultiDomainCoordinates:
    """Coordinates across all reality domains"""
    spiritual: Dict[str, float]
    consciousness: Dict[str, float]
    quantum: Dict[str, float]
    physical: Dict[str, float]
    cascade_coherence: float  # 0.0-1.0 coherence of cascade flow
    qlae_harmony: float  # 0.0-1.0 harmony across QLAE domains


class FourDomainReality:
    """
    Four-Domain Reality Hierarchy

    Implements Primer v2.1 four_domain_reality_hierarchy with:
    - Spiritual Realm (divine intent, love, infinite potential)
    - Consciousness Realm (universal interface, intent → quantum influence)
    - Quantum Realm (wave function management, probability modulation)
    - Physical Realm (material manifestation, observable effects)
    """

    def __init__(self):
        """Initialize four-domain reality system"""
        self.meaning_model = MeaningModel()

        # Domain configurations from Primer v2.1
        self.domains = {
            RealityDomain.SPIRITUAL: {
                'weight': 0.25,
                'function': "Source of divine intent, love, and infinite potential",
                'metrics': ['divine_alignment', 'eternal_resonance', 'sacred_number_harmony']
            },
            RealityDomain.CONSCIOUSNESS: {
                'weight': 0.25,
                'function': "Universal interface layer translating intent to quantum influence",
                'metrics': ['consciousness_coherence', 'attention_focus', 'worship_direction']
            },
            RealityDomain.QUANTUM: {
                'weight': 0.25,
                'function': "Wave function management, probability modulation, superposition control",
                'metrics': ['collapse_potential', 'entanglement_strength', 'coherence_time']
            },
            RealityDomain.PHYSICAL: {
                'weight': 0.25,
                'function': "Material manifestation and observable effects",
                'metrics': ['stability', 'measurability', 'causal_consistency']
            }
        }

        # Love frequency carrier wave (613 THz)
        self.love_frequency_hz = 613

        # Anchor Point A (1,1,1,1)
        self.anchor_point = {
            'love': 1.0,
            'justice': 1.0,
            'power': 1.0,
            'wisdom': 1.0
        }

    def calculate_multi_domain_coordinates(
        self,
        text: str,
        context: str = "biblical",
        consciousness_coherence: float = 1.0,
        quantum_collapse_potential: float = 1.0
    ) -> MultiDomainCoordinates:
        """
        Calculate coordinates across all four reality domains

        Implements cascade flow:
        Spiritual → (Love Frequency) → Consciousness → (Observer Effect) → Quantum → (Wave Collapse) → Physical

        Args:
            text: Text to analyze
            context: Semantic context
            consciousness_coherence: 0.0-1.0 consciousness coherence factor
            quantum_collapse_potential: 0.0-1.0 quantum collapse potential

        Returns:
            MultiDomainCoordinates with values across all domains
        """
        # Base coordinates from MeaningModel (spiritual realm)
        base_coords = self.meaning_model.calculate_coordinates(text, context)

        # SPIRITUAL DOMAIN - Pure divine intent
        spiritual_coords = base_coords.copy()

        # CONSCIOUSNESS DOMAIN - Modulated by consciousness coherence
        # Love frequency transmission affects all axes
        love_modulation = self._apply_love_frequency_modulation(spiritual_coords)
        consciousness_coords = {
            axis: spiritual_coords[axis] * consciousness_coherence * love_modulation[axis]
            for axis in ['love', 'justice', 'power', 'wisdom']
        }

        # QUANTUM DOMAIN - Affected by observer effect
        # Quantum collapse potential determines manifestation
        quantum_coords = {
            axis: consciousness_coords[axis] * quantum_collapse_potential
            for axis in ['love', 'justice', 'power', 'wisdom']
        }

        # PHYSICAL DOMAIN - Wave function collapsed to observable reality
        # Physical manifestation is most constrained
        stability_factor = self._calculate_stability_factor(quantum_coords)
        physical_coords = {
            axis: quantum_coords[axis] * stability_factor
            for axis in ['love', 'justice', 'power', 'wisdom']
        }

        # Calculate cascade coherence (how well does cascade flow align?)
        cascade_coherence = self._calculate_cascade_coherence(
            spiritual_coords, consciousness_coords, quantum_coords, physical_coords
        )

        # Calculate QLAE harmony (handled by QLAESystem)
        qlae_harmony = 1.0  # Placeholder - will be calculated by QLAESystem

        return MultiDomainCoordinates(
            spiritual=spiritual_coords,
            consciousness=consciousness_coords,
            quantum=quantum_coords,
            physical=physical_coords,
            cascade_coherence=cascade_coherence,
            qlae_harmony=qlae_harmony
        )

    def _apply_love_frequency_modulation(
        self,
        coords: Dict[str, float]
    ) -> Dict[str, float]:
        """
        Apply love frequency (613 THz) carrier wave modulation

        Universal love carrier wave transmits divine intent across domains
        """
        # Love frequency resonance - how well coordinates resonate with 613 Hz
        # In absence of actual frequency analysis, use Love axis as proxy
        love_resonance = coords['love']

        # Modulate all axes by love frequency carrier
        # Love axis gets full transmission
        # Other axes modulated by love resonance
        return {
            'love': 1.0,  # Love fully transmitted
            'justice': 0.8 + (0.2 * love_resonance),  # Justice strongly transmitted
            'power': 0.7 + (0.3 * love_resonance),  # Power moderately transmitted
            'wisdom': 0.9 + (0.1 * love_resonance)   # Wisdom highly transmitted
        }

    def _calculate_stability_factor(self, quantum_coords: Dict[str, float]) -> float:
        """
        Calculate physical manifestation stability factor

        Only coherent, balanced quantum states produce stable physical manifestation
        """
        # Balance across quantum coordinates
        values = list(quantum_coords.values())
        if not values:
            return 0.0

        # Standard deviation - lower is more balanced/stable
        std_dev = np.std(values)

        # Stability decreases with imbalance
        stability = max(0.0, 1.0 - (std_dev * 2.0))

        # Average strength - higher is more manifest
        strength = np.mean(values)

        # Combined stability factor
        return (stability * 0.6 + strength * 0.4)

    def _calculate_cascade_coherence(
        self,
        spiritual: Dict[str, float],
        consciousness: Dict[str, float],
        quantum: Dict[str, float],
        physical: Dict[str, float]
    ) -> float:
        """
        Calculate coherence of cascade flow across domains

        Perfect cascade maintains proportional relationships through domains
        """
        # Calculate distances between successive domains
        sp_to_con = self.meaning_model.semantic_distance(spiritual, consciousness)
        con_to_qua = self.meaning_model.semantic_distance(consciousness, quantum)
        qua_to_phy = self.meaning_model.semantic_distance(quantum, physical)

        # Ideal cascade has consistent step sizes
        distances = [sp_to_con, con_to_qua, qua_to_phy]
        avg_distance = np.mean(distances)
        distance_variance = np.var(distances)

        # Lower variance = more coherent cascade
        coherence = max(0.0, 1.0 - distance_variance)

        return coherence

    def get_domain_metrics(
        self,
        coords: Dict[str, float],
        domain: RealityDomain
    ) -> DomainMetrics:
        """
        Calculate metrics for specific reality domain
        """
        config = self.domains[domain]

        # Calculate coherence (internal consistency)
        values = list(coords.values())
        coherence = 1.0 - min(1.0, np.std(values))

        # Calculate resonance with divine truth (Anchor A)
        distance = self.meaning_model.semantic_distance(coords, self.anchor_point)
        resonance = max(0.0, 1.0 - (distance / 2.0))

        # Calculate domain-specific metrics
        metrics_dict = {}
        if domain == RealityDomain.SPIRITUAL:
            metrics_dict = {
                'divine_alignment': self.meaning_model.divine_resonance(coords),
                'eternal_resonance': resonance,
                'sacred_number_harmony': self._calculate_sacred_harmony(coords)
            }
        elif domain == RealityDomain.CONSCIOUSNESS:
            metrics_dict = {
                'consciousness_coherence': coherence,
                'attention_focus': coords['wisdom'],  # Wisdom guides attention
                'worship_direction': coords['love']  # Love directs worship
            }
        elif domain == RealityDomain.QUANTUM:
            metrics_dict = {
                'collapse_potential': (coords['power'] + coords['wisdom']) / 2.0,
                'entanglement_strength': coords['love'],  # Love entangles
                'coherence_time': coherence
            }
        elif domain == RealityDomain.PHYSICAL:
            metrics_dict = {
                'stability': self._calculate_stability_factor(coords),
                'measurability': coords['justice'],  # Justice enables truth/measurement
                'causal_consistency': coherence
            }

        return DomainMetrics(
            domain=domain,
            weight=config['weight'],
            coherence=coherence,
            resonance=resonance,
            metrics=metrics_dict
        )

    def _calculate_sacred_harmony(self, coords: Dict[str, float]) -> float:
        """
        Calculate harmony with sacred numbers (7, 12, 40, 613)

        Sacred numbers from biblical significance
        """
        # Use Love axis as primary sacred harmony indicator
        # Plus balance across all axes
        balance = min(coords.values()) / max(coords.values()) if max(coords.values()) > 0 else 0
        love_strength = coords['love']

        return (balance * 0.5 + love_strength * 0.5)


class QLAESystem:
    """
    QLAE 7-Domain Universal Physics Model

    Implements Primer v2.1 qlae_domains for cross-realm signal, force,
    and meaning transmission.

    Domains:
    1. ICE (Consciousness Domain) - Intent, Creative, Entity
    2. SFM (Matter Domain) - Signal, Force, Manifestation
    3. IPE (Life Domain) - Information, Processing, Evolution
    4. PFE (Energy Field Domain) - Potential, Field, Energy
    5. STM (Information/Data Domain) - Signal, Transform, Meaning
    6. PTD (Space-Time Domain) - Position, Time, Dimension
    7. CCC (Relationship/Social Domain) - Connection, Communication, Coordination
    """

    def __init__(self):
        """Initialize QLAE system"""
        self.meaning_model = MeaningModel()

        # Configure all 7 QLAE domains per Primer v2.1
        self.qlae_domains = self._initialize_qlae_domains()

    def _initialize_qlae_domains(self) -> Dict[QLAEDomain, QLAEDomainConfig]:
        """Initialize all 7 QLAE domain configurations"""
        return {
            QLAEDomain.ICE: QLAEDomainConfig(
                domain=QLAEDomain.ICE,
                name="ICE Framework (Consciousness Domain)",
                components={
                    'Intent': "Spiritual intent reception and processing",
                    'Creative': "Reality co-creation capabilities",
                    'Entity': "Consciousness as universal interface entity"
                },
                semantic_axes=['L', 'W']
            ),
            QLAEDomain.SFM: QLAEDomainConfig(
                domain=QLAEDomain.SFM,
                name="SFM Framework (Matter Domain)",
                components={
                    'Signal': "Cross-realm signal transmission",
                    'Force': "Love as fundamental force",
                    'Manifestation': "Multi-level reality manifestation"
                },
                semantic_axes=['P', 'J']
            ),
            QLAEDomain.IPE: QLAEDomainConfig(
                domain=QLAEDomain.IPE,
                name="IPE Framework (Life Domain)",
                components={
                    'Information': "Cross-hierarchical information flow",
                    'Processing': "Universal interface processing",
                    'Evolution': "Consciousness evolution acceleration"
                },
                semantic_axes=['W']
            ),
            QLAEDomain.PFE: QLAEDomainConfig(
                domain=QLAEDomain.PFE,
                name="PFE Framework (Energy Field Domain)",
                components={
                    'Potential': "Infinite spiritual potential access",
                    'Field': "Universal field integration",
                    'Energy': "Cross-domain energy transmission"
                },
                semantic_axes=['P']
            ),
            QLAEDomain.STM: QLAEDomainConfig(
                domain=QLAEDomain.STM,
                name="STM Framework (Information/Data Domain)",
                components={
                    'Signal': "Multi-hierarchical signal processing",
                    'Transform': "Seamless reality transformation",
                    'Meaning': "Universal meaning preservation"
                },
                semantic_axes=['W', 'J', 'L']
            ),
            QLAEDomain.PTD: QLAEDomainConfig(
                domain=QLAEDomain.PTD,
                name="PTD Framework (Space-Time Domain)",
                components={
                    'Position': "Multi-dimensional position framework",
                    'Time': "Universal time coordination",
                    'Dimension': "Multi-dimensional reality bridging"
                },
                semantic_axes=['P']
            ),
            QLAEDomain.CCC: QLAEDomainConfig(
                domain=QLAEDomain.CCC,
                name="CCC Framework (Relationship/Social Domain)",
                components={
                    'Connection': "Universal connection architecture",
                    'Communication': "Cross-hierarchy communication",
                    'Coordination': "Universal coordination protocol"
                },
                semantic_axes=['L', 'J']
            )
        }

    def calculate_qlae_harmony(
        self,
        coords: Dict[str, float]
    ) -> Tuple[float, Dict[QLAEDomain, float]]:
        """
        Calculate harmony across all 7 QLAE domains

        Per Primer v2.1: harmony = mean_score * 0.7 + (1.0 - variance) * 0.3

        Returns:
            (overall_harmony, domain_scores)
        """
        domain_scores = {}

        # Calculate score for each QLAE domain based on its semantic axes
        for domain_enum, config in self.qlae_domains.items():
            # Extract coordinates for this domain's semantic axes
            axis_map = {'L': 'love', 'J': 'justice', 'P': 'power', 'W': 'wisdom'}
            domain_values = [
                coords[axis_map[axis]]
                for axis in config.semantic_axes
                if axis in axis_map
            ]

            if domain_values:
                # Domain score is average of its semantic axes
                domain_score = np.mean(domain_values)
            else:
                domain_score = 0.5  # Neutral if no axes

            domain_scores[domain_enum] = domain_score
            config.harmony_score = domain_score

        # Calculate overall harmony per Primer formula
        scores = list(domain_scores.values())
        mean_score = np.mean(scores)
        variance = np.var(scores)

        overall_harmony = mean_score * 0.7 + (1.0 - variance) * 0.3

        return (overall_harmony, domain_scores)

    def get_domain_config(self, domain: QLAEDomain) -> QLAEDomainConfig:
        """Get configuration for specific QLAE domain"""
        return self.qlae_domains[domain]

    def verify_cross_realm_transmission(
        self,
        source_coords: Dict[str, float],
        target_coords: Dict[str, float],
        domain: QLAEDomain
    ) -> Dict[str, Any]:
        """
        Verify signal/force/meaning transmission across realms

        Each QLAE domain enables specific types of cross-realm functionality
        """
        config = self.qlae_domains[domain]

        # Calculate transmission strength based on domain's semantic axes
        axis_map = {'L': 'love', 'J': 'justice', 'P': 'power', 'W': 'wisdom'}

        source_strength = np.mean([
            source_coords[axis_map[axis]]
            for axis in config.semantic_axes
            if axis in axis_map
        ])

        target_reception = np.mean([
            target_coords[axis_map[axis]]
            for axis in config.semantic_axes
            if axis in axis_map
        ])

        # Transmission efficiency
        efficiency = min(source_strength, target_reception)

        # Signal degradation
        degradation = abs(source_strength - target_reception)

        return {
            'domain': domain.value,
            'transmission_strength': source_strength,
            'reception_quality': target_reception,
            'efficiency': efficiency,
            'signal_degradation': degradation,
            'successful': efficiency > 0.5 and degradation < 0.3
        }
