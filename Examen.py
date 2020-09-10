import sys

sys.path.insert(1,"dsp-modulo")

from thinkdsp import SinSignal
from thinkdsp import decorate

from thinkdsp import read_wave
from thinkdsp import play_wave

import matplotlib.pyplot as plt

frecuencia1 = SinSignal(freq=697, amp=1, offset=0)
frecuencia11 = SinSignal(freq=1209, amp=1, offset=0)

wave_frecuencia1 = frecuencia1.make_wave(duration=0.5, start=0, framerate=44100)
wave_frecuencia11 = frecuencia11.make_wave(duration=0.5, start=0, framerate=44100)

wave_sonido1 = wave_frecuencia1 + wave_frecuencia11

frecuencia5 = SinSignal(freq=770, amp=1, offset=0)
frecuencia51 = SinSignal(freq=1336, amp=1, offset=0)

wave_frecuencia5 = frecuencia5.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_frecuencia51 = frecuencia51.make_wave(duration=0.5, start=0.5, framerate=44100)

wave_sonido2 = wave_frecuencia5 + wave_frecuencia51


frecuencia3 = SinSignal(freq=697, amp=1, offset=0)
frecuencia31 = SinSignal(freq=1477, amp=1, offset=0)

wave_frecuencia3 = frecuencia3.make_wave(duration=0.5, start=1, framerate=44100)
wave_frecuencia31 = frecuencia31.make_wave(duration=0.5, start=1, framerate=44100)

wave_sonido3 = wave_frecuencia3 + wave_frecuencia31

frecuencia7 = SinSignal(freq=852, amp=1, offset=0)
frecuencia71 = SinSignal(freq=1209, amp=1, offset=0)

wave_frecuencia7 = frecuencia7.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_frecuencia71 = frecuencia71.make_wave(duration=0.5, start=1.5, framerate=44100)

wave_sonido4 = wave_frecuencia7 + wave_frecuencia71

wave_suma = wave_sonido1 + wave_sonido2 + wave_sonido3 +wave_sonido4

wave_suma.write("output.wav")