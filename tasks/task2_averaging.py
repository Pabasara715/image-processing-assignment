import numpy as np

def apply_average_filter_manual(image, kernel_size):
    """Applies a spatial average filter manually using NumPy."""
    # (Copy the function code from the previous answer here)
    is_color = len(image.shape) == 3
    output_image = np.zeros_like(image, dtype=np.float32)
    pad_width = kernel_size // 2
    padded_image = np.pad(image, ((pad_width, pad_width), (pad_width, pad_width), (0, 0)) if is_color else pad_width, mode='edge')
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            neighborhood = padded_image[y:y + kernel_size, x:x + kernel_size]
            if is_color:
                output_image[y, x, :] = np.mean(neighborhood, axis=(0, 1))
            else:
                output_image[y, x] = np.mean(neighborhood)
    return output_image.astype(np.uint8)