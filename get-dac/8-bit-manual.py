import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

bits = [0, 1, 2, 3, 4, 5, 6, 7]
GPIO.setup (bits, GPIO.OUT)

dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print (f"Напряжение за динамическим диапазоном ЦАП (0ю00 - {dynamic_range: .2f} B)")
        print ("Устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)

def to_bin (num):
    return [int(element) for element in bin(num)[2:].zfill(8)]


try:
    while True:
        try:
            voltage = float (input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            to_bin (number)

        except ValueError:
            print ("Вы ввели не число. Переделайте\n")

finally:
    GPIO.output(bits, 0)
    GPIO.cleanup()
