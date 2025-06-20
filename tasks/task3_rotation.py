import cv2
import numpy as np

def rotate_image_cv(image, angle):

    if angle % 90 == 0:
        if angle == 90:
            return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        if angle == 180:
            return cv2.rotate(image, cv2.ROTATE_180)
        if angle == 270:
            return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        if angle == 0 or angle % 360 == 0:
            return image

    height, width = image.shape[:2]
    image_center = (width / 2, height / 2)

    # Get the rotation matrix
    rotation_mat = cv2.getRotationMatrix2D(image_center, -angle, 1.0)

    # --- Calculate the new bounding box dimensions ---
    abs_cos = abs(rotation_mat[0, 0])
    abs_sin = abs(rotation_mat[0, 1])

    new_width = int(height * abs_sin + width * abs_cos)
    new_height = int(height * abs_cos + width * abs_sin)

    # --- Adjust the rotation matrix to account for the new canvas size ---
    rotation_mat[0, 2] += new_width / 2 - image_center[0]
    rotation_mat[1, 2] += new_height / 2 - image_center[1]

    # Perform the actual rotation and resizing
    rotated_image = cv2.warpAffine(image, rotation_mat, (new_width, new_height))
    
    return rotated_image