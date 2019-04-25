import numpy as np
import matplotlib.pyplot as plt

alpha = 3.00
beta = 0.100

v = lambda t: alpha + beta * t ** 2
a = lambda t: 2 * beta * t

xp = np.linspace(0, 5.00)

plt.plot(xp, v(xp))
plt.plot(xp, a(xp))

plt.xlabel(r'$t$')

plt.savefig('2_17')
plt.show()

