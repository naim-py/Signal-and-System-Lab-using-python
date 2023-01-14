import numpy as np
import matplotlib.pyplot as plot

def DFT(x):
    N = len(x)
    X = np.zeros((N,),dtype=np.complex128)
    for m in range(0,N):
        for n in range(0,N):
            X[m] += x[n]*np.exp(-np.pi*2j*m*n/N)
    return X

def IDFT(x):
    N = len(x)
    X = np.zeros((N,),dtype=np.complex128)
    for m in range(0,N):
        for n in range(0,N):
            X[m] += x[n]*np.exp(np.pi*2j*m*n/N)
    return X/N

x=[1,2,3,4,5,6,5,4,3,2,1]
sr=100
N=len(x)
n=np.arange(N)
T=N/sr
freq=n/T

X=DFT(x)
plot.figure(figsize=(20,6))

# DFT
plot.subplot(121)
plot.stem(freq,abs(X),'b',markerfmt=" ",basefmt="-b")
plot.ylabel("DFT Amplitude |X(freq)|")
plot.xlabel("Freq(Hz)")
plot.title("Discrete Fourier Transform")

# IDFT
plot.subplot(122)
plot.stem(freq,abs(IDFT(X)),'b',markerfmt=" ",basefmt="-b")
plot.ylabel("IDFT Amplitude |X(freq)|")
plot.xlabel("Freq(Hz)")
plot.title("Inverse Discrete Fourier Transform")
plot.show()

