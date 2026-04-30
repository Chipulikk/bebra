import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, num):
        return[int(elements) for elements in bin(self.num)[2: ].zfill(8)]

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print (f"Напряжение за динамическим диапазоном ЦАП (0.00 - {self.dynamic_range: .2f} B)")
            print ("Устанавливаем 0.0 В")
            return 0

        number =  int(voltage / self.dynamic_range * 255)
        return self.set_number (number)


if __name__ == "__main__":
    try:
        dac = R2R_DAC ([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Перепишите\n")

    finally:
        dac.deinit()
