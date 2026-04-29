import math
import matplotlib.pyplot as plt

u = 10
theta = 30

theta_rad = math.radians(theta)

t = 0
dt = 0.01

x_vals = [ ]
y_vals = [ ]

while True:
    x = u * math.cos(theta_rad) * t
    y = u * math.sin(theta_rad) * t - 0.5 * 9.8 * t**2

    if y < 0:
        break

    x_vals.append(x)
    y_vals.append(y)

    t += dt

# Plot graph
plt.plot(x_vals, y_vals)
plt.xlabel("X (Distance)")
plt.ylabel("Y (Height)")
plt.title("Projectile Motion Trajectory")

plt.show()