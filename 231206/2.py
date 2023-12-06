## 실습 7
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1,10)
y = 3*x

plt.plot(x,y)
plt.show()

## 실습 8
x = np.arange(1,10)
y = 3*x

y2 = 5*np.sin(x)+5

plt.plot(x,y,'r-', label = 'linear')
plt.plot(x,y2,'g--', label = 'sine')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('matplotlib example')
plt.legend(loc='best')

plt.xlim(0,10)
plt.ylim(0,30)
plt.show()

