import numpy as np
import matplotlib.pyplot as plt

print("hello world")

test = np.sin(3*np.pi/2)
print(test)

x = np.linspace(0, 2, 100)

plt.plot(x, x*x, label='linear')  # Plot some data on the axes.

plt.show()