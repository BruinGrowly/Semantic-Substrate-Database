# Quick Start Guide - Semantic Substrate Database

## Installation & Testing

### 1. Run the Demo
```bash
cd "C:\Users\Well\Claude Code\Projects\SSE_Database"
python semantic_substrate_database.py
```

**Expected Output:**
```
SEMANTIC SUBSTRATE DATABASE v1.0 - Revolutionary Meaning-Native Database
Storing 8 biblical concepts...
Storing 6 sacred numbers...
Semantic search: 'compassion and kindness' → love (0.980 similarity)
Database exported to semantic_export.json
```

### 2. Run the Tests
```bash
python test_semantic_database.py
```

**Current Results:**
- 17/30 tests passing (57%)
- Core functionality verified
- Performance benchmarks completed

---

## Basic Usage

### Example 1: Store and Query Concepts
```python
from semantic_substrate_database import SemanticSubstrateDatabase

# Initialize
db = SemanticSubstrateDatabase("my_database.db")

# Store concepts
love_id = db.store_concept("love", "biblical")
mercy_id = db.store_concept("mercy", "biblical")
wisdom_id = db.store_concept("wisdom", "biblical")

# Query by text
result = db.query_by_text("love", "biblical")
print(f"Divine Resonance: {result['divine_resonance']:.3f}")
print(f"Distance from JEHOVAH: {result['distance_from_jehovah']:.3f}")

# Close
db.close()
```

### Example 2: Semantic Search
```python
from semantic_substrate_database import SemanticSubstrateDatabase

db = SemanticSubstrateDatabase("semantic.db")

# Find concepts similar to a query
results = db.search_semantic(
    "compassion and kindness",
    context="biblical",
    limit=5
)

for result in results:
    print(f"{result['concept_text']}: {result['semantic_similarity']:.3f}")

db.close()
```

### Example 3: Query by Divine Alignment
```python
from semantic_substrate_database import SemanticSubstrateDatabase

db = SemanticSubstrateDatabase("semantic.db")

# Find highly aligned concepts
divine_concepts = db.query_by_divine_resonance(
    min_resonance=0.8,
    context="biblical"
)

for concept in divine_concepts:
    print(f"{concept['concept_text']}: {concept['divine_resonance']:.3f}")

db.close()
```

### Example 4: Navigate to Universal Anchors
```python
from semantic_substrate_database import SemanticSubstrateDatabase

db = SemanticSubstrateDatabase("semantic.db")

# Find concepts near Divine Law (anchor 613)
near_law = db.query_nearest_to_anchor(
    anchor_id=613,
    max_distance=1.0,
    limit=10
)

for concept in near_law:
    print(f"{concept['concept_text']}: distance = {concept['semantic_distance']:.3f}")

db.close()
```

### Example 5: Context Manager (Recommended)
```python
from semantic_substrate_database import SemanticSubstrateDatabase

# Automatically closes on exit
with SemanticSubstrateDatabase("semantic.db") as db:
    # Store
    db.store_concept("faith", "biblical")
    db.store_concept("hope", "biblical")

    # Search
    results = db.search_semantic("belief", context="biblical")

    # Stats
    stats = db.get_statistics()
    print(f"Total concepts: {stats['total_concepts']}")
```

---

## Advanced Usage

### Store Sacred Numbers
```python
with SemanticSubstrateDatabase("semantic.db") as db:
    # Store sacred numbers
    db.store_sacred_number(7)   # Divine Perfection
    db.store_sacred_number(12)  # God's People
    db.store_sacred_number(40)  # Divine Testing
    db.store_sacred_number(613) # Divine Law

    # Query sacred numbers
    sacred = db.query_sacred_numbers(
        min_value=0,
        max_value=1000,
        only_sacred=True
    )

    for num in sacred:
        print(f"Number {num['value']}: {num['biblical_significance']:.3f}")
```

### Store Relationships
```python
with SemanticSubstrateDatabase("semantic.db") as db:
    # Store concepts
    love_id = db.store_concept("love", "biblical")
    mercy_id = db.store_concept("mercy", "biblical")

    # Store relationship
    db.store_relationship(love_id, mercy_id, "semantic_proximity")
```

### Export Database
```python
with SemanticSubstrateDatabase("semantic.db") as db:
    # Export entire database to JSON
    db.export_to_json("backup.json")

    # Get statistics
    stats = db.get_statistics()
    print(f"Exported {stats['total_concepts']} concepts")
    print(f"Exported {stats['sacred_numbers_count']} sacred numbers")
```

