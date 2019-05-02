import numpy as np
import matplotlib.pyplot as plt

g = -9.80
y0 = 0
v0 = 15.8
ay = 0.379 * g

y = lambda t: y0 + v0 * t + 0.5 * ay * t ** 2
v = lambda t: v0 + ay * t
a = lambda t: (v(t) - v0) / t

t = np.linspace(0.1, 8.5, 100)

plt.plot(t, y(t), label=r'$y$')
plt.plot(t, v(t), dashes=[2, 2, 10, 2], label=r'$v_y$')
plt.plot(t, a(t), dashes=[6, 2], label=r'$a_y$')

fig, ax = plt.subplots()
plt.xlabel(r'$t$')
ax.legend()

plt.savefig('2_39')
plt.show()

