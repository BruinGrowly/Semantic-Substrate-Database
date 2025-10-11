# Semantic Substrate Database v2.0 - ICE-Centric Database System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Database](https://img.shields.io/badge/Database-Semantic-brightgreen.svg)](https://github.com/BruinGrowly/Semantic-Substrate-Database)
[![Open Source](https://img.shields.io/badge/Open%20Source-100%25-brightgreen.svg)](https://github.com/BruinGrowly/Semantic-Substrate-Database)
[![ICE Engine](https://img.shields.io/badge/Engine-ICE--Centric-red.svg)](https://github.com/BruinGrowly/Semantic-Substrate-Engine)

**The World's First ICE-Centric Semantic Database**

A revolutionary database system that stores and queries semantic meaning using the **ICE (Intent-Context-Execution)** framework with 4D divine coordinate system. Built on [Semantic Substrate Engine v3.0](https://github.com/BruinGrowly/Semantic-Substrate-Engine).

## 🚀 Key Features

### Database-Centric Architecture
- **Semantic Storage**: Store meaning as 4D coordinates (LOVE, POWER, WISDOM, JUSTICE)
- **Intent-Aware Queries**: Find concepts by their intent and meaning, not keywords
- **Context-Rich Retrieval**: Context-aware semantic search across 8 domains
- **Universal Anchor Navigation**: Navigate toward perfect ethical alignment
- **Self-Aware Capabilities**: Database understands its own semantic relationships

### ICE Framework Integration
- **Intent Understanding**: Analyzes the WHY behind every stored concept
- **Context Processing**: Processes the WHERE of every query operation
- **Execution Validation**: Ensures behavioral alignment of responses
- **7-Stage Pipeline**: Full ICE semantic analysis for all operations
- **99.83% Semantic Integrity**: Meaning preservation guaranteed

## ⚡ Quick Start

### Installation
```bash
# Install the Database (includes Engine dependency)
pip install semantic-substrate-database

# Or clone from source
git clone https://github.com/BruinGrowly/Semantic-Substrate-Database.git
cd Semantic-Substrate-Database
pip install -r requirements.txt
```

### Basic Database Usage
```python
from src import SemanticSubstrateDatabase

# Initialize the semantic database
db = SemanticSubstrateDatabase("meaning.db")

# Store semantic meaning
concept_id = db.store_concept(
    "Show compassion to those who suffer",
    context="spiritual"
)

# Query by meaning, not keywords
results = db.search_semantic(
    "Help those in need",
    context="spiritual"
)

print(f"Found {len(results)} semantically related concepts")
for result in results:
    print(f"Concept: {result['concept_text']}")
    print(f"Semantic Similarity: {result['semantic_similarity']:.2%}")
    print(f"Divine Alignment: {result['divine_resonance']:.2%}")
```

## 📊 Database Architecture

### Semantic Storage Schema
```sql
CREATE TABLE semantic_coordinates (
    id INTEGER PRIMARY KEY,
    concept_text TEXT NOT NULL,
    context TEXT NOT NULL,
    love REAL NOT NULL,      -- X-axis: Compassion, mercy
    power REAL NOT NULL,     -- Y-axis: Strength, authority  
    wisdom REAL NOT NULL,    -- Z-axis: Understanding, insight
    justice REAL NOT NULL,   -- W-axis: Righteousness, fairness
    divine_resonance REAL,
    distance_from_jehovah REAL,
    biblical_balance REAL
);
```

## 🔧 Components

### Database Core
- **`semantic_substrate_database.py`**: Main ICE-Centric database engine
- **`enhanced_semantic_database.py`**: Extended features and capabilities
- **`meaning_based_database.py`**: Natural language operations

### API & Deployment
- **`api/semantic_api.py`**: REST API for database operations
- **`docker-compose.yml`**: Containerized deployment
- **`Dockerfile`**: Production-ready container

## 📚 Documentation

- [Ethical Foundation & Transparency](docs/ETHICAL_FOUNDATION.md)
- [Docker Deployment Guide](docs/DOCKER.md) 
- [API Documentation](api/API_README.md)
- [Examples & Tutorials](examples/)

## 🧪 Testing

```bash
# Core database tests
python tests/test_semantic_database.py

# Integration tests with ICE Engine
python tests/test_integration.py

# Comprehensive test suite
python tests/run_all_tests.py

# API tests
python api/test_api.py
```

## 📄 License

**MIT License** - Copyright (c) 2025 BruinGrowly

Free and open source with no commercial restrictions.

## 🔗 Dependencies

- **[Semantic Substrate Engine](https://github.com/BruinGrowly/Semantic-Substrate-Engine)** v3.0+ - Core ICE framework
- **SQLite** - Embedded database storage
- **NumPy/SciPy** - Mathematical operations
- **Optional: Flask** - REST API server

---

**Semantic Substrate Database v2.0 - ICE-Centric**

**Built on Semantic Substrate Engine v3.0**: Intent → Context → Execution

**The difference is stored, retrieved, and validated.**