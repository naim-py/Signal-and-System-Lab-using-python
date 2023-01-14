import matplotlib.pyplot as plot
import numpy as np

def delta(n):
    r = np.zeros(n.size)
    for i in range(n.size):
        if n[i] == 0:  # n=0 hle output 1 hbe otherwise 0
            r[i] = 1
    return r

n = np.arange(-5, 6)
y = 2*delta(n+2) - delta(n-4)
plot.figure(figsize=(10,8))
plot.stem(n, y,basefmt="-b")
plot.xlabel("--n-->")
plot.ylabel("delta(n)")
plot.show()