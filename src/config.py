from pathlib import Path
from typing import Any

#directorys
BASE_DIR = Path.cwd()
OUTPUT_DIR = BASE_DIR/"reports"

#styles (family, size, "style1 style2 ...")
HEADER : dict[str, Any] = {
    "font": ("Arial", 24, "bold"),
    "fg": "black"
}
SUB_HEADER : dict[str, Any] = {
    "font": ("Arial", 16, ""),
    "fg": "grey"
}