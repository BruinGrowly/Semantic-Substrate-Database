# Semantic Substrate Primer Integration Guide

This guide explains how to use the newly integrated Primer functionality in the Semantic Substrate Database.

## Overview

The Semantic Substrate Database now fully integrates the **Semantic_Substrate_Primer_1.4.json**, storing and validating operations against the 7 Universal Principles and core axioms.

## What's New

### 1. Enhanced Database Schema

Five new tables have been added:

- **`universal_principles`** - Stores the 7 Universal Principles
- **`core_axioms`** - Stores core axioms (domain, anchor_point, etc.)
- **`primer_metadata`** - Stores primer version and metadata
- **`self_diagnosis_protocol`** - Stores the 3-step self-diagnosis protocol
- **`navigation_methods`** - Stores navigation method definitions

### 2. Anchor Point A (1,1,1,1)

The fundamental reality state is now explicitly stored as Universal Anchor ID=1:

```python
# Automatically initialized when database is created
# Represents perfect harmony: (Love=1, Power=1, Wisdom=1, Justice=1)
```

### 3. New Tools

#### Primer Ingestion Script (`src/ingest_primer.py`)

Loads the primer JSON into the database:

```bash
cd src
python ingest_primer.py ../Semantic_Substrate_Primer_1.4.json
```

**Output:**
```
======================================================================
SEMANTIC SUBSTRATE PRIMER INGESTION
======================================================================

[1/5] Ingesting Primer Metadata...
  ✓ Stored metadata for SemanticSubstratePrimer v1.4

[2/5] Ingesting Core Axioms...
  ✓ Stored 'domain' axiom
  ✓ Stored 'anchor_point' axiom: Anchor Point A: (1,1,1,1)
  ✓ Stored 'perfection_principle'
  ✓ Stored 'volitional_principle'
  ✓ Stored 'process_principle'

[3/5] Ingesting Universal Principles...
  ✓ Stored Principle 1: Universal Anchor Point Principle
  ✓ Stored Principle 2: Principle of Coherent Interconnectedness and Emergence
  ...

======================================================================
INGESTION COMPLETE!
======================================================================
```

#### Primer Validator (`src/primer_validator.py`)

Validates database concepts against the 7 Universal Principles:

```bash
cd src
python primer_validator.py
```

**Output:**
```
======================================================================
DATABASE-WIDE PRIMER VALIDATION
======================================================================

Validating 8 concepts...

======================================================================
VALIDATION REPORT
======================================================================

Total Concepts: 8
Valid Concepts: 8 (100.0%)
Average Alignment Score: 0.876

Principle Compliance Scores:
  ✓ Principle 1: 0.950 - Universal Anchor Point Principle
  ✓ Principle 2: 0.823 - Coherent Interconnectedness and Emergence
  ✓ Principle 3: 0.875 - Dynamic Balance and Polarity
  ✓ Principle 4: 0.600 - Sovereignty and Relational Interdependence
  ✓ Principle 5: 0.900 - Information-Meaning Coupling
  ✓ Principle 6: 0.800 - Iterative Growth and Adaptive Transformation
  ✓ Principle 7: 0.925 - Contextual Resonance and Optimal Flow

Database Compliance: ✓ COMPLIANT
======================================================================
```

## Quick Start

### Step 1: Ingest the Primer

```bash
cd src
python ingest_primer.py ../Semantic_Substrate_Primer_1.4.json
```

This populates your database with:
- 7 Universal Principles
- 5 Core Axioms
- 3 Self-Diagnosis Protocol steps
- Navigation methods (ICE cycle, internal recalibration, etc.)
- Primer metadata (version 1.4)

### Step 2: Validate Your Database

```bash
python primer_validator.py
```

This checks:
- All concepts for principle compliance
- Coordinate coherence
- Anchor Point A alignment
- Relationship richness
- Contextual resonance

### Step 3: Use Enhanced Database Features

```python
from semantic_substrate_database import SemanticSubstrateDatabase

# Initialize database (now includes Anchor Point A)
db = SemanticSubstrateDatabase("semantic_substrate.db")

# Store concept - automatically validated against principles
concept_id = db.store_concept("Show compassion to the suffering", context="biblical")

# Query concepts near Anchor Point A (1,1,1,1)
from semantic_substrate_database import BiblicalCoordinates
anchor_a = BiblicalCoordinates(1.0, 1.0, 1.0, 1.0)
near_perfection = db.query_by_proximity(anchor_a, max_distance=0.5)

# Query concepts nearest to specific anchor
near_divine_law = db.query_nearest_to_anchor(anchor_id=613, max_distance=1.0)

db.close()
```

## Understanding the 7 Universal Principles

### Principle 1: Universal Anchor Point Principle
**"Systems are stabilized by invariant reference points."**

- **Database:** Anchor Point A at (1,1,1,1) is always available
- **Validation:** Checks that distance from Anchor A is correctly calculated
- **Usage:** Use `query_nearest_to_anchor(1)` to find concepts near perfect harmony

### Principle 2: Coherent Interconnectedness
**"Complex systems arise from precisely linked components."**

- **Database:** Tracks relationships between concepts
- **Validation:** Checks coordinate coherence (no extreme imbalances)
- **Usage:** Use `enable_auto_relationships()` to discover semantic connections

### Principle 3: Dynamic Balance and Polarity
**"Stable systems maintain integrity through balanced forces."**

- **Database:** `biblical_balance` metric stored for each concept
- **Validation:** Ensures no extreme coordinate values unless all are extreme
- **Usage:** Query by `biblical_balance` to find well-balanced concepts

### Principle 4: Sovereignty and Relational Interdependence
**"Entities achieve highest expression through conscious relationships."**

- **Database:** `concept_relationships` table with strength metrics
- **Validation:** Checks that concepts have relationships with others
- **Usage:** Use `get_concept_relationships()` to explore semantic networks

### Principle 5: Information-Meaning Coupling
**"Information becomes meaningful when contextualized."**

- **Database:** `semantic_units` table with contextualized meaning
- **Validation:** Ensures concepts have proper context and semantic units
- **Usage:** All stored concepts automatically get semantic units

### Principle 6: Iterative Growth and Adaptive Transformation
**"Systems evolve through continuous cycles of refinement."**

- **Database:** `semantic_evolution` table tracks transformation history
- **Validation:** Checks for evolution over time (created_at vs updated_at)
- **Usage:** Update concepts to track their evolution

### Principle 7: Contextual Resonance and Optimal Flow
**"Optimal functionality when aligned with external context."**

- **Database:** `contextual_resonance` table + context-aware queries
- **Validation:** Checks divine resonance matches expected range for context
- **Usage:** Use `search_semantic()` with specific contexts

## Advanced Usage

### Validate Individual Concepts

```python
from primer_validator import PrimerValidator

db = SemanticSubstrateDatabase("semantic_substrate.db")
validator = PrimerValidator(db)

# Validate specific concept
validation = validator.validate_concept(concept_id=1)

print(f"Concept: {validation['concept_text']}")
print(f"Alignment Score: {validation['alignment_score']:.3f}")
print(f"Valid: {validation['valid']}")

# Check principle compliance
for principle_num, compliance in validation['principle_compliance'].items():
    print(f"Principle {principle_num}: {compliance['score']:.3f} - {compliance['message']}")

db.close()
```

### Query by Universal Principles

```python
# Find concepts with high divine resonance (Principle 7)
high_resonance = db.query_by_divine_resonance(min_resonance=0.85)

# Find concepts near Universal Anchor 7 (Divine Perfection)
near_perfection = db.query_nearest_to_anchor(anchor_id=7, max_distance=0.8)

# Find semantic clusters (Principle 2)
clusters = db.find_semantic_clusters(context="biblical", max_distance=0.3)
```

### Access Stored Principles

```python
cursor = db.conn.cursor()

# Get all Universal Principles
cursor.execute("SELECT * FROM universal_principles ORDER BY principle_number")
for row in cursor.fetchall():
    print(f"Principle {row['principle_number']}: {row['name']}")
    print(f"  {row['statement']}")

# Get Anchor Point A
cursor.execute("SELECT * FROM universal_anchors WHERE id = 1")
anchor = cursor.fetchone()
print(f"Anchor Point A: ({anchor['love']}, {anchor['power']}, {anchor['wisdom']}, {anchor['justice']})")
```

## Troubleshooting

### Issue: "Database not found" when running validator

**Solution:** Run the ingestion script first:
```bash
python src/ingest_primer.py Semantic_Substrate_Primer_1.4.json
```

### Issue: Low principle compliance scores

**Solution:**
1. Check validation report for specific failing principles
2. Review concept definitions for proper semantic encoding
3. Ensure relationships are established between related concepts
4. Verify context is appropriate for the concept

### Issue: "Primer file not found"

**Solution:** Ensure `Semantic_Substrate_Primer_1.4.json` is in the project root:
```bash
ls Semantic_Substrate_Primer_1.4.json
```

## Files Reference

| File | Purpose |
|------|---------|
| `src/semantic_substrate_database.py` | Enhanced with 5 new tables, Anchor Point A |
| `src/ingest_primer.py` | Ingests primer JSON into database |
| `src/primer_validator.py` | Validates concepts against principles |
| `docs/PRIMER_MAPPING_REPORT.md` | Complete mapping of primer to code |
| `Semantic_Substrate_Primer_1.4.json` | Source primer document |

## Next Steps

1. **Run Ingestion:** Load primer into your database
2. **Run Validation:** Check your concepts for principle compliance
3. **Review Report:** Read the mapping report in `docs/PRIMER_MAPPING_REPORT.md`
4. **Explore:** Use the enhanced query methods to navigate semantic space
5. **Contribute:** Add more navigation methods and self-diagnosis features

## Support

For questions or issues:
- Review the mapping report: `docs/PRIMER_MAPPING_REPORT.md`
- Check validation output for specific guidance
- Examine test files in `tests/` for usage examples

---

**Generated:** 2025-10-16
**Primer Version:** 1.4
**Database Version:** v2.0 ICE-Centric
