import numpy as np
import matplotlib.pyplot as plt

g = 9.8
u = 20  # initial velocity

angles = [30, 45, 60]

t = np.linspace(0, 5, 200)

plt.figure(figsize=(8,5))

for angle in angles:
    theta = np.radians(angle)

    x = u * np.cos(theta) * t
    y = u * np.sin(theta) * t - 0.5 * g * t**2

    # ground cut-off
    y = np.where(y >= 0, y, np.nan)

    plt.plot(x, y, label=f"{angle}°")

plt.title("Projectile Motion Comparison")
plt.xlabel("Horizontal Distance")
plt.ylabel("Height")
plt.legend()
plt.grid(True)

plt.show()