import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

bits = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup (bits, GPIO.OUT)
dynamic_range = 3.3



def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print (f"Напряжение за динамическим диапазоном ЦАП (0.00 - {dynamic_range: .2f} B)")
        print ("Устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)

def to_dac (num):
    dac = [int(element) for element in bin(num)[2:].zfill(8)]
    print ("ararar   ",   (dac), "\n\n")
    GPIO.output (bits, dac)
    



try:
    while True:
        try:
            voltage = float (input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            to_dac (number)

        except ValueError:
            print ("Вы ввели не число. Переделайте\n")

finally:
    GPIO.output(bits, 0)
    GPIO.cleanup()
