import numpy as np

def reduce_intensity_levels(image, levels):
    """Reduces the number of intensity levels in a grayscale image."""
    if not (levels > 1 and (levels & (levels - 1) == 0)):
        raise ValueError("Number of levels must be an integer power of 2 greater than 1.")
    factor = 256 // levels
    new_value_multiplier = 255 // (levels - 1)
    reduced_image = (image // factor) * new_value_multiplier
    return reduced_image.astype(np.uint8)