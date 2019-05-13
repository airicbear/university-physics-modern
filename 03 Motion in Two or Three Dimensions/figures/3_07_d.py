import numpy as np
import matplotlib.pyplot as plt

# Declare functions and variables
alpha = 2.4
beta = 1.2

rx = lambda t: alpha * t
ry = lambda t: 3.0 - beta * t ** 2

vx = lambda t: alpha + t * 0
vy = lambda t: -2 * beta * t

ax = lambda t: t * 0
ay = lambda t: -2 * beta + t * 0

t = np.array([0, 2.0])
ts = np.linspace(0, 2, 100)

rvec = np.array([[0, 0, rx(t[0]), ry(t[0])], [0, 0, rx(t[1]), ry(t[1])]])
rx1, ry1, rx2, ry2 = zip(*rvec)

vvec = np.array([[rx(t[0]), ry(t[0]), vx(t[0]), vy(t[0])], [rx(t[1]), ry(t[1]), vx(t[1]), vy(t[1])]])
vx1, vy1, vx2, vy2 = zip(*vvec)

avec = np.array([[rx(t[1]), ry(t[1]), ax(t[1]), ay(t[1])]])
ax1, ay1, ax2, ay2 = zip(*avec)

# Plot velocity and acceleration
plt.figure()
axis = plt.gca()

axis.quiver(rx1, ry1, rx2, ry2, angles='xy', scale_units='xy', scale=1, color='g')
axis.quiver(vx1, vy1, vx2, vy2, angles='xy', scale_units='xy', scale=1, color='b')
axis.quiver(ax1, ay1, ax2, ay2, angles='xy', scale_units='xy', scale=1, color='r')

axis.set_xlim([-1, 8])
axis.set_ylim([-8, 4])
plt.draw()
plt.plot(rx(ts), ry(ts), linestyle='--')
plt.scatter([rx2[0], rx2[1]], [ry2[0], ry2[1]])

plt.annotate(r'$t_1$', [rx2[0], ry2[0]])
plt.annotate(r'$t_2$', [rx2[1], ry2[1]])
plt.annotate(r'$v_t$', [rx(t[1]) + vx(t[1]), ry(t[1]) + vy(t[1])])
plt.annotate(r'$a_t$', [rx(t[1]) + ax(t[1]), ry(t[1]) + ay(t[1])])

plt.savefig('3_07_d.png')
plt.show()

