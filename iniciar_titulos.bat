@echo off
cd /d "%~dp0"
python -c "import requests, yaml" >nul 2>&1
if errorlevel 1 (
  python -m pip install -r title_creator\requirements.txt
  if errorlevel 1 (
    pause
    exit /b 1
  )
)
python -m title_creator.server --open
pause
