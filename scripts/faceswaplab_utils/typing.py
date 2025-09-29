# --- faceswaplab local import shim ---
import sys, os
_here = os.path.dirname(__file__)
if _here not in sys.path: sys.path.insert(0, _here)
# --- end shim ---

from typing import Tuple
from numpy import uint8
from insightface.app.common import Face as IFace
from PIL import Image
import numpy as np
from enum import Enum

PILImage = Image.Image
CV2ImgU8 = np.ndarray[int, np.dtype[uint8]]
Face = IFace
BoxCoords = Tuple[int, int, int, int]


class Gender(Enum):
    AUTO = -1
    FEMALE = 0
    MALE = 1
