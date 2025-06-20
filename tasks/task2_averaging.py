import cv2

def apply_average_filter_cv(image, kernel_size):
    """Applies a spatial average filter using OpenCV's blur function."""
    return cv2.blur(image, (kernel_size, kernel_size))