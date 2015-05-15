import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,51,2)
y = np.zeros(len(x))
y[0] = 50
for ind in range(len(y)):
    if ( ind > 0 ):
        y[ind] = y[ind-1]*2
        
f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.plot(x,y,'ro--')
ax1.set_xlabel("Time (years)",fontsize=16)
ax1.set_ylabel("# Transistors on Chip",fontsize=16)
f1.show()

f2 = plt.figure()
ax2 = f2.add_subplot(111)
ax2.set_yscale('log')
ax2.plot(x,y,'ro--')
ax2.set_xlabel("Time (years)",fontsize=16)
ax2.set_ylabel("# Transistors on Chip",fontsize=16)
f2.show()