import numpy as np
from pathlib import Path
from PIL import Image
import random

BASE_DIR = Path('/work/11217/ianc8683/ls6/DNBP/data/hand_tracking/F-PHAB/Video_files/')
TARGETS = ('Subject_2', 'Subject_5', 'Subject_6')

NOISE_PROB = 0.05
np.random.seed(42)

def add_noise():
    print(f'Starting corruption in: {BASE_DIR}')

    for subject in TARGETS:
        subject_dir = BASE_DIR / subject
        all_files = list(subject_dir.rglob('*.png'))
        print(f'Processing {subject}: {len(all_files)} depth maps found.')

        for file_path in all_files:
            try:
                with Image.open(file_path) as img:
                    img_arr = np.array(img)

                rnd = np.random.random(img_arr.shape[:2])
                img_arr[rnd < (NOISE_PROB / 2)] = 0
                img_arr[rnd > (1 - NOISE_PROB / 2)] = 255

                Image.fromarray(img_arr).save(file_path)
            except Exception as e:
                print(f'Failed to process {file_path}: {e}')

    print('\nCorruption complete. Originals are overwritten.')

if __name__ == '__main__':
    add_noise()

