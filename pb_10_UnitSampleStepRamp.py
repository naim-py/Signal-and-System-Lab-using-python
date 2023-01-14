import numpy as np
import matplotlib.pyplot as plot

n=np.arange(-5,6,1)
x=np.array(n==0,dtype=int)
plot.figure(figsize=(10,8))
plot.subplot(311)
plot.stem(n,x)
plot.title('Unit Sample Sequence')
plot.xlabel('n')
plot.ylabel('x(n)')
plot.tight_layout()

N=5
n=np.arange(-N,N+1,1)
x=np.concatenate((np.zeros(N),np.ones(N+1)))
plot.subplot(312)
plot.stem(n,x)
plot.title('Unit Step Signal')
plot.xlabel('n')
plot.ylabel('x(n)')
plot.tight_layout()

n=np.arange(-5,6,1)
x=np.array(n*(n>=0))
plot.subplot(313)
plot.stem(n,x)
plot.title('Unit Ramp Signal')
plot.xlabel('n')
plot.ylabel('x(n)')
plot.tight_layout()
plot.show()

