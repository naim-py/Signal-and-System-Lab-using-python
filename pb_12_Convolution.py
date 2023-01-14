import matplotlib.pyplot as plot
import numpy as np

t = np.arange(0,51)
k = 2
c = -(1/12) + (np.pi)*(0.16666666666j)  # 1/6 = 0.16666666666
y = k*np.exp(c*t)
# print(c,y)
plot.figure(figsize=(12,8))
plot.subplot(4,1,1)
plot.plot(t, np.abs(y))
plot.xlabel(r'$t$')
plot.ylabel(r'$|x(t)|$')
plot.title(r'Absolute value  of  $x(t)=k*e^{c*t}$')

plot.subplot(4,1,2)
plot.plot(t, y.real)
plot.xlabel(r'$t$')
plot.ylabel(r'$|x(t)|$')
plot.title(r'Real part  of  $x(t)=k*e^{c*t}$')

plot.subplot(4,1,3)
plot.plot(t, y.imag )
plot.xlabel(r'$t$')
plot.ylabel(r'$|x(t)|$')
plot.title(r'Imaginary part  of  $x(t)=k*e^{c*t}$')

plot.subplot(4,1,4)
plot.plot(t, np.angle((y)*360/(2*np.pi)))
plot.xlabel(r'$t$')
plot.ylabel(r'$|x(t)|$')
plot.title(r'Phase part  of  $x(t)=k*e^{c*t}$');
plot.tight_layout()
plot.show()