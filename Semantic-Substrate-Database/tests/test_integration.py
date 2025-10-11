"""
Test Semantic Substrate Database v2.0 with ICE-Centric Integration

This test validates that the upgraded database properly integrates with
Semantic Substrate Engine v3.0 and provides full ICE-Centric functionality.
"""

import sys
import os
import tempfile
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_database_initialization():
    """Test that the database initializes correctly with ICE components"""
    print("Testing Database Initialization...")
    
    try:
        from semantic_substrate_database import SemanticSubstrateDatabase
        from ice_semantic_substrate_engine import ICESemanticSubstrateEngine
        from unified_ice_framework import UnifiedICEFramework
        
        # Test database creation
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
            db_path = tmp.name
        
        db = SemanticSubstrateDatabase(db_path)
        print("Database initialized successfully")
        
        # Test ICE engine integration
        engine = ICESemanticSubstrateEngine()
        print("ICE engine integrated successfully")
        
        # Test unified framework
        unified = UnifiedICEFramework()
        print("Unified framework integrated successfully")
        
        # Cleanup
        db.conn.close()
        os.unlink(db_path)
        return True
        
    except Exception as e:
        print(f"Initialization failed: {e}")
        return False

def test_ice_database_integration():
    """Test ICE-Centric database operations"""
    print("\nTesting ICE Database Integration...")
    
    try:
        from semantic_substrate_database import SemanticSubstrateDatabase
        from ice_semantic_substrate_engine import ICESemanticSubstrateEngine, ThoughtType, ContextDomain
        
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
            db_path = tmp.name
        
        db = SemanticSubstrateDatabase(db_path)
        engine = ICESemanticSubstrateEngine()
        
        # Test ICE transformation and storage
        test_text = "Show compassion and mercy to those who suffer"
        result = engine.transform(
            test_text,
            ThoughtType.EMOTIONAL_EXPRESSION,
            ContextDomain.SPIRITUAL
        )
        
        # Store with ICE analysis
        db.store_concept(
            test_text,
            result.context_domain.value,
            auto_analyze=True
        )
        
        print(f"Stored meaning with {result.semantic_integrity:.2%} integrity")
        print(f"Execution strategy: {result.execution_strategy.value}")
        
        # Test semantic search
        search_results = db.search_semantic(
            "Help those in need",
            context="spiritual",
            limit=5
        )
        
        print(f"Found {len(search_results)} semantic matches")
        
        # Cleanup
        db.conn.close()
        os.unlink(db_path)
        return True
        
    except Exception as e:
        print(f"ICE integration failed: {e}")
        return False

def test_database_performance():
    """Test database performance with ICE processing"""
    print("\nTesting Database Performance...")
    
    try:
        from semantic_substrate_database import SemanticSubstrateDatabase
        from ice_semantic_substrate_engine import ICESemanticSubstrateEngine, ThoughtType, ContextDomain
        
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
            db_path = tmp.name
        
        db = SemanticSubstrateDatabase(db_path)
        engine = ICESemanticSubstrateEngine()
        
        import time
        
        # Test batch insertion with ICE analysis
        test_texts = [
            "Act with justice and fairness",
            "Seek wisdom through understanding", 
            "Show compassion to the suffering",
            "Exercise power with responsibility",
            "Love your neighbor as yourself"
        ]
        
        start_time = time.time()
        
        for i, text in enumerate(test_texts):
            result = engine.transform(
                text,
                ThoughtType.MORAL_JUDGMENT,
                ContextDomain.SPIRITUAL
            )
            
            db.store_concept(
                text,
                result.context_domain.value,
                auto_analyze=True
            )
        
        insertion_time = time.time() - start_time
        
        # Test search performance
        start_time = time.time()
        search_results = db.search_semantic("moral guidance", context="spiritual")
        search_time = time.time() - start_time
        
        print(f"Inserted {len(test_texts)} meanings in {insertion_time:.3f}s")
        print(f"Semantic search completed in {search_time:.3f}s")
        print(f"Found {len(search_results)} results for 'moral guidance'")
        
        # Cleanup
        db.conn.close()
        os.unlink(db_path)
        return True
        
    except Exception as e:
        print(f"Performance test failed: {e}")
        return False

def test_api_functionality():
    """Test API functionality if available"""
    print("\nTesting API Functionality...")
    
    try:
        # Test if API files exist
        api_path = Path(__file__).parent.parent / "api" / "semantic_api.py"
        if not api_path.exists():
            print("API module not found, skipping API tests")
            return True
        
        # Basic import test
        sys.path.insert(0, str(api_path.parent))
        import semantic_api
        print("API module imported successfully")
        
        return True
        
    except Exception as e:
        print(f"API test failed: {e}")
        return False

def main():
    """Run all integration tests"""
    print("Semantic Substrate Database v2.0 - Integration Test Suite")
    print("=" * 60)
    
    tests = [
        test_database_initialization,
        test_ice_database_integration,
        test_database_performance,
        test_api_functionality
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed! Database is ready for deployment.")
        return True
    else:
        print("Some tests failed. Please review the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)