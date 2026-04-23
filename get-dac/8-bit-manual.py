import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

bits = [0, 1, 2, 3, 4, 5, 6, 7]
GPIO.setup (bits, GPIO.OUT)

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print ()