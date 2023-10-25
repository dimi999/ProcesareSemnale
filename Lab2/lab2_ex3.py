import matplotlib.pyplot as plt
import numpy as np
import scipy
import sounddevice

rate1, x1 = scipy.io.wavfile.read('../lab1/semnal2a.wav')
rate2, x2 = scipy.io.wavfile.read('../lab1/semnal2b.wav')
rate3, x3 = scipy.io.wavfile.read('../lab1/semnal2c.wav')
rate4, x4 = scipy.io.wavfile.read('../lab1/semnal2d.wav')

sounddevice.play(x1, rate1)
sounddevice.wait()
sounddevice.play(x2, rate2)
sounddevice.wait()
sounddevice.play(x3, rate3)
sounddevice.wait()
sounddevice.play(x4, rate4)
sounddevice.wait()
