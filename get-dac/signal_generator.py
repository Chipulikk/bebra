import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    return (np.sin(2 * np.pi * freq * time) + 1) / 2

def wait_for_sampling_period (sampling_frequency, start_time = None):
    if start_time is None:
        start_time = time.time()
    
    period = 1.0 / sampling_freq
    done = time.time() - start_time

    if done < period:
        time.sleep (period - done)


    