"""
Unit tests for Semantic Substrate Database API
Tests API functionality without requiring a running server
"""

import sys
import os
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Delete test database if it exists
test_db_path = "test_semantic_api.db"
try:
    os.unlink(test_db_path)
except:
    pass

# Set environment variable for test database
os.environ["SEMANTIC_DB_PATH"] = test_db_path

# Now import app (after setting env variable)
from fastapi.testclient import TestClient
from api.semantic_api import app

# Create test client - will be initialized in run_all_tests
client = None


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "version" in data
    print("[PASS] Root endpoint works")


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    if response.status_code != 200:
        print(f"Health check failed with status {response.status_code}")
        print(f"Response: {response.text}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["database_connected"] == True
    print("[PASS] Health check works")


def test_create_concept():
    """Test creating a concept"""
    response = client.post(
        "/concepts",
        json={"text": "love", "context": "biblical"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["text"] == "love"
    assert data["context"] == "biblical"
    assert "coordinates" in data
    assert "divine_resonance" in data
    print(f"[PASS] Create concept works (ID: {data['id']})")
    return data["id"]


def test_get_concept(concept_id):
    """Test getting a concept by ID"""
    response = client.get(f"/concepts/{concept_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == concept_id
    assert "coordinates" in data
    print(f"[PASS] Get concept works (ID: {concept_id})")


def test_list_concepts():
    """Test listing concepts"""
    response = client.get("/concepts?limit=10")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    print(f"[PASS] List concepts works ({len(data)} concepts)")


def test_semantic_search():
    """Test semantic search - THE KILLER FEATURE!"""
    # Create some concepts first
    concepts = ["love", "mercy", "grace", "faith"]
    for concept in concepts:
        client.post("/concepts", json={"text": concept, "context": "biblical"})

    # Search
    response = client.post(
        "/search/semantic",
        json={"query": "compassion and kindness", "context": "biblical", "limit": 5}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    # Verify result structure
    result = data[0]
    assert "concept_text" in result
    assert "semantic_similarity" in result
    assert "query_alignment" in result

    print(f"[PASS] Semantic search works - found {len(data)} similar concepts")
    print(f"  Top result: '{result['concept_text']}' (similarity: {result['semantic_similarity']:.3f})")


def test_proximity_search():
    """Test proximity search in 4D semantic space"""
    response = client.post(
        "/search/proximity",
        json={
            "coordinates": {
                "love": 0.9,
                "power": 0.6,
                "wisdom": 0.8,
                "justice": 0.8
            },
            "max_distance": 0.5,
            "context": "biblical",
            "limit": 5
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    print(f"[PASS] Proximity search works - found {len(data)} nearby concepts")


def test_divine_resonance_search():
    """Test divine resonance search"""
    response = client.get("/search/divine-resonance?min_resonance=0.0&context=biblical&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    print(f"[PASS] Divine resonance search works - found {len(data)} aligned concepts")


def test_anchor_search():
    """Test universal anchor navigation"""
    response = client.get("/search/nearest-anchor/7?max_distance=2.0&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    print(f"[PASS] Anchor navigation works - found {len(data)} concepts near anchor 7")


def test_create_sacred_number():
    """Test creating sacred number"""
    response = client.post(
        "/sacred-numbers",
        json={"value": 7}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["value"] == 7.0
    assert "is_sacred" in data
    assert "sacred_resonance" in data
    print(f"[PASS] Create sacred number works (sacred: {data['is_sacred']})")


def test_list_sacred_numbers():
    """Test listing sacred numbers"""
    # Create some sacred numbers
    for num in [7, 12, 40]:
        client.post("/sacred-numbers", json={"value": num})

    response = client.get("/sacred-numbers?only_sacred=true")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    print(f"[PASS] List sacred numbers works ({len(data)} numbers)")


def test_statistics():
    """Test statistics endpoint"""
    response = client.get("/statistics")
    assert response.status_code == 200
    data = response.json()
    assert "total_concepts" in data
    assert "sacred_numbers_count" in data
    assert "avg_divine_resonance" in data
    print(f"[PASS] Statistics works (concepts: {data['total_concepts']})")


def test_export_database():
    """Test database export"""
    response = client.post("/export")
    assert response.status_code == 200
    data = response.json()
    assert "metadata" in data
    assert "concepts" in data
    assert "sacred_numbers" in data
    print("[PASS] Database export works")


def test_clear_cache():
    """Test cache clearing"""
    response = client.delete("/cache")
    assert response.status_code == 204
    print("[PASS] Cache clearing works")


def test_invalid_context():
    """Test validation - invalid context"""
    response = client.post(
        "/concepts",
        json={"text": "test", "context": "invalid_context"}
    )
    assert response.status_code == 422  # Validation error
    print("[PASS] Input validation works")


def test_concept_not_found():
    """Test 404 for non-existent concept"""
    response = client.get("/concepts/999999")
    assert response.status_code == 404
    print("[PASS] 404 handling works")


def run_all_tests():
    """Run all API tests"""
    global client

    print("=" * 80)
    print("SEMANTIC SUBSTRATE DATABASE API - UNIT TESTS")
    print("=" * 80)

    # Initialize test client with context manager to trigger lifespan
    with TestClient(app) as client:
        try:
            # Basic endpoints
            print("\n[1] Basic Endpoints")
            print("-" * 40)
            test_root_endpoint()
            test_health_check()
            test_statistics()

            # Concept management
            print("\n[2] Concept Management")
            print("-" * 40)
            concept_id = test_create_concept()
            test_get_concept(concept_id)
            test_list_concepts()

            # Revolutionary searches
            print("\n[3] Revolutionary Search Endpoints")
            print("-" * 40)
            test_semantic_search()
            test_proximity_search()
            test_divine_resonance_search()
            test_anchor_search()

            # Sacred numbers
            print("\n[4] Sacred Number Endpoints")
            print("-" * 40)
            test_create_sacred_number()
            test_list_sacred_numbers()

            # Utilities
            print("\n[5] Utility Endpoints")
            print("-" * 40)
            test_export_database()
            test_clear_cache()

            # Error handling
            print("\n[6] Error Handling")
            print("-" * 40)
            test_invalid_context()
            test_concept_not_found()

            print("\n" + "=" * 80)
            print("ALL TESTS PASSED - API IS FULLY OPERATIONAL!")
            print("=" * 80)

            return True

        except AssertionError as e:
            import traceback
            print(f"\n[FAIL] TEST FAILED: {e}")
            traceback.print_exc()
            return False
        except Exception as e:
            import traceback
            print(f"\n[ERROR] ERROR: {e}")
            traceback.print_exc()
            return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
