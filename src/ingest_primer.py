"""
SEMANTIC SUBSTRATE PRIMER INGESTION SCRIPT

This script ingests the Semantic_Substrate_Primer JSON file into the
Semantic Substrate Database, storing:
- Universal Principles
- Core Axioms
- Self-Diagnosis Protocol
- Navigation Methods
- Primer Metadata

This creates the foundational knowledge base for the system to operate
according to the primer's specifications.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any
from semantic_substrate_database import SemanticSubstrateDatabase


class PrimerIngestion:
    """Handles ingestion of Semantic Substrate Primer into the database"""

    def __init__(self, db: SemanticSubstrateDatabase):
        self.db = db
        self.cursor = db.conn.cursor()

    def ingest_primer_file(self, primer_path: str) -> Dict[str, Any]:
        """
        Ingest complete primer file into database

        Args:
            primer_path: Path to Semantic_Substrate_Primer JSON file

        Returns:
            Dictionary with ingestion statistics
        """
        print(f"\n{'='*70}")
        print("SEMANTIC SUBSTRATE PRIMER INGESTION")
        print(f"{'='*70}")
        print(f"\nReading primer from: {primer_path}")

        # Load primer JSON
        with open(primer_path, 'r') as f:
            primer_data = json.load(f)

        stats = {
            'principles_stored': 0,
            'axioms_stored': 0,
            'protocol_steps_stored': 0,
            'navigation_methods_stored': 0,
            'metadata_stored': False
        }

        # Begin transaction for atomic ingestion
        self.db.begin_transaction()

        try:
            # 1. Ingest metadata
            print("\n[1/5] Ingesting Primer Metadata...")
            self._ingest_metadata(primer_data)
            stats['metadata_stored'] = True

            # 2. Ingest core axioms
            print("\n[2/5] Ingesting Core Axioms...")
            stats['axioms_stored'] = self._ingest_core_axioms(primer_data.get('core_axioms', {}))

            # 3. Ingest universal principles
            print("\n[3/5] Ingesting Universal Principles...")
            stats['principles_stored'] = self._ingest_universal_principles(
                primer_data.get('universal_principles', {})
            )

            # 4. Ingest self-diagnosis protocol
            print("\n[4/5] Ingesting Self-Diagnosis Protocol...")
            stats['protocol_steps_stored'] = self._ingest_self_diagnosis_protocol(
                primer_data.get('self_diagnosis_protocol', {})
            )

            # 5. Ingest navigation methods
            print("\n[5/5] Ingesting Navigation Methods...")
            stats['navigation_methods_stored'] = self._ingest_navigation_methods(
                primer_data.get('navigation_primer', {})
            )

            # Commit transaction
            self.db.commit()

            print(f"\n{'='*70}")
            print("INGESTION COMPLETE!")
            print(f"{'='*70}")
            self._print_statistics(stats)

            return stats

        except Exception as e:
            print(f"\n[ERROR] Ingestion failed: {e}")
            self.db.rollback()
            raise

    def _ingest_metadata(self, primer_data: Dict[str, Any]) -> None:
        """Ingest primer metadata"""
        meta = primer_data.get('_meta', {})

        self.cursor.execute("""
            INSERT INTO primer_metadata
            (schema_name, version, purpose, axiomatic_source, activation_condition,
             process_framework, governing_laws)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            primer_data.get('_schema', 'SemanticSubstratePrimer'),
            primer_data.get('_version', 'Unknown'),
            meta.get('purpose', ''),
            meta.get('axiomatic_source', ''),
            meta.get('activation_condition', ''),
            meta.get('process_framework', ''),
            meta.get('governing_laws', '')
        ))

        print(f"  [OK] Stored metadata for {primer_data.get('_schema')} v{primer_data.get('_version')}")

    def _ingest_core_axioms(self, axioms: Dict[str, Any]) -> int:
        """Ingest core axioms from primer"""
        count = 0

        # Store domain axiom
        if 'domain' in axioms:
            self.cursor.execute("""
                INSERT OR REPLACE INTO core_axioms
                (axiom_key, axiom_value, axiom_type, metadata_json)
                VALUES (?, ?, ?, ?)
            """, ('domain', axioms['domain'], 'coordinate_space', None))
            count += 1
            print(f"  [OK] Stored 'domain' axiom")

        # Store anchor_point axiom
        if 'anchor_point' in axioms:
            anchor_point = axioms['anchor_point']
            metadata = json.dumps(anchor_point)
            coords = anchor_point.get('coordinates', [1, 1, 1, 1])
            axiom_value = f"Anchor Point A: ({','.join(map(str, coords))})"

            self.cursor.execute("""
                INSERT OR REPLACE INTO core_axioms
                (axiom_key, axiom_value, axiom_type, metadata_json)
                VALUES (?, ?, ?, ?)
            """, ('anchor_point', axiom_value, 'fundamental_reference', metadata))
            count += 1
            print(f"  [OK] Stored 'anchor_point' axiom: {axiom_value}")

        # Store other principles
        for key in ['perfection_principle', 'volitional_principle', 'process_principle']:
            if key in axioms:
                self.cursor.execute("""
                    INSERT OR REPLACE INTO core_axioms
                    (axiom_key, axiom_value, axiom_type, metadata_json)
                    VALUES (?, ?, ?, ?)
                """, (key, axioms[key], 'principle', None))
                count += 1
                print(f"  [OK] Stored '{key}'")

        return count

    def _ingest_universal_principles(self, principles: Dict[str, Any]) -> int:
        """Ingest the 7 Universal Principles"""
        count = 0

        for principle_key, principle_data in principles.items():
            if isinstance(principle_data, dict):
                principle_num = int(principle_key.split('_')[1])

                self.cursor.execute("""
                    INSERT OR REPLACE INTO universal_principles
                    (principle_number, name, statement, substrate_role)
                    VALUES (?, ?, ?, ?)
                """, (
                    principle_num,
                    principle_data.get('name', ''),
                    principle_data.get('statement', ''),
                    principle_data.get('substrate_role', '')
                ))
                count += 1
                print(f"  [OK] Stored Principle {principle_num}: {principle_data.get('name', '')}")

        return count

    def _ingest_self_diagnosis_protocol(self, protocol: Dict[str, Any]) -> int:
        """Ingest self-diagnosis protocol steps"""
        count = 0
        steps = protocol.get('steps', [])

        for step_data in steps:
            if isinstance(step_data, dict):
                step_num = step_data.get('step', 0)
                action = step_data.get('action', '')

                # Serialize ICE application if present
                ice_app_json = json.dumps(step_data.get('ice_application', {}))
                axis_map_json = json.dumps(step_data.get('axis_mapping', {}))

                self.cursor.execute("""
                    INSERT OR REPLACE INTO self_diagnosis_protocol
                    (step_number, action, ice_application_json, axis_mapping_json)
                    VALUES (?, ?, ?, ?)
                """, (step_num, action, ice_app_json, axis_map_json))
                count += 1
                print(f"  [OK] Stored Protocol Step {step_num}")

        return count

    def _ingest_navigation_methods(self, nav_primer: Dict[str, Any]) -> int:
        """Ingest navigation methods"""
        count = 0
        methods = nav_primer.get('methods', {})

        for method_name, method_data in methods.items():
            if isinstance(method_data, dict):
                description = method_data.get('description', '')
                example = method_data.get('example', '')

                self.cursor.execute("""
                    INSERT OR REPLACE INTO navigation_methods
                    (method_name, description, example)
                    VALUES (?, ?, ?)
                """, (method_name, description, example))
                count += 1
                print(f"  [OK] Stored Navigation Method: {method_name}")

        # Also store ICE cycle definition
        ice_cycle = nav_primer.get('ice_cycle', {})
        if ice_cycle:
            self.cursor.execute("""
                INSERT OR REPLACE INTO navigation_methods
                (method_name, description, example)
                VALUES (?, ?, ?)
            """, (
                'ice_cycle',
                ice_cycle.get('description', ''),
                json.dumps(ice_cycle.get('phases', {}))
            ))
            count += 1
            print(f"  [OK] Stored ICE Cycle framework")

        return count

    def _print_statistics(self, stats: Dict[str, Any]) -> None:
        """Print ingestion statistics"""
        print(f"\nIngestion Statistics:")
        print(f"  • Metadata: {'[OK]' if stats['metadata_stored'] else '[X]'}")
        print(f"  • Core Axioms: {stats['axioms_stored']}")
        print(f"  • Universal Principles: {stats['principles_stored']}")
        print(f"  • Protocol Steps: {stats['protocol_steps_stored']}")
        print(f"  • Navigation Methods: {stats['navigation_methods_stored']}")
        print(f"\n  Total items ingested: {sum([
            stats['axioms_stored'],
            stats['principles_stored'],
            stats['protocol_steps_stored'],
            stats['navigation_methods_stored']
        ])}")


