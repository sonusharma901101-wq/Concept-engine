import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ---------------- PHYSICS ----------------
g = 9.8

t = np.linspace(0, 5, 300)

# ---------------- INITIAL VALUES ----------------
init_angle = 45
init_u = 20

# ---------------- FIGURE ----------------
plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(8,5))
plt.subplots_adjust(bottom=0.25)

ax.set_xlim(0, 60)
ax.set_ylim(0, 30)

ax.set_title("Real-Time Projectile Simulation Engine")
ax.set_xlabel("Distance")
ax.set_ylabel("Height")

line, = ax.plot([], [], color="cyan", linewidth=2)

# ---------------- UPDATE FUNCTION ----------------
def compute(angle, u):
    theta = np.radians(angle)

    x = u * np.cos(theta) * t
    y = u * np.sin(theta) * t - 0.5 * g * t**2

    y = np.where(y < 0, 0, y)

    return x, y

x, y = compute(init_angle, init_u)
line.set_data(x, y)

# ---------------- SLIDERS ----------------
ax_angle = plt.axes([0.2, 0.1, 0.65, 0.03])
ax_speed = plt.axes([0.2, 0.05, 0.65, 0.03])

angle_slider = Slider(ax_angle, "Angle", 1, 89, valinit=init_angle)
speed_slider = Slider(ax_speed, "Speed", 5, 50, valinit=init_u)

# ---------------- LIVE UPDATE ----------------
def update(val):
    angle = angle_slider.val
    u = speed_slider.val

    x, y = compute(angle, u)

    line.set_xdata(x)
    line.set_ydata(y)

    fig.canvas.draw_idle()

angle_slider.on_changed(update)
speed_slider.on_changed(update)

plt.show()