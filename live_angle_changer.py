import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ---------------- PHYSICS ----------------
g = 9.8
u = 20

t = np.linspace(0, 5, 300)

# ---------------- FIGURE ----------------
plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(8,5))
plt.subplots_adjust(bottom=0.25)

angle0 = 45

theta = np.radians(angle0)
x = u * np.cos(theta) * t
y = u * np.sin(theta) * t - 0.5 * g * t**2
y = np.where(y < 0, 0, y)

(line,) = ax.plot(x, y, color="cyan", linewidth=2)

ax.set_xlim(0, 50)
ax.set_ylim(0, 30)

ax.set_title("Projectile Motion – Live Angle Control")
ax.set_xlabel("Distance")
ax.set_ylabel("Height")

# ---------------- SLIDER ----------------
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
angle_slider = Slider(ax_slider, "Angle", 1, 89, valinit=angle0)

# ---------------- UPDATE FUNCTION ----------------
def update(val):
    angle = angle_slider.val
    theta = np.radians(angle)

    x = u * np.cos(theta) * t
    y = u * np.sin(theta) * t - 0.5 * g * t**2
    y = np.where(y < 0, 0, y)

    line.set_xdata(x)
    line.set_ydata(y)

    fig.canvas.draw_idle()

angle_slider.on_changed(update)

plt.show()