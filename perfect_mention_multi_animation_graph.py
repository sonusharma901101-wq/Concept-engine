import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------- Physics ----------------
g = 9.8
u = 20
angles = [30, 45, 60]

t = np.linspace(0, 5, 200)

# ---------------- Figure (dark theme) ----------------
fig, ax = plt.subplots()
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

ax.set_xlim(0, 50)
ax.set_ylim(0, 25)

ax.tick_params(colors="white")
ax.spines[:].set_color("white")
ax.grid(True, linestyle="--", alpha=0.3)

colors = ["cyan", "lime", "red"]

# ---------------- Precompute trajectories ----------------
trajectories = []

for angle in angles:
    theta = np.radians(angle)

    x = u * np.cos(theta) * t
    y = u * np.sin(theta) * t - 0.5 * g * t**2

    y = np.where(y < 0, 0, y)

    trajectories.append((x, y))

# ---------------- Plot objects ----------------
lines = []
points = []

for i, angle in enumerate(angles):
    line, = ax.plot([], [], color=colors[i], linewidth=2, label=f"{angle}°")
    point, = ax.plot([], [], 'o', color=colors[i])
    lines.append(line)
    points.append(point)

ax.legend(facecolor="black", labelcolor="white")

# ---------------- Animation function ----------------
def update(i):
    for j, (x, y) in enumerate(trajectories):

        lines[j].set_data(x[:i], y[:i])
        points[j].set_data([x[i]], [y[i]])

    return lines + points

# ---------------- Run animation ----------------
ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)

plt.title("Projectile Motion - Multi Angle Simulation", color="white")
plt.show()