#!/bin/bash
#
# Semantic Substrate Database - Quick Start Script
#
# This script starts the web server with the beautiful frontend interface
#

echo "===================================================================="
echo "  SEMANTIC SUBSTRATE DATABASE - Web Server"
echo "  The World's First Meaning-Native Database"
echo "===================================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✓ Python 3 found"

# Check if dependencies are installed
echo "Checking dependencies..."

python3 -c "import numpy" 2>/dev/null || {
    echo "Installing numpy..."
    pip install numpy
}

python3 -c "import fastapi" 2>/dev/null || {
    echo "Installing fastapi..."
    pip install fastapi
}

python3 -c "import uvicorn" 2>/dev/null || {
    echo "Installing uvicorn..."
    pip install uvicorn
}

echo "✓ All dependencies installed"
echo ""
echo "===================================================================="
echo "  Starting Server..."
echo "===================================================================="
echo ""
echo "  📊 Frontend:        http://localhost:8000"
echo "  📚 API Docs:        http://localhost:8000/api/docs"
echo "  ❤️  API Health:      http://localhost:8000/api/health"
echo ""
echo "===================================================================="
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the server
python3 api/simple_api.py
