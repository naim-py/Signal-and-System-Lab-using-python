import matplotlib.pyplot as plot
import numpy as np

A = 5
f = 100
T = 1 / f
t = np.arange(0, T+T/100, T / 100)
y = A * np.sin(2 * np.pi * f * t)
plot.figure(figsize=(10, 8))
plot.stem(t, y)
plot.xlabel('Time(sec)')
plot.ylabel('Amplitude')
plot.title('Sinusoidal Wave')
plot.show()

