import r2r_dac as r2r
import signal_generator as sg
import time

amp = 3.2
sig_freq = 10
samp_freq = 1000

pins = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.3

try:
    dac = r2r.R2R_DAC (pins, dynamic_range, verbose = False)
    t = 0.0
    vals = input ("Введите Амплитуда, частоту считывания и Частоту сигнала через прбел: ").split()
    amp = float(vals[0])
    sig_freq = float(vals[1])
    samp_freq = int(vals[2])

    while True:
        norm_value = sg.get_sin_wave_amplitude (sig_freq, t)
        voltage = norm_value * amp
        dac.r2r.set_voltage(voltage)
        sg.wait_for_sampling_period (samp_freq)

except ValueError:
    print("Вы ввели не число. Перепишите\n")



