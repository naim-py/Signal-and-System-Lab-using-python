import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 1000)
x = np.cos(2*np.pi*100*t) + np.cos(2*np.pi*500*t)

plt.figure(figsize= (14, 10))
plt.subplot(211)
plt.plot(t, x)
plt.xlabel('time')
# plt.ylabel('frequency')
plt.title('The spectrum of $x$')
plt.subplot(212)
fft = np.fft.fft(x)
mag = np.abs(fft)
mag = mag[:801]
plt.plot(mag)
plt.title("Amplitude of Spectrum")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()