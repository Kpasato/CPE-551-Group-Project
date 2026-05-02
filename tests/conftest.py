# conftest.py
import sys
from pathlib import Path
# Add the project root folder to Python's import path for pytest
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))
