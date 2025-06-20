import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def load_image_cv(path):
    """Loads an image using OpenCV."""
    image = cv2.imread(path)
    if image is None:
        print(f"Error: Image not found or could not be read at '{path}'")
    return image

def get_grayscale_image_cv(color_image):
    """Converts a color image (BGR) to grayscale using OpenCV."""
    return cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

def show_images(images, titles, save_path=None):
    """Displays multiple images using Matplotlib and saves the plot."""
    num_images = len(images)
    cols = min(num_images, 4)
    rows = (num_images + cols - 1) // cols
    plt.figure(figsize=(5 * cols, 5 * rows))
    
    for i, (image, title) in enumerate(zip(images, titles)):
        plt.subplot(rows, cols, i + 1)
        
        # IMPORTANT: Convert BGR to RGB for correct color display in Matplotlib
        if len(image.shape) == 3:
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        else: # Grayscale
            plt.imshow(image, cmap='gray')
            
        plt.title(title)
        plt.axis('off')
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
        print(f"Result saved to {save_path}")
    plt.close()