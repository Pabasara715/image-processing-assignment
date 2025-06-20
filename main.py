import os

# Import the new OpenCV-based functions
from tasks.utils import load_image_cv, get_grayscale_image_cv, show_images
from tasks.task1_intensity import reduce_intensity_levels
from tasks.task2_averaging import apply_average_filter_cv
from tasks.task3_rotation import rotate_image_cv
from tasks.task4_resolution import reduce_spatial_resolution

def run_all_tasks():
    """Main script to execute all assignment tasks using OpenCV."""
    print("Starting EC7212 Assignment 1 (OpenCV Implementation)...")

    # --- Setup ---
    image_path = 'sample_image.png'  
    results_dir = 'results_opencv' # Use a new directory for OpenCV results

    original_image_color = load_image_cv(image_path)
    if original_image_color is None:
        return

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # --- Execute Task 1: Intensity Reduction ---
    print("\n--- Running Task 1: Intensity Level Reduction ---")
    original_image_gray = get_grayscale_image_cv(original_image_color)
    levels_to_test = [16, 4, 2]
    reduced_intensity_images = [reduce_intensity_levels(original_image_gray, k) for k in levels_to_test]
    show_images(
        [original_image_gray] + reduced_intensity_images,
        ['Original Grayscale'] + [f'{k} Levels' for k in levels_to_test],
        save_path=os.path.join(results_dir, 'task1_intensity_reduction.png')
    )

    # --- Execute Task 2: Spatial Averaging ---
    print("\n--- Running Task 2: Spatial Averaging ---")
    kernels_to_test = [3, 10, 20]
    averaged_images = [apply_average_filter_cv(original_image_color, k) for k in kernels_to_test]
    show_images(
        [original_image_color] + averaged_images,
        ['Original'] + [f'{k}x{k} Average' for k in kernels_to_test],
        save_path=os.path.join(results_dir, 'task2_spatial_averaging.png')
    )
    
    # --- Execute Task 3: Image Rotation ---
    print("\n--- Running Task 3: Image Rotation ---")
    rotated_90 = rotate_image_cv(original_image_color, 90)
    rotated_45 = rotate_image_cv(original_image_color, 45)
    show_images(
        [original_image_color, rotated_90, rotated_45],
        ['Original', 'Rotated 90°', 'Rotated 45°'],
        save_path=os.path.join(results_dir, 'task3_rotation.png')
    )

    # --- Execute Task 4: Spatial Resolution Reduction ---
    print("\n--- Running Task 4: Spatial Resolution Reduction ---")
    blocks_to_test = [3, 5, 7]
    pixelated_images = [reduce_spatial_resolution(original_image_color, b) for b in blocks_to_test]
    show_images(
        [original_image_color] + pixelated_images,
        ['Original'] + [f'{b}x{b} Block Average' for b in blocks_to_test],
        save_path=os.path.join(results_dir, 'task4_spatial_reduction.png')
    )

    print(f"\nAll tasks completed. Results saved in '{results_dir}' directory.")

if __name__ == '__main__':
    run_all_tasks()