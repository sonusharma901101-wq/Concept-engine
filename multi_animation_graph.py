import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.8
u = 20
angles = [30, 45, 60]

t = np.linspace(0, 5, 200)

fig, ax = plt.subplots()
ax.set_xlim(0, 50)
ax.set_ylim(0, 25)

lines = []
points = []

for _ in angles:
    line, = ax.plot([], [], lw=2)
    point, = ax.plot([], [], 'o')
    lines.append(line)
    points.append(point)

trajectories = []

for angle in angles:
    theta = np.radians(angle)
    x = u*np.cos(theta)*t
    y = u*np.sin(theta)*t - 0.5*g*t**2
    y = np.where(y < 0, 0, y)
    trajectories.append((x, y))

def update(i):
    for idx, (x, y) in enumerate(trajectories):
        lines[idx].set_data(x[:i], y[:i])
        points[idx].set_data([x[i]], [y[i]])
    return lines + points

ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)

plt.title("Multi-Angle Projectile Animation")
plt.show()