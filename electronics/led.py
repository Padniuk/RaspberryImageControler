import RPi.GPIO as GPIO
from dataclasses import dataclass, field
from typing import List


@dataclass
class DigitRepresentation:
    digitclr: List[int] = field(default_factory=lambda: [0, 0, 0, 0, 0, 0, 0])
    digit0: List[int] = field(default_factory=lambda: [1, 1, 1, 1, 1, 1, 0])
    digit1: List[int] = field(default_factory=lambda: [0, 1, 1, 0, 0, 0, 0])
    digit2: List[int] = field(default_factory=lambda: [1, 1, 0, 1, 1, 0, 1])
    digit3: List[int] = field(default_factory=lambda: [1, 1, 1, 1, 0, 0, 1])
    digit4: List[int] = field(default_factory=lambda: [0, 1, 1, 0, 0, 1, 1])
    digit5: List[int] = field(default_factory=lambda: [1, 0, 1, 1, 0, 1, 1])
    digit6: List[int] = field(default_factory=lambda: [1, 0, 1, 1, 1, 1, 1])
    digit7: List[int] = field(default_factory=lambda: [1, 1, 1, 0, 0, 0, 0])
    digit8: List[int] = field(default_factory=lambda: [1, 1, 1, 1, 1, 1, 1])
    digit9: List[int] = field(default_factory=lambda: [1, 1, 1, 1, 0, 1, 1])


class LEDControler(DigitRepresentation):
    def __init__(self, led_pins):
        super().__init__()
        self.led_pins = led_pins
        self.setup_pins()

    def __del__(self):
        for number in self.led_pins.values():
            GPIO.cleanup(number)

    def setup_pins(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        for name, number in self.led_pins.items():
            GPIO.setup(number, GPIO.OUT)

    def show_digit(self, digit):
        digits = [getattr(self, attr) for attr in dir(self) if attr.startswith("digit")]
        for pin, value in zip(self.led_pins.values(), self.digitclr):
            GPIO.output(pin, value)
        for pin, value in zip(self.led_pins.values(), digits[digit]):
            GPIO.output(pin, value)
