import RPi.GPIO as GPIO


class FanControler:
    def __init__(self, pwm_pin, signal_frequency=1000):
        self.pwm_pin = pwm_pin
        self.signal_frequency = signal_frequency
        self.setup_pins()
        self.pwm = GPIO.PWM(self.pwm_pin, self.signal_frequency)
        self.start_fan()

    def __del__(self):
        self.pwm.stop()
        GPIO.cleanup(self.pwm_pin)

    def setup_pins(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pwm_pin, GPIO.OUT)

    def start_fan(self):
        self.pwm.start(100)

    def change_frequency(self, new_frequency):
        self.pwm.start(0.5 * new_frequency + 50)
