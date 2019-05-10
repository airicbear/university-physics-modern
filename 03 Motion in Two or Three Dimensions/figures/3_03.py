import numpy as np
import matplotlib.pyplot as plt

rx = lambda t: (4.0 + (2.5) * t ** 2)
ry = lambda t: 5.0 * t

vx = lambda t: 5.0 * t
vy = lambda t: 5.0 + t * 0

x = np.linspace(0, 5, 100)

rvec = np.array([[0, 0, rx(0), ry(0)], [0, 0, rx(2), ry(2)]])
vvec = np.array([[rx(0), ry(0), vx(0), vy(0)], [rx(2), ry(2), vx(2), vy(2)]])
rX, rY, rZ, rV = zip(*rvec)
vX, vY, vZ, vV = zip(*vvec)
plt.figure()
ax = plt.gca()
ax.quiver(rX, rY, rZ, rV, angles='xy', scale_units='xy', scale=1, color='b')
ax.quiver(vX, vY, vZ, vV, angles='xy', scale_units='xy', scale=1, color='g')
ax.set_xlim([-1, 30])
ax.set_ylim([-1, 20])
plt.draw()
plt.plot(rx(x), ry(x), linestyle='--', lw=2)
plt.scatter([rx(0), rx(2)], [ry(0), ry(2)], color='black')

for vec in rvec:
    plt.annotate(r'$\vec r\langle{}, {}\rangle$'.format(vec[2], vec[3]), [vec[2], vec[3]])

for i in range(0, len(vvec)):
    plt.annotate(r'$\vec v\langle{}, {}\rangle$'.format(vvec[i][2], vvec[i][3]), [rvec[i][2] + vvec[i][2], rvec[i][3] + vvec[i][3]])

plt.savefig('3_03')
plt.show()

