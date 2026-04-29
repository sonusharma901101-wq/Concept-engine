import numpy as np
import matplotlib.pyplot as plt
g = 9.8
u = 20
angles = [30, 45, 60]
t = np.linspace(0, 5, 300)
plt.figure()

for angle in angles:
    theta = np.radians(angle)

    vx = u * np.cos(theta)
    vy = u * np.sin(theta)

    x = []
    y = []

    for ti in t:
        x_t = vx * ti
        y_t = vy * ti - 0.5 * g * ti**2

        if y_t < 0:
            break

        x.append(x_t)
        y.append(y_t)

    plt.plot(x, y, label=f"{angle}°")

plt.legend()
plt.grid()
plt.show()
print("45° gives best range in ideal case.")
import numpy as np

g = 9.8
u = 20

angles = np.arange(1, 90)

ranges = []

for angle in angles:
    theta = np.radians(angle)
    R = (u**2 * np.sin(2 * theta)) / g
    ranges.append(R)

best_angle = angles[np.argmax(ranges)]
best_range = max(ranges)

print("Best angle for maximum range:", best_angle)
print("Maximum range:", best_range)
import matplotlib.pyplot as plt

plt.plot(angles, ranges)
plt.title("Angle vs Range")
plt.xlabel("Angle (degrees)")
plt.ylabel("Range")
plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

g = 9.8
u = 20
angles = [30, 45, 60]

t = np.linspace(0, 5, 300)

plt.figure(figsize=(8,5))

for angle in angles:
    theta = np.radians(angle)

    x = u * np.cos(theta) * t
    y = u * np.sin(theta) * t - 0.5 * g * t**2

    # stop below ground
    y = np.where(y >= 0, y, np.nan)

    plt.plot(x, y, label=f"{angle}°")

plt.title("Projectile Motion Comparison (Corrected)")
plt.xlabel("Distance (x)")
plt.ylabel("Height (y)")
plt.legend()
plt.grid()

plt.ylim(bottom=0)   # IMPORTANT FIX
plt.show()