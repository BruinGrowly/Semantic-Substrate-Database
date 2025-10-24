"""
SEMANTIC SUBSTRATE DATABASE - Simple Working API

A simplified REST API that works with the current database implementation.
Provides semantic search and 4D coordinate storage functionality.

Run with: uvicorn simple_api:app --reload
Then visit: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from pathlib import Path
import sys

# Add src to path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))
sys.path.insert(0, str(PROJECT_ROOT))

# Import with fallback
try:
    from src.semantic_substrate_database import SemanticSubstrateDatabase
except ImportError:
    from semantic_substrate_database import SemanticSubstrateDatabase

# ============================================================================
# MODELS
# ============================================================================

class ConceptRequest(BaseModel):
    """Request to store a concept"""
    text: str = Field(..., min_length=1, max_length=500)
    context: str = Field(default="biblical")

    class Config:
        schema_extra = {
            "example": {
                "text": "love",
                "context": "biblical"
            }
        }


class ConceptResponse(BaseModel):
    """Response with concept and coordinates"""
    concept_text: str
    context: str
    coordinates: Dict[str, float]
    divine_resonance: float
    distance_from_jehovah: float
    biblical_balance: float


class SearchRequest(BaseModel):
    """Semantic search request"""
    query: str = Field(..., min_length=1)
    context: str = Field(default="biblical")
    limit: int = Field(default=10, ge=1, le=100)


class ProximityRequest(BaseModel):
    """Search by coordinates"""
    love: float = Field(..., ge=0.0, le=1.0)
    justice: float = Field(..., ge=0.0, le=1.0)
    power: float = Field(..., ge=0.0, le=1.0)
    wisdom: float = Field(..., ge=0.0, le=1.0)
    max_distance: float = Field(default=0.5, ge=0.0, le=4.0)
    context: Optional[str] = None
    limit: int = Field(default=10, ge=1, le=100)


# ============================================================================
# APP SETUP
# ============================================================================

app = FastAPI(
    title="Semantic Substrate Database API",
    description="Revolutionary meaning-native database with 4D semantic coordinates",
    version="2.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database instance
db = SemanticSubstrateDatabase("semantic_api.db")

# Mount static files for frontend
try:
    static_path = PROJECT_ROOT / "frontend"
    static_path.mkdir(exist_ok=True)
    app.mount("/", StaticFiles(directory=str(static_path), html=True), name="frontend")
except Exception as e:
    print(f"Warning: Could not mount frontend directory: {e}")


# ============================================================================
# ENDPOINTS
# ============================================================================

@app.get("/api/")
async def root():
    """API information"""
    return {
        "name": "Semantic Substrate Database API",
        "version": "2.0.0",
        "description": "World's first meaning-native database",
        "docs": "/api/docs",
        "frontend": "/",
    }


@app.get("/api/health")
async def health_check():
    """Health check"""
    try:
        # Test database
        test = db.get_concept("test", "general")
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "degraded",
            "database": "error",
            "error": str(e)
        }


@app.post("/api/concepts", response_model=ConceptResponse)
async def store_concept(request: ConceptRequest):
    """
    Store a concept and get its 4D semantic coordinates

    The database analyzes the meaning and maps it to 4D space:
    - Love: Compassion, kindness, unity
    - Justice: Fairness, righteousness, truth
    - Power: Authority, strength, capability
    - Wisdom: Understanding, knowledge, insight
    """
    try:
        # Store concept
        concept_id = db.store_concept(request.text, request.context)

        # Retrieve full details
        result = db.get_concept(request.text, request.context)

        if not result:
            raise HTTPException(status_code=500, detail="Failed to retrieve stored concept")

        return ConceptResponse(
            concept_text=result['concept_text'],
            context=result['context'],
            coordinates={
                'love': result['love'],
                'justice': result['justice'],
                'power': result['power'],
                'wisdom': result['wisdom']
            },
            divine_resonance=result['divine_resonance'],
            distance_from_jehovah=result['distance_from_jehovah'],
            biblical_balance=result['biblical_balance']
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error storing concept: {str(e)}")


@app.get("/api/concepts/{text}", response_model=ConceptResponse)
async def get_concept_by_text(
    text: str,
    context: str = Query(default="biblical")
):
    """Get concept by text"""
    try:
        result = db.get_concept(text, context)

        if not result:
            raise HTTPException(status_code=404, detail=f"Concept '{text}' not found in context '{context}'")

        return ConceptResponse(
            concept_text=result['concept_text'],
            context=result['context'],
            coordinates={
                'love': result['love'],
                'justice': result['justice'],
                'power': result['power'],
                'wisdom': result['wisdom']
            },
            divine_resonance=result['divine_resonance'],
            distance_from_jehovah=result['distance_from_jehovah'],
            biblical_balance=result['biblical_balance']
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving concept: {str(e)}")


@app.post("/api/search/semantic")
async def semantic_search(request: SearchRequest):
    """
    Revolutionary semantic search - finds concepts by MEANING similarity

    This is NOT text matching! The database:
    1. Analyzes the semantic meaning of your query
    2. Maps it to 4D semantic coordinates
    3. Finds concepts closest in meaning-space

    Example: Search "compassion" and find "love", "mercy", "kindness"
    """
    try:
        results = db.search_semantic(
            request.query,
            context=request.context,
            limit=request.limit
        )

        return {
            "query": request.query,
            "context": request.context,
            "results_count": len(results),
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.post("/api/search/proximity")
async def proximity_search(request: ProximityRequest):
    """
    Search by proximity in 4D semantic space

    Provide 4D coordinates and find all concepts nearby.
    Distance is Euclidean in 4D space.
    """
    try:
        target_coords = {
            'love': request.love,
            'justice': request.justice,
            'power': request.power,
            'wisdom': request.wisdom
        }

        results = db.query_by_proximity(
            target_coords,
            max_distance=request.max_distance,
            context=request.context,
            limit=request.limit
        )

        return {
            "target_coordinates": target_coords,
            "max_distance": request.max_distance,
            "results_count": len(results),
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Proximity search failed: {str(e)}")


@app.get("/api/stats")
async def get_stats():
    """Get database statistics"""
    try:
        cursor = db.conn.cursor()

        # Count total concepts
        cursor.execute("SELECT COUNT(*) FROM semantic_coordinates")
        total = cursor.fetchone()[0]

        # Count by context
        cursor.execute("SELECT context, COUNT(*) FROM semantic_coordinates GROUP BY context")
        contexts = {row[0]: row[1] for row in cursor.fetchall()}

        # Average metrics
        cursor.execute("""
            SELECT
                AVG(divine_resonance) as avg_resonance,
                AVG(distance_from_jehovah) as avg_distance,
                AVG(biblical_balance) as avg_balance
            FROM semantic_coordinates
        """)
        row = cursor.fetchone()

        return {
            "total_concepts": total,
            "by_context": contexts,
            "averages": {
                "divine_resonance": float(row[0]) if row[0] else 0,
                "distance_from_jehovah": float(row[1]) if row[1] else 0,
                "biblical_balance": float(row[2]) if row[2] else 0
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Stats failed: {str(e)}")


@app.on_event("shutdown")
async def shutdown_event():
    """Close database on shutdown"""
    db.close()


if __name__ == "__main__":
    import uvicorn

    print("=" * 80)
    print("SEMANTIC SUBSTRATE DATABASE API v2.0")
    print("=" * 80)
    print("Server starting...")
    print("API Documentation: http://localhost:8000/api/docs")
    print("Frontend: http://localhost:8000/")
    print("=" * 80)

    uvicorn.run(
        "simple_api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
