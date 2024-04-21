import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from tensorflow.keras.utils import save_img

dir = 'images/training/ticks'
if not os.path.exists(dir):
    os.makedirs(dir)

# Define an instance of the ImageDataGenerator
datagen = ImageDataGenerator(
    rotation_range=70, 
    width_shift_range=0.2, 
    height_shift_range=0.2, 
    shear_range=0.2, 
    zoom_range=0.2, 
    horizontal_flip=True, 
    fill_mode='nearest' 
)

# Load images and augment them
for filename in os.listdir(dir):
    if filename.endswith(('png', 'jpg', 'jpeg')):
        # Load the image
        img_path = os.path.join(dir, filename)
        image = load_img(img_path)
        x = img_to_array(image)  # Converts the image to an array
        x = x.reshape((1,) + x.shape)  # Reshape to (1, height, width, channels)

        # Generate new images
        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir=dir, save_prefix='ticks', save_format='jpeg'):
            i += 1
            if i >= 1: 
                break

print("Augmented images are saved at:", dir)