import numpy as np
from matplotlib import pyplot as plot

plot.subplots_adjust(hspace=0.5)
f = np.arange(-2, 2, 0.01)
x = np.array(4 * np.sinc(4 * np.pi * f))
plot.figure(figsize=(10, 8))

# real part
plot.subplot(311)
plot.stem(f, np.real(x), markerfmt='-r')
plot.title('Real Part')
plot.xlabel('f-->')
plot.tight_layout()

# magnitude part
plot.subplot(312)
plot.stem(f, np.abs(x), markerfmt='-r')
plot.title('Magnitude Part')
plot.xlabel('f-->')
plot.tight_layout()

# Phase part
plot.subplot(313)
plot.stem(f, np.angle(x), markerfmt='-r')
plot.title('Phase Part')
plot.xlabel('f-->')
plot.tight_layout()
plot.show()