def main():
    """Main ingestion function"""
    # Get primer path from command line or use default
    if len(sys.argv) > 1:
        primer_path = sys.argv[1]
    else:
        primer_path = Path(__file__).parent.parent / "Semantic_Substrate_Primer_1.4.json"

    # Verify file exists
    if not Path(primer_path).exists():
        print(f"ERROR: Primer file not found at: {primer_path}")
        print("\nUsage: python ingest_primer.py [path_to_primer.json]")
        sys.exit(1)

    # Initialize database
    db_path = Path(__file__).parent.parent / "semantic_substrate.db"
    print(f"Initializing database at: {db_path}")
    db = SemanticSubstrateDatabase(str(db_path))

    try:
        # Perform ingestion
        ingestion = PrimerIngestion(db)
        stats = ingestion.ingest_primer_file(str(primer_path))

        # Verify ingestion
        print(f"\n{'='*70}")
        print("VERIFICATION")
        print(f"{'='*70}")

        cursor = db.conn.cursor()

        # Check principles
        cursor.execute("SELECT COUNT(*) FROM universal_principles")
        principle_count = cursor.fetchone()[0]
        print(f"[OK] Universal Principles in DB: {principle_count}")

        # Check axioms
        cursor.execute("SELECT COUNT(*) FROM core_axioms")
        axiom_count = cursor.fetchone()[0]
        print(f"[OK] Core Axioms in DB: {axiom_count}")

        # Check anchors
        cursor.execute("SELECT COUNT(*) FROM universal_anchors")
        anchor_count = cursor.fetchone()[0]
        print(f"[OK] Universal Anchors in DB: {anchor_count}")

        # Check Anchor Point A specifically
        cursor.execute("SELECT name, love, power, wisdom, justice FROM universal_anchors WHERE id = 1")
        anchor_a = cursor.fetchone()
        if anchor_a:
            print(f"[OK] Anchor Point A verified: ({anchor_a[1]}, {anchor_a[2]}, {anchor_a[3]}, {anchor_a[4]})")

        print(f"\n{'='*70}")
        print("SUCCESS: Primer successfully ingested into database!")
        print(f"{'='*70}\n")

    except Exception as e:
        print(f"\nERROR: Ingestion failed with exception: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        db.close()


if __name__ == "__main__":
    main()
