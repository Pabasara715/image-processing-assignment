import numpy as np

def reduce_spatial_resolution(image, block_size):
    output_image = image.copy()
    height, width = image.shape[:2]
    is_color = len(image.shape) == 3
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            y_end, x_end = min(y + block_size, height), min(x + block_size, width)
            block = image[y:y_end, x:x_end]
            if block.size == 0: continue
            avg_val = np.mean(block, axis=(0, 1) if is_color else None, dtype=int)
            output_image[y:y_end, x:x_end] = avg_val
    return output_image