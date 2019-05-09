import numpy as np
import matplotlib.pyplot as plt

soa = np.array([[0, 0, 4, 0], [4, 0, 14, 10], [0, 0, 18, 10]])
X, Y, U, V = zip(*soa)
plt.figure()
ax = plt.gca()
ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color=['r','b','black'])
ax.set_xlim([-1, 20])
ax.set_ylim([-1, 20])
plt.draw()

plt.savefig('3_03')
plt.show()

