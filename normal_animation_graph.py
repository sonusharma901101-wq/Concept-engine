import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.8
u = 20
angle = 45

theta = np.radians(angle)

t = np.linspace(0, 5, 200)

x = u * np.cos(theta) * t
y = u * np.sin(theta) * t - 0.5 * g * t**2

# ground cut
y = np.where(y < 0, 0, y)

fig, ax = plt.subplots()

ax.set_xlim(0, max(x))
ax.set_ylim(0, max(y) + 2)

line, = ax.plot([], [], lw=2)
point, = ax.plot([], [], 'ro')

def update(i):
    line.set_data(x[:i], y[:i])
    point.set_data([x[i]], [y[i]])  # IMPORTANT FIX
    return line, point

ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)

plt.title("Projectile Animation (Stable)")
plt.show()