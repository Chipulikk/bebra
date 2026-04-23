import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)

led_16 = 16
GPIO.setup (led_16, GPIO.OUT)

led_5 = 5
GPIO.setup (led_5, GPIO.OUT)

led_25 = 25
GPIO.setup (led_25, GPIO.OUT)

led_17 = 17
GPIO.setup (led_17, GPIO.OUT)

delit = 6
GPIO.setup (delit, GPIO.IN)

state = 0

while True:
    state = not GPIO.input (delit)
    GPIO.output (led_16, state)
    GPIO.output (led_5, state)
    GPIO.output (led_25, state)
    GPIO.output (led_17, state)
