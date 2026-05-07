import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_freq, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.pem_freq = pwm_freq
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

        self.pwm = GPIO.PWM (gpio_pin, pwm_freq)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    """def set_number(self, num):
        dac = [int(elements) for elements in bin(num)[2: ].zfill(8)]
        GPIO.output (self.gpio_pin, dac)
        return dac"""
    

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print (f"Напряжение за динамическим диапазоном ЦАП (0.00 - {self.dynamic_range: .2f} B)")
            print ("Устанавливаем 0.0 В")
            return 0

        duty = 100 * voltage / self.dynamic_range
        print ("Коэффициент заполнения: ", (duty))
        self.pwm.start (duty)
        #print (". Его двоичное представление: ", (self.set_number (number)))


if __name__ == "__main__":
    try:
        dac = PWM_DAC (12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Перепишите\n")

    finally:
        dac.deinit()
