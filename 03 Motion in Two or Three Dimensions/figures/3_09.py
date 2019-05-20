import numpy as np
import matplotlib.pyplot as plt

g = 9.80
v_0x = 1.10
t = [0, 0.480]

x = lambda t: v_0x * t
y = lambda t: -0.5 * g * t ** 2

vx = lambda t: v_0x + t * 0
vy = lambda t: -g * t

ts = np.linspace(t[0], t[1], 1000)
tp = np.linspace(t[0], t[1], 3)

vvec = np.array([[x(i), y(i), vx(i), vy(i)] for i in tp])
vx1, vy1, vx2, vy2 = zip(*vvec)

plt.figure()
axis = plt.gca()

axis.quiver(vx1, vy1, vx2, vy2, angles='xy', scale_units='xy', scale=1, color='b')

axis.set_xlim([0, 1.75])
axis.set_ylim([-6, 0.1])

plt.draw()
plt.plot(x(ts), y(ts), linestyle='--')

plt.savefig('3_09')
plt.show()

