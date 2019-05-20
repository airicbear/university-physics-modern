import numpy as np
import matplotlib.pyplot as plt

g = 9.80
v_0 = 30
alpha = np.deg2rad(33)
t = [0, 4.1]

x = lambda t: v_0 * np.cos(alpha) * t
y = lambda t: v_0 * np.sin(alpha) * t -0.5 * g * t ** 2 + 15

vx = lambda t: v_0 * np.cos(alpha) + (0 * t)
vy = lambda t: v_0 * np.sin(alpha) - (g * t)

ts = np.linspace(t[0], t[1], 1000)
tp = np.linspace(t[0], t[1], 6)

vvec = np.array([[x(i), y(i), vx(i), vy(i)] for i in tp])
vx1, vy1, vx2, vy2 = zip(*vvec)

plt.figure()
axis = plt.gca()

axis.quiver(vx1, vy1, vx2, vy2, angles='xy', scale_units='xy', scale=1)

axis.set_xlim([0, 135])
axis.set_ylim([-25, 35])

plt.draw()
plt.plot(x(ts), y(ts), linestyle='--')
plt.plot(np.linspace(0,140,2), np.linspace(0,0,2))

plt.xlabel('x')
plt.ylabel('y')

plt.savefig('3_21')
plt.show()

