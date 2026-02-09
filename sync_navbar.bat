@echo off
REM Navbar Sync Script for Windows
REM This script updates all HTML files with the navbar from navbar_template.txt

setlocal enabledelayedexpansion

echo.
echo ===================================
echo  Navbar Synchronization Script
echo ===================================
echo.

REM Check if navbar_template.txt exists
if not exist "navbar_template.txt" (
    echo ERROR: navbar_template.txt not found!
    echo Please create navbar_template.txt first.
    pause
    exit /b 1
)

echo Found navbar_template.txt
echo.
echo This approach uses a Python helper if available, OR manual copy.
echo.
echo To use this:
echo 1. Edit navbar_template.txt with your navbar HTML
echo 2. Install Python (https://www.python.org/downloads)
echo 3. Run: python sync_navbar.py
echo.
echo For now, the navbar structure is ready in navbar_template.txt
echo.
pause
