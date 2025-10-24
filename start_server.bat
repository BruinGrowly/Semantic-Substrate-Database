@echo off
REM Semantic Substrate Database - Quick Start Script (Windows)

echo ====================================================================
echo   SEMANTIC SUBSTRATE DATABASE - Web Server
echo   The World's First Meaning-Native Database
echo ====================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo Installing dependencies...
pip install numpy fastapi uvicorn

echo.
echo ====================================================================
echo   Starting Server...
echo ====================================================================
echo.
echo   Frontend:        http://localhost:8000
echo   API Docs:        http://localhost:8000/api/docs
echo   API Health:      http://localhost:8000/api/health
echo.
echo ====================================================================
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the server
python api\simple_api.py
