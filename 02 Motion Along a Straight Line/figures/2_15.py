import numpy as np
import matplotlib.pyplot as plt

x = lambda t: 50.0 + 2.00 * t - 0.0625 * t ** 2
v = lambda t: 2.00 - 0.125 * t
a = lambda t: -0.125 + 0 * t

xp = np.linspace(0, 40, 100)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.plot(xp, x(xp))
plt.plot(xp, v(xp))
plt.plot(xp, a(xp))

plt.xlabel(r'$t$')

plt.savefig('2_15')
plt.show()
