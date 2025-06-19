import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

def load_image_as_numpy(path):
    try:
        pil_image = Image.open(path)
        return np.array(pil_image)
    except FileNotFoundError:
        print(f"Error: Image not found at '{path}'")
        return None

def get_grayscale_image(color_image):
    if len(color_image.shape) == 3:
        return np.dot(color_image[...,:3], [0.299, 0.587, 0.114]).astype(np.uint8)
    return color_image

def show_images(images, titles, save_path=None):
    """
    Displays multiple images using Matplotlib.
    Saves the plot if a path is provided.
    Does NOT block the script.
    """
    num_images = len(images)
    cols = min(num_images, 4)
    rows = (num_images + cols - 1) // cols
    plt.figure(figsize=(5 * cols, 5 * rows))
    
    for i, (image, title) in enumerate(zip(images, titles)):
        plt.subplot(rows, cols, i + 1)
        plt.imshow(image, cmap='gray' if len(image.shape) == 2 else None)
        plt.title(title)
        plt.axis('off')
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
        print(f"Result saved to {save_path}")
    plt.close()