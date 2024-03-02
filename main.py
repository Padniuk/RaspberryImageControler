import time
import numpy as np
from tensorflow.keras.models import load_model
from electronics.led import LEDControler
from electronics.fan import FanControler
from electronics.usb_camera import USBCameraControler


def main():
    usb_camera_controler = USBCameraControler("fswebcam -r 480x320 -S 20 --no-banner -")
    led_pins = {"A": 37, "B": 33, "C": 36, "D": 38, "E": 40, "F": 31, "G": 35}
    led_controler = LEDControler(led_pins)
    fan_controler = FanControler(29, 1000)

    model = load_model("my_model.h5")

    while True:
        prediction = model.predict(usb_camera_controler.get_processed_image())
        predicted_label = np.argmax(prediction)
        led_controler.show_digit(predicted_label)
        fan_controler.change_frequency(10 * predicted_label)
        usb_camera_controler.image_debug()
        time.sleep(10)


if __name__ == "__main__":
    main()
