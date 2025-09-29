# --- faceswaplab local import shim ---
import sys, os
_here = os.path.dirname(__file__)
if _here not in sys.path: sys.path.insert(0, _here)
# --- end shim ---

from types import ModuleType


def check_install() -> None:
    # Very ugly hack :( due to sdnext optimization not calling install.py every time if git log has not changed
    import importlib.util
    import sys
    import os

    current_dir = os.path.dirname(os.path.realpath(__file__))
    check_install_path = os.path.join(current_dir, "..", "..", "install.py")
    spec = importlib.util.spec_from_file_location("check_install", check_install_path)
    if spec != None:
        check_install: ModuleType = importlib.util.module_from_spec(spec)
        sys.modules["check_install"] = check_install
        spec.loader.exec_module(check_install)  # type: ignore
        check_install.check_install()  # type: ignore
        #### End of ugly hack :( !
