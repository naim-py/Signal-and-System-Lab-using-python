import numpy as np
import matplotlib.pyplot as plot

x1=[4,3,6,1,4,9]
x2=[4,3,5,1,1,10]
n1=np.arange(-2,4)
n2=np.arange(-1,5)
n=np.arange(min(min(n1),min(n2)),max(max(n1),max(n2))+1)
y1=np.zeros(len(n))
y2=np.zeros(len(n))

li=list(n)
y1[li.index(n1[0]):li.index(n1[0])+len(n1)]=x1
y2[li.index(n2[0]):li.index(n2[0])+len(n2)]=x2

# signal audition
y=y1+y2
plot.figure(figsize=(10,10))
plot.subplot(311)
plot.stem(n,y,basefmt="-b")
plot.title("Signal Addition")
plot.tight_layout()

# normal signal
x=[0,1,2,3,4,5,4,3]
n=np.arange(0,8)
plot.subplot(312)
plot.stem(n,x,basefmt="-b")
plot.title("Signal")
plot.tight_layout()

# folding signal
x.reverse()
n=np.flip(-n)
plot.subplot(313)
plot.stem(n,x,basefmt="-b")
plot.title("Folding Signal")
plot.tight_layout()
plot.show()

