# --- faceswaplab local import shim ---
import sys, os
_here = os.path.dirname(__file__)
if _here not in sys.path: sys.path.insert(0, _here)
# --- end shim ---

from faceswaplab_postprocessing.postprocessing_options import (
    PostProcessingOptions,
)
from faceswaplab_utils.faceswaplab_logging import logger
from PIL import Image
import numpy as np
from modules import codeformer_model
from faceswaplab_utils.typing import *


def upscale_img(image: PILImage, pp_options: PostProcessingOptions) -> PILImage:
    if pp_options.upscaler is not None and pp_options.upscaler.name != "None":
        original_image: PILImage = image.copy()
        logger.info(
            "Upscale with %s scale = %s",
            pp_options.upscaler.name,
            pp_options.scale,
        )
        result_image = pp_options.upscaler.scaler.upscale(
            image, pp_options.scale, pp_options.upscaler.data_path  # type: ignore
        )

        # FIXME : Could be better (managing images whose dimensions are not multiples of 16)
        if pp_options.scale == 1 and original_image.size == result_image.size:
            logger.debug(
                "Sizes orig=%s, result=%s", original_image.size, result_image.size
            )
            result_image = Image.blend(
                original_image, result_image, pp_options.upscale_visibility
            )
        return result_image
    return image


def restore_face(image: Image.Image, pp_options: PostProcessingOptions) -> Image.Image:
    if pp_options.face_restorer is not None:
        original_image = image.copy()
        logger.info("Restore face with %s", pp_options.face_restorer.name())
        numpy_image = np.array(image)
        if pp_options.face_restorer_name == "CodeFormer":
            numpy_image = codeformer_model.codeformer.restore(
                numpy_image, w=pp_options.codeformer_weight
            )
        else:
            numpy_image = pp_options.face_restorer.restore(numpy_image)

        restored_image = Image.fromarray(numpy_image)
        result_image = Image.blend(
            original_image, restored_image, pp_options.restorer_visibility
        )
        return result_image
    return image
