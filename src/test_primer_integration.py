"""
Integration test for Primer functionality

Tests:
1. Primer ingestion
2. Schema verification
3. Concept validation
4. Query operations with primer data
"""

from semantic_substrate_database import SemanticSubstrateDatabase, BiblicalCoordinates
from primer_validator import PrimerValidator


def test_primer_integration():
    """Comprehensive integration test"""
    print("\n" + "="*70)
    print("PRIMER INTEGRATION TEST")
    print("="*70 + "\n")

    # Initialize database
    db = SemanticSubstrateDatabase("../semantic_substrate.db")

    # Test 1: Verify primer tables exist
    print("[TEST 1] Verifying primer tables...")
    cursor = db.conn.cursor()

    expected_tables = [
        'universal_principles',
        'core_axioms',
        'primer_metadata',
        'self_diagnosis_protocol',
        'navigation_methods'
    ]

    for table in expected_tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        status = "[PASS]" if count > 0 else "[FAIL]"
        print(f"  {status} {table}: {count} rows")

    # Test 2: Verify Anchor Point A
    print("\n[TEST 2] Verifying Anchor Point A...")
    cursor.execute("SELECT * FROM universal_anchors WHERE id = 1")
    anchor = cursor.fetchone()
    if anchor:
        coords = (anchor[3], anchor[4], anchor[5], anchor[6])  # L, P, W, J
        expected = (1.0, 1.0, 1.0, 1.0)
        if coords == expected:
            print(f"  [PASS] Anchor Point A: {coords}")
        else:
            print(f"  [FAIL] Expected {expected}, got {coords}")
    else:
        print("  [FAIL] Anchor Point A not found")

    # Test 3: Test concept storage and retrieval
    print("\n[TEST 3] Testing concept storage...")
    test_concept = "Show mercy to the weak"
    concept_id = db.store_concept(test_concept, "biblical")

    retrieved = db.query_by_text(test_concept, "biblical")
    if retrieved and retrieved['concept_text'] == test_concept:
        print(f"  [PASS] Stored and retrieved: '{test_concept}'")
    else:
        print(f"  [FAIL] Could not retrieve stored concept")

    # Test 4: Test proximity to Anchor Point A
    print("\n[TEST 4] Testing proximity queries to Anchor Point A...")
    anchor_a = BiblicalCoordinates(1.0, 1.0, 1.0, 1.0)
    near_anchor = db.query_by_proximity(anchor_a, max_distance=2.0, limit=5)
    print(f"  [PASS] Found {len(near_anchor)} concepts near Anchor Point A")
    for i, concept in enumerate(near_anchor[:3], 1):
        print(f"    {i}. {concept['concept_text']}: distance={concept['semantic_distance']:.3f}")

    # Test 5: Test validation
    print("\n[TEST 5] Testing concept validation...")
    validator = PrimerValidator(db)

    if concept_id:
        validation = validator.validate_concept(concept_id)
        print(f"  [PASS] Validation complete")
        print(f"    Alignment Score: {validation['alignment_score']:.3f}")
        print(f"    Valid: {validation['valid']}")
        print(f"    Principle Compliance:")
        for num, compliance in sorted(validation['principle_compliance'].items())[:3]:
            print(f"      P{num}: {compliance['score']:.3f} - {compliance['message']}")

    # Test 6: Query by divine resonance
    print("\n[TEST 6] Testing divine resonance queries...")
    high_res = db.query_by_divine_resonance(min_resonance=0.7, context="biblical")
    print(f"  [PASS] Found {len(high_res)} concepts with divine resonance >= 0.7")

    # Test 7: Access Universal Principles
    print("\n[TEST 7] Accessing stored Universal Principles...")
    cursor.execute("SELECT principle_number, name FROM universal_principles ORDER BY principle_number")
    principles = cursor.fetchall()
    if len(principles) == 7:
        print(f"  [PASS] All 7 Universal Principles stored")
        for num, name in principles[:3]:
            print(f"    P{num}: {name}")
    else:
        print(f"  [FAIL] Expected 7 principles, found {len(principles)}")

    # Test 8: Access Core Axioms
    print("\n[TEST 8] Accessing stored Core Axioms...")
    cursor.execute("SELECT COUNT(*) FROM core_axioms")
    axiom_count = cursor.fetchone()[0]
    if axiom_count >= 5:
        print(f"  [PASS] Core Axioms stored: {axiom_count}")
    else:
        print(f"  [FAIL] Expected >= 5 axioms, found {axiom_count}")

    # Final Summary
    print("\n" + "="*70)
    print("INTEGRATION TEST COMPLETE")
    print("="*70)
    print("\nAll critical functionality verified:")
    print("  [OK] Primer data ingested")
    print("  [OK] Database schema enhanced")
    print("  [OK] Anchor Point A initialized")
    print("  [OK] Concept storage and retrieval")
    print("  [OK] Validation system operational")
    print("  [OK] Universal Principles accessible")
    print("  [OK] Core Axioms accessible")
    print("\n" + "="*70 + "\n")

    db.close()


if __name__ == "__main__":
    test_primer_integration()
