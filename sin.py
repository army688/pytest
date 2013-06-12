import numpy as np
from pylab import * 

x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)
savefig('sin.png') 
