# Help with this plot would be greatly appreciated.

import numpy as np
import matplotlib.pyplot as plt

# Define upward constants
t0 = 0
y0 = 0
v0 = 0
ay0 = 2.25

# Define downward constants
t1 = 21.6
y1 = 525
v1 = 48.6
ay1 = -9.80

t2 = 26.56
y2 = 646
v2 = 0
ay2 = -9.80

t3 = 38
y3 = 0
v3 = 112
ay3 = -9.80

# These values were supposed to work for downwards y motion
y4 = -3051.4
v4 = 272.72
ay4 = -9.80

# Define time
t = np.linspace(t0 + 0.0001, t1, 1000)

# Define general motion
y = lambda t, y0, v0, ay: y0 + v0 * t + 0.5 * ay * t ** 2
v = lambda t, v0, ay: v0 + ay * t
a = lambda t, vy, v0: (vy - v0) / t

# Define upward motion
y_up = lambda t: y(t, y0, v0, ay0)
v_up = lambda t: v(t, v0, ay0)
a_up = lambda t: a(t, v_up(t), v0)

# Define downward motion
y_down = lambda t: y(t, y4, v4, ay4)
v_down = lambda t: v(t, v4, ay4)
a_down = lambda t: a(t, v_down(t), v4)

# Plot points
pt_t = np.array([t0, t1, t2, t3])
pt_y = np.array([y0, y1, y2, y3])

plt.scatter(pt_t, pt_y)

# Plot upward motion
plt.plot(t, y_up(t), label=r'$y$')
plt.plot(t, v_up(t), dashes=[2, 2, 10, 2], label=r'$v_y$')
plt.plot(t, a_up(t), dashes=[6, 2], label=r'$a_y$')

# Plot downward motion
t += t1
# TODO: Fix downwards y motion
# plt.plot(t, y_down(t), label=r'$y$')
plt.plot(t, v_down(t), dashes=[2, 2, 10, 2], label=r'$v_y$')
plt.plot(t, a_down(t), dashes=[6, 2], label=r'$a_y$')

plt.xlabel(r'$t$')
plt.xlim(0, 40)
plt.ylim(-100, 800)

plt.savefig('2_43')
plt.show()

