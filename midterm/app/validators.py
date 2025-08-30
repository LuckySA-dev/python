from __future__ import annotations
import re
from . import config

PLATE_RE = re.compile(r"^[A-Z]{3}-\d{3,4}$")

def valid_year(y: int) -> bool:
    return 1970 <= int(y) <= 2100

def valid_rate(rate: float) -> bool:
    return 0.0 <= float(rate) <= 1_000_000.0

def valid_plate(plate: str) -> bool:
    return bool(PLATE_RE.match((plate or "").strip().upper()))

def nonempty(s: str) -> bool:
    return bool((s or "").strip())

def clamp_str(s: str, max_len: int) -> str:
    s = (s or "").strip()
    return s[:max_len]
