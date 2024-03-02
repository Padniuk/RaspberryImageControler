import subprocess
from PIL import Image, ImageOps
from io import BytesIO
import numpy as np


class USBCameraControler:
    def __init__(self, command):
        self.command = command

    def take_picture(self):
        process = subprocess.Popen(
            self.command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output, error = process.communicate()
        image_data = BytesIO(output)

        return image_data

    def get_processed_image(self, intensity_cut=5):
        image = Image.open(self.take_picture())
        resized_image = image.resize((28, 28)).convert("L")
        image_array = np.array(ImageOps.invert(resized_image))
        image_array[image_array < intensity_cut] = 0

        return image_array.reshape(1, 28, 28, 1).astype("float32") / 255.0

    def image_debug(self, intensity_cut=5):
        image = Image.open(self.take_picture())
        resized_image = image.resize((28, 28)).convert("L")
        image_array = np.array(ImageOps.invert(resized_image))
        image_array[image_array < intensity_cut] = 0

        for row in image_array:
            row_str = [('.' if pixel < 128 else '#') for pixel in row]
            print(''.join(row_str))

