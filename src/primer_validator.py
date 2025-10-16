"""
PRIMER ALIGNMENT VALIDATOR

This module validates that database operations and stored concepts align
with the Universal Principles and axioms from the Semantic Substrate Primer.

It ensures that:
1. Operations respect the 7 Universal Principles
2. Coordinates are properly measured relative to Anchor Point A (1,1,1,1)
3. ICE framework (Intent-Context-Execution) is properly applied
4. Semantic coherence is maintained
"""

import math
from typing import Dict, Any, List, Tuple, Optional
from semantic_substrate_database import SemanticSubstrateDatabase, BiblicalCoordinates


class PrimerValidator:
    """Validates database operations against primer principles"""

    def __init__(self, db: SemanticSubstrateDatabase):
        self.db = db
        self.cursor = db.conn.cursor()

        # Load universal principles from database
        self.principles = self._load_principles()
        self.anchor_point_a = BiblicalCoordinates(1.0, 1.0, 1.0, 1.0)

    def _load_principles(self) -> Dict[int, Dict[str, str]]:
        """Load universal principles from database"""
        self.cursor.execute("""
            SELECT principle_number, name, statement, substrate_role
            FROM universal_principles
            ORDER BY principle_number
        """)

        principles = {}
        for row in self.cursor.fetchall():
            principles[row[0]] = {
                'name': row[1],
                'statement': row[2],
                'substrate_role': row[3]
            }
        return principles

    def validate_concept(self, concept_id: int) -> Dict[str, Any]:
        """
        Validate a stored concept against primer principles

        Returns validation report with alignment scores and principle compliance
        """
        # Get concept data
        self.cursor.execute("""
            SELECT concept_text, context, love, power, wisdom, justice,
                   divine_resonance, distance_from_jehovah
            FROM semantic_coordinates
            WHERE id = ?
        """, (concept_id,))

        row = self.cursor.fetchone()
        if not row:
            return {'error': f'Concept {concept_id} not found'}

        concept = {
            'text': row[0],
            'context': row[1],
            'coordinates': BiblicalCoordinates(row[2], row[3], row[4], row[5]),
            'divine_resonance': row[6],
            'distance_from_anchor': row[7]
        }

        validation = {
            'concept_id': concept_id,
            'concept_text': concept['text'],
            'valid': True,
            'alignment_score': 0.0,
            'principle_compliance': {},
            'warnings': [],
            'recommendations': []
        }

        # Validate against each principle
        validation['principle_compliance'][1] = self._validate_principle_1(concept)
        validation['principle_compliance'][2] = self._validate_principle_2(concept)
        validation['principle_compliance'][3] = self._validate_principle_3(concept)
        validation['principle_compliance'][4] = self._validate_principle_4(concept)
        validation['principle_compliance'][5] = self._validate_principle_5(concept)
        validation['principle_compliance'][6] = self._validate_principle_6(concept)
        validation['principle_compliance'][7] = self._validate_principle_7(concept)

        # Calculate overall alignment score
        compliance_scores = [v['score'] for v in validation['principle_compliance'].values()]
        validation['alignment_score'] = sum(compliance_scores) / len(compliance_scores)

        # Check if valid
        if validation['alignment_score'] < 0.6:
            validation['valid'] = False
            validation['warnings'].append("Low principle alignment - review concept definition")

        # Add recommendations based on weak areas
        for principle_num, compliance in validation['principle_compliance'].items():
            if compliance['score'] < 0.7:
                validation['recommendations'].append(
                    f"Improve alignment with Principle {principle_num}: {self.principles[principle_num]['name']}"
                )

        return validation

    def _validate_principle_1(self, concept: Dict[str, Any]) -> Dict[str, Any]:
        """Validate Universal Anchor Point Principle"""
        # Principle 1: Systems are stabilized by invariant reference points
        # Check: Concept should have measurable distance from Anchor Point A

        coords = concept['coordinates']
        distance = concept['distance_from_anchor']

        # Calculate expected distance
        expected_distance = math.sqrt(
            (1.0 - coords.love) ** 2 +
            (1.0 - coords.power) ** 2 +
            (1.0 - coords.wisdom) ** 2 +
            (1.0 - coords.justice) ** 2
        )

        # Check consistency
        distance_error = abs(distance - expected_distance)
        score = 1.0 - min(1.0, distance_error)

        return {
            'score': score,
            'compliant': distance_error < 0.1,
            'message': f"Distance from Anchor A: {distance:.3f} (expected: {expected_distance:.3f})"
        }

    def _validate_principle_2(self, concept: Dict[str, Any]) -> Dict[str, Any]:
        """Validate Coherent Interconnectedness and Emergence"""
        # Principle 2: Complex systems arise from precisely linked components
        # Check: All four axes should be coherently aligned (no extreme imbalances)

        coords = concept['coordinates']
        values = [coords.love, coords.power, coords.wisdom, coords.justice]

        # Calculate variance (measure of imbalance)
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        std_dev = math.sqrt(variance)

        # Lower standard deviation = better coherence
        score = max(0.0, 1.0 - (std_dev * 2))

        return {
            'score': score,
            'compliant': std_dev < 0.3,
            'message': f"Coordinate coherence: {score:.3f} (std_dev: {std_dev:.3f})"
        }

    def _validate_principle_3(self, concept: Dict[str, Any]) -> Dict[str, Any]:
        """Validate Dynamic Balance and Polarity"""
        # Principle 3: Stable systems maintain integrity through balanced forces
        # Check: No axis should be at extremes (0 or 1) unless all are

        coords = concept['coordinates']
        values = [coords.love, coords.power, coords.wisdom, coords.justice]

        # Check for extreme values
        extreme_count = sum(1 for v in values if v < 0.1 or v > 0.9)
        all_extreme = all(v > 0.9 for v in values) or all(v < 0.1 for v in values)

        if all_extreme:
            score = 1.0  # Perfectly aligned to an extreme state
        elif extreme_count == 0:
            score = 1.0  # Well balanced
        else:
            score = max(0.0, 1.0 - (extreme_count * 0.25))

        return {
            'score': score,
            'compliant': score > 0.7,
            'message': f"Dynamic balance: {score:.3f}"
        }

    def _validate_principle_4(self, concept: Dict[str, Any]) -> Dict[str, Any]:
        """Validate Sovereignty and Relational Interdependence"""
        # Principle 4: Entities achieve highest expression through conscious relationships
        # Check: Concept should have relationships with other concepts

        concept_id = self.db.query_by_text(concept['text'], concept['context'])
        if concept_id:
            relationships = self.db.get_concept_relationships(concept_id['id'])
            relationship_count = len(relationships)

            # Score based on relationship richness
            score = min(1.0, relationship_count / 5.0)

            return {
                'score': score,
                'compliant': relationship_count > 0,
                'message': f"Relationships: {relationship_count}"
            }

        return {
            'score': 0.5,
            'compliant': False,
            'message': "Cannot verify relationships"
        }

    def _validate_principle_5(self, concept: Dict[str, Any]) -> Dict[str, Any]:
        """Validate Information-Meaning Coupling"""
        # Principle 5: Information becomes meaningful when contextualized
        # Check: Concept has proper context and semantic unit

        has_context = bool(concept['context'])
        context_specificity = len(concept['context']) > 3  # Not just generic

        # Check if semantic unit exists
        self.cursor.execute("""
            SELECT COUNT(*) FROM semantic_units su
            JOIN semantic_coordinates sc ON su.coordinate_id = sc.id
            WHERE sc.concept_text = ? AND sc.context = ?
        """, (concept['text'], concept['context']))

        has_semantic_unit = self.cursor.fetchone()[0] > 0

        score = (0.4 if has_context else 0.0) + \
                (0.3 if context_specificity else 0.0) + \
                (0.3 if has_semantic_unit else 0.0)

        return {
            'score': score,
            'compliant': score > 0.7,
            'message': f"Meaning coupling: {score:.3f}"
        }

    def _validate_principle_6(self, concept: Dict[str, Any]) -> Dict[str, Any]:
        """Validate Iterative Growth and Adaptive Transformation"""
        # Principle 6: Systems evolve through continuous cycles
        # Check: Concept has evolution history (updates)

        self.cursor.execute("""
            SELECT created_at, updated_at FROM semantic_coordinates
            WHERE concept_text = ? AND context = ?
        """, (concept['text'], concept['context']))

        row = self.cursor.fetchone()
        if row:
            created = row[0]
            updated = row[1]
            has_evolved = created != updated

            score = 1.0 if has_evolved else 0.7  # 0.7 for new concepts

            return {
                'score': score,
                'compliant': True,
                'message': f"Evolution: {'Yes' if has_evolved else 'Initial state'}"
            }

        return {
            'score': 0.5,
            'compliant': False,
            'message': "Cannot verify evolution"
        }

    def _validate_principle_7(self, concept: Dict[str, Any]) -> Dict[str, Any]:
        """Validate Contextual Resonance and Optimal Flow"""
        # Principle 7: Optimal functionality when aligned with context
        # Check: Divine resonance is appropriate for context

        resonance = concept['divine_resonance']
        context = concept['context']

        # Expected resonance ranges by context
        context_resonance_targets = {
            'biblical': (0.8, 1.0),
            'ministry': (0.75, 0.95),
            'educational': (0.7, 0.9),
            'business': (0.6, 0.85),
            'personal': (0.65, 0.9)
        }

        target = context_resonance_targets.get(context, (0.5, 0.9))
        in_range = target[0] <= resonance <= target[1]

        if in_range:
            score = 1.0
        else:
            # Calculate distance from range
            if resonance < target[0]:
                distance = target[0] - resonance
            else:
                distance = resonance - target[1]
            score = max(0.0, 1.0 - distance)

        return {
            'score': score,
            'compliant': in_range,
            'message': f"Contextual resonance: {resonance:.3f} (target: {target[0]:.2f}-{target[1]:.2f})"
        }

    def validate_database(self) -> Dict[str, Any]:
        """
        Validate entire database for primer alignment

        Returns comprehensive validation report
        """
        print(f"\n{'='*70}")
        print("DATABASE-WIDE PRIMER VALIDATION")
        print(f"{'='*70}\n")

        # Get all concepts
        self.cursor.execute("SELECT id, concept_text FROM semantic_coordinates")
        concepts = self.cursor.fetchall()

        total_concepts = len(concepts)
        valid_concepts = 0
        total_alignment = 0.0
        principle_scores = {i: [] for i in range(1, 8)}

        print(f"Validating {total_concepts} concepts...\n")

        for concept_id, concept_text in concepts:
            validation = self.validate_concept(concept_id)

            if validation['valid']:
                valid_concepts += 1

            total_alignment += validation['alignment_score']

            # Collect principle scores
            for principle_num, compliance in validation['principle_compliance'].items():
                principle_scores[principle_num].append(compliance['score'])

        # Calculate averages
        avg_alignment = total_alignment / total_concepts if total_concepts > 0 else 0
        avg_principle_scores = {
            num: sum(scores) / len(scores) if scores else 0
            for num, scores in principle_scores.items()
        }

        report = {
            'total_concepts': total_concepts,
            'valid_concepts': valid_concepts,
            'validity_rate': valid_concepts / total_concepts if total_concepts > 0 else 0,
            'average_alignment': avg_alignment,
            'principle_scores': avg_principle_scores,
            'database_compliant': avg_alignment >= 0.7
        }

        # Print report
        print(f"{'='*70}")
        print("VALIDATION REPORT")
        print(f"{'='*70}\n")
        print(f"Total Concepts: {report['total_concepts']}")
        print(f"Valid Concepts: {report['valid_concepts']} ({report['validity_rate']*100:.1f}%)")
        print(f"Average Alignment Score: {report['average_alignment']:.3f}")
        print(f"\nPrinciple Compliance Scores:")

        for principle_num in range(1, 8):
            score = avg_principle_scores[principle_num]
            status = "[OK]" if score >= 0.7 else "[!]" if score >= 0.5 else "[X]"
            principle_name = self.principles.get(principle_num, {}).get('name', 'Unknown')
            print(f"  {status} Principle {principle_num}: {score:.3f} - {principle_name}")

        print(f"\nDatabase Compliance: {'[OK] COMPLIANT' if report['database_compliant'] else '[X] NON-COMPLIANT'}")
        print(f"{'='*70}\n")

        return report

    def generate_recommendations(self) -> List[str]:
        """Generate recommendations for improving primer alignment"""
        report = self.validate_database()

        recommendations = []

        if report['average_alignment'] < 0.7:
            recommendations.append(
                "CRITICAL: Overall alignment is below threshold. Review core concepts and coordinate calculations."
            )

        # Check each principle
        for principle_num, score in report['principle_scores'].items():
            if score < 0.7:
                principle_name = self.principles[principle_num]['name']
                recommendations.append(
                    f"Improve Principle {principle_num} ({principle_name}): Current score {score:.2f}"
                )

        if report['validity_rate'] < 0.8:
            recommendations.append(
                f"Validity rate is {report['validity_rate']*100:.1f}%. Review invalid concepts for proper semantic encoding."
            )

        return recommendations


def main():
    """Run validation on database"""
    import sys
    from pathlib import Path

    # Initialize database
    db_path = Path(__file__).parent.parent / "semantic_substrate.db"

    if not db_path.exists():
        print(f"ERROR: Database not found at {db_path}")
        print("Please run ingest_primer.py first to initialize the database.")
        sys.exit(1)

    print(f"Loading database from: {db_path}")
    db = SemanticSubstrateDatabase(str(db_path))

    try:
        validator = PrimerValidator(db)

        # Run validation
        report = validator.validate_database()

        # Generate recommendations
        recommendations = validator.generate_recommendations()

        if recommendations:
            print(f"\n{'='*70}")
            print("RECOMMENDATIONS")
            print(f"{'='*70}\n")
            for i, rec in enumerate(recommendations, 1):
                print(f"{i}. {rec}")
            print()

    finally:
        db.close()


if __name__ == "__main__":
    main()
