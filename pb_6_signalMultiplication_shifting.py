import numpy as np
import matplotlib.pyplot as plot

x1=[0,1,2,3,4]
x2=[2,2,2,2,2]
n1=np.arange(0,5)
n2=np.arange(-2,3)
n=np.arange(min(min(n1),min(n2)),max(max(n1),max(n2))+1)
y1=np.zeros(len(n))
y2=np.zeros(len(n))

li=list(n)
y1[li.index(n1[0]):li.index(n1[0])+len(n1)]=x1
y2[li.index(n2[0]):li.index(n2[0])+len(n2)]=x2

# Signal Multiplication
y=y1*y2
plot.figure(figsize=(14,8))
plot.subplot(311)
plot.stem(n,y)
plot.title('Signal Multiplication')
plot.xlabel('n')
plot.ylabel('x(n)')
plot.tight_layout()

# signal shifting
n = np.arange(0,9)
x = [0,1,5,2,1,3,6,4,5]
plot.subplot(312)
plot.stem(n,x);
plot.title('x(n) signal')
plot.xlabel('n')
plot.ylabel('x(n)')
plot.tight_layout()

plot.subplot(313)
plot.stem(n + 2, x, 'b', markerfmt= 'bo', basefmt= 'r')
plot.title('x(n-2) signal')
plot.xlabel('n')
plot.ylabel('x(n-2)')
plot.xticks(np.arange(len(n)+2))
plot.plot([0, 1, 2], [0, 0, 0], color= 'red')
plot.tight_layout()
plot.show()


