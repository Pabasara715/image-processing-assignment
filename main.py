import os

from tasks.utils import load_image_as_numpy, get_grayscale_image, show_images
from tasks.task1_intensity import reduce_intensity_levels

def run_all_tasks():
    """Main script to execute all assignment tasks."""
    print("Starting EC7212 Assignment 1 (Modular Structure)...")

    # --- Setup ---
    image_path = 'sample_image.png'  
    results_dir = 'results_modular'

    original_image_color = load_image_as_numpy(image_path)
    if original_image_color is None:
        return

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # --- Execute Task 1: Intensity Reduction ---
    print("\n--- Running Task 1: Intensity Level Reduction ---")
    original_image_gray = get_grayscale_image(original_image_color)
    levels_to_test = [16, 4, 2]
    reduced_intensity_images = [reduce_intensity_levels(original_image_gray, k) for k in levels_to_test]
    show_images(
        [original_image_gray] + reduced_intensity_images,
        ['Original Grayscale'] + [f'{k} Levels' for k in levels_to_test],
        save_path=os.path.join(results_dir, 'task1_intensity_reduction.png')
    )

    print("\nAll tasks completed. Results saved in '{}' directory.".format(results_dir))

if __name__ == '__main__':
    run_all_tasks()