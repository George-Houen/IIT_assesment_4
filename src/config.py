from pathlib import Path
from typing import Any

#directorys
BASE_DIR = Path.cwd()

#styles (family, size, "style1 style2 ...")
HEADER : dict[str, Any] = {
    "font": ("Arial", 24, "bold"),
    "fg": "grey"
}
SUB_HEADER_FONT = ("Arial", 24, "bold")