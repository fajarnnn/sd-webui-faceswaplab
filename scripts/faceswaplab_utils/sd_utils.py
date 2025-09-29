# --- faceswaplab local import shim ---
import sys, os
_here = os.path.dirname(__file__)
if _here not in sys.path: sys.path.insert(0, _here)
# --- end shim ---

from typing import Any
from modules.shared import opts


def get_sd_option(name: str, default: Any) -> Any:
    assert opts.data is not None
    return opts.data.get(name, default)