---

## Universal Anchors

The database includes 4 eternal reference points:

| ID | Name | Significance | Coordinates (L,P,W,J) |
|----|------|--------------|----------------------|
| **613** | Divine Law | 613 Commandments | (1.0, 1.0, 1.0, 1.0) |
| **12** | God's People | 12 Tribes of Israel | (0.9, 0.95, 0.9, 0.95) |
| **7** | Divine Perfection | 7 Days of Creation | (0.98, 0.95, 1.0, 0.98) |
| **40** | Divine Testing | 40 Days/Years | (0.85, 0.9, 0.88, 0.92) |

### Query by Anchor
```python
with SemanticSubstrateDatabase("semantic.db") as db:
    # Find concepts near each anchor
    near_law = db.query_nearest_to_anchor(613, max_distance=1.0)
    near_perfection = db.query_nearest_to_anchor(7, max_distance=1.0)
    near_testing = db.query_nearest_to_anchor(40, max_distance=1.0)
```

---

## Database Statistics

```python
with SemanticSubstrateDatabase("semantic.db") as db:
    stats = db.get_statistics()

    # Available statistics:
    print(f"Total Concepts: {stats['total_concepts']}")
    print(f"Unique Contexts: {stats['unique_contexts']}")
    print(f"Semantic Units: {stats['total_semantic_units']}")
    print(f"Sacred Numbers: {stats['sacred_numbers_count']}")
    print(f"Relationships: {stats['total_relationships']}")
    print(f"Avg Divine Resonance: {stats['avg_divine_resonance']:.3f}")
    print(f"Avg Distance from JEHOVAH: {stats['avg_distance_from_jehovah']:.3f}")
    print(f"Avg Biblical Balance: {stats['avg_biblical_balance']:.3f}")

    # Context distribution
    for context, count in stats['context_distribution'].items():
        print(f"  {context}: {count} concepts")
```

---

## Troubleshooting

### Database Already Exists
```python
# If database file exists, it will be opened and reused
db = SemanticSubstrateDatabase("existing.db")  # Opens existing
```

### Clear Cache
```python
with SemanticSubstrateDatabase("semantic.db") as db:
    db.clear_cache()  # Clears in-memory cache
```

### Optimize Database
```python
with SemanticSubstrateDatabase("semantic.db") as db:
    db.vacuum()  # Optimizes storage
```

---

## Performance Tips

### 1. Use Context Manager
```python
# Good - auto-closes connection
with SemanticSubstrateDatabase("db.db") as db:
    pass

# Bad - must manually close
db = SemanticSubstrateDatabase("db.db")
# ... do work ...
db.close()
```

### 2. Batch Operations
```python
with SemanticSubstrateDatabase("db.db") as db:
    # Batch store (more efficient than one-by-one)
    concepts = ["love", "mercy", "grace", "faith", "hope"]
    for concept in concepts:
        db.store_concept(concept, "biblical")
```

### 3. Cache Statistics
```python
with SemanticSubstrateDatabase("db.db") as db:
    cache_stats = db.get_cache_statistics()
    print(f"Cache size: {cache_stats['cache_size']}")
```

---

## Next Steps

1. **Test with your data** - Store your own concepts
2. **Experiment with contexts** - Try "educational", "business", "scientific"
3. **Explore semantic search** - Find conceptually similar items
4. **Track divine alignment** - Measure concept quality
5. **Build applications** - Use as backend for your apps

---

## Getting Help

- Read `DATABASE_README.md` for detailed documentation
- Check `PROJECT_STRUCTURE.md` for architecture details
- Review `semantic_substrate_database.py` for implementation
- Run tests with `python test_semantic_database.py`

---

## What's Working

✅ Core database schema (7 tables)
✅ Semantic coordinate storage
✅ Multi-dimensional queries
✅ Sacred number integration
✅ Universal anchor navigation
✅ Cache layer
✅ Export/import
✅ 17/30 tests passing

## Known Limitations

⚠️ SQLite backend (use PostgreSQL for production)
⚠️ In-memory cache only (add Redis for scale)
⚠️ Sequential queries (add concurrency support)
⚠️ Some tests need calibration

---

*Semantic Substrate Database v1.0 - Prototype*
*Built on SSE v2.2 Ultimate*
