import numpy as np
from pathlib import Path
from PIL import Image
import random

BASE_DIR = Path('/work/11217/ianc8683/ls6/DNBP/data/spider/Test')

CORRUPTION_PROB = 0.20
random.seed(42)

def create_white_image(original_img: Image.Image):
    width, height = original_img.size
    return Image.new('RGB', (width, height), color='white')

def corrupt_all_frames_recursively(base_dir: Path, prob: float):
    print(f"Starting recursive corruption in: {base_dir}")
    all_image_files = list(base_dir.rglob('*.jpg'))
    if not all_image_files:
        print(f"Error: No JPG files found recursively under {base_dir}. Check your path.")
        return

    corrupted_count = 0
    total_count = len(all_image_files)
    print(f"Found {total_count} total image files.")

    for file_path in all_image_files:
        try:
            if random.random() < prob:
                with Image.open(file_path) as original_img:
                    white_img = create_white_image(original_img)
                    white_img.save(file_path)
                    corrupted_count += 1
        except Exception as e:
            print(f"Could not process or overwrite file {file_path}: {e}")
    
    print("\n--- Summary ---")
    print(f"Total files processed: {total_count}")
    print(f"Total files corrupted: {corrupted_count}")
    print(f"Actual corruption ratio: {corrupted_count/total_count:.4f}")
    print("All target sequences processed.")


if __name__ == "__main__":
    corrupt_all_frames_recursively(BASE_DIR, CORRUPTION_PROB)
