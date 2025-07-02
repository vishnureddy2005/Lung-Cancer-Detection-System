import os
import shutil
import random

source_dir = 'The IQ-OTHNCCD lung cancer dataset'
dest_dir = 'dataset'
train_ratio = 0.8

# Correct folder names based on your screenshot
for label in ['Bengin cases', 'Malignant cases', 'Normal cases']:
    images = os.listdir(os.path.join(source_dir, label))
    random.shuffle(images)
    train_count = int(len(images) * train_ratio)

    train_images = images[:train_count]
    val_images = images[train_count:]

    for img in train_images:
        src = os.path.join(source_dir, label, img)
        dst = os.path.join(dest_dir, 'train', label)
        os.makedirs(dst, exist_ok=True)
        shutil.copy(src, dst)

    for img in val_images:
        src = os.path.join(source_dir, label, img)
        dst = os.path.join(dest_dir, 'val', label)
        os.makedirs(dst, exist_ok=True)
        shutil.copy(src, dst)
