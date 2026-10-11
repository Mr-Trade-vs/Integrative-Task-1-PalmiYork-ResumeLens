import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROFILE_PATH = ROOT / "config" / "profiles.json"

def load_profiles(path: Path = PROFILE_PATH) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)
