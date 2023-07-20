import numpy as np
import matplotlib.pyplot as plt
size=512

funcX=np.arange(size)
funcY=np.power(np.sin(np.pi/size*funcX),2)

plt.plot(funcX,funcY)
plt.show()