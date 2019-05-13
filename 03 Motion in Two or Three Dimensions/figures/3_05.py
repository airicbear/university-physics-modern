import numpy as np
import matplotlib.pyplot as plt

vvec = np.array([[0, 0, 90, 110], [0, 0, -170, 40]])
vx1, vy1, vx2, vy2 = zip(*vvec)
plt.figure()
ax = plt.gca()
ax.quiver(vx1, vy1, vx2, vy2, angles='xy', scale_units='xy', scale=1, color='g')
ax.set_xlim([-200, 120])
ax.set_ylim([-1, 130])
plt.draw()
plt.scatter([vx2[0], vy2[0]], [vx2[1], vx2[1]], color='black')

plt.annotate(r'$t_1$', [vx2[0], vy2[0]])
plt.annotate(r'$t_2$', [vx2[1], vy2[1]])

plt.savefig('3_05')
plt.show()

