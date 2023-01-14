# from IPython.core.display import Markdown
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(4, figsize= (20, 20))

f = 10
T = 1/f
t = np.arange(0, 2*T, T/50)
A = 10
y = A*np.sin(2*np.pi*f*t)

#figure 1
plt.tight_layout()
ax[0].plot(t,y)
ax[0].set_xlabel('Time(sec)')
ax[0].set_ylabel('Amplitude (volt)')
ax[0].set_title('Transmitting Singnals')

# sampling
A = 500
# Ts = T / 20
# Fs = 1 / Ts
Fs=500
Ts=1/Fs
n = np.arange(0, len(y))
y1 = A*np.sin(2*np.pi*f*n*Ts)

#figure 2
plt.tight_layout()
ax[1].stem(n,y1)
ax[1].set_xlabel('Discrete time(sec)')
ax[1].set_ylabel('Amplitude (volt)')
ax[1].set_title('Discrete Time signal after sampling')

y1 = A + y1
#figure 3
plt.tight_layout()
ax[2].stem(n,y1)
ax[2].set_xlabel('Discrete time(sec)')
ax[2].set_ylabel('Amplitude (volt)')
ax[2].set_title('De level + Discrete time Signals')

# Quantization
y1 = np.round(y1)
#figure 4
plt.tight_layout()
ax[3].stem(n,y1)
ax[3].set_xlabel('Discrete time(sec)')
ax[3].set_ylabel('Amplitude (volt)')
ax[3].set_title('Quantization Signals')
plt.show()

y1 = np.array(y1, dtype= int)
n = np.max(y1)
n = np.ceil(np.log2(n))
n = int(n)
print("Coding:")
for e in y1:
    print(f'{e:0{n}b}')

