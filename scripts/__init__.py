# --- faceswaplab package marker ---
import sys, os
_here = os.path.dirname(__file__)
if _here not in sys.path:
    sys.path.insert(0, _here)

# supaya "from scripts import X" bisa nemu modul di folder ini
import importlib
for name in [
    "faceswaplab",
    "configure",
    "faceswaplab_globals",
]:
    try:
        mod = importlib.import_module(name)
        sys.modules.setdefault(f"scripts.{name}", mod)
    except Exception:
        pass
