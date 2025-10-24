# Semantic Substrate Database - Quick Start

Get up and running in 60 seconds! ⚡

## 🚀 The Absolute Fastest Way

### Linux / Mac:
```bash
./start_server.sh
```

### Windows:
```bash
start_server.bat
```

### Manual Start:
```bash
python api/simple_api.py
```

Then open: **http://localhost:8000**

---

## 📚 What You Get

### 1. Beautiful Web Interface
- Store concepts and see 4D coordinates
- Semantic search (search by meaning!)
- Proximity search in 4D space
- Live statistics dashboard
- Built-in tutorials

### 2. REST API
- Full REST API at `/api/`
- Interactive docs at `/api/docs`
- Try endpoints in your browser

### 3. Python Library
```python
from src.semantic_substrate_database import SemanticSubstrateDatabase

db = SemanticSubstrateDatabase("my_db.db")
db.store_concept("love", "biblical")
results = db.search_semantic("compassion", "biblical")
db.close()
```

---

## 🎯 Try These Examples

### Example 1: Store Your First Concept

1. Go to **"Store Concept"** tab
2. Enter: `love`
3. Context: `biblical`
4. Click **"Analyze & Store"**
5. See the 4D coordinates!

### Example 2: Semantic Search

1. First, store some concepts:
   - `love`, `faith`, `hope`, `charity`
2. Go to **"Semantic Search"** tab
3. Search for: `compassion and kindness`
4. See concepts ranked by semantic similarity!

### Example 3: Proximity Search

1. Go to **"Proximity Search"** tab
2. Set sliders: Love=0.9, Justice=0.8, Power=0.6, Wisdom=0.7
3. Click **"Find Nearby Concepts"**
4. See all concepts near that point in 4D space!

---

## 📖 Next Steps

- Read **HOW_TO_USE.md** for comprehensive guide
- Check **README.md** for architecture details
- Explore **http://localhost:8000/api/docs** for API reference
- Build your own semantic database!

---

## 🔧 Troubleshooting

### "Module not found" error
```bash
pip install numpy fastapi uvicorn
```

### Port already in use
```bash
# Use different port
uvicorn api.simple_api:app --port 8001
```

### Need help?
Open an issue: https://github.com/BruinGrowly/Semantic-Substrate-Database/issues

---

**Welcome to the future of meaning-native databases!** 🌌
