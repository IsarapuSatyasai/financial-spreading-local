"""Small helpers."""
from pathlib import Path

def ensure_dirs():
    for p in ["data/input", "data/templates", "data/output"]:
        Path(p).mkdir(parents=True, exist_ok=True)
