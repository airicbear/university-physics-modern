import numpy as np
import matplotlib.pyplot as plt

alpha = 2.4
beta = 1.2

rx = lambda t: alpha * t
ry = lambda t: 3.0 - beta * t ** 2

t = np.array([0, 2.0])
ts = np.linspace(0, 2, 100)

rvec = np.array([[0, 0, rx(t[0]), ry(t[0])], [0, 0, rx(t[1]), ry(t[1])]])
rx1, ry1, rx2, ry2 = zip(*rvec)
plt.figure()
ax = plt.gca()
ax.quiver(rx1, ry1, rx2, ry2, angles='xy', scale_units='xy', scale=1, color='g')
ax.set_xlim([-1, 6])
ax.set_ylim([-3, 4])
plt.draw()
plt.plot(rx(ts), ry(ts), linestyle='--')
#plt.scatter([rx2[0], rx2[1]], [ry2[0], ry2[1]])

plt.annotate(r'$t_1$', [rx2[0], ry2[0]])
plt.annotate(r'$t_2$', [rx2[1], ry2[1]])

plt.savefig('3_07_a')
plt.show()

