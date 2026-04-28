import math

# Inputs
u = float(input("Enter initial velocity (u): "))
theta = float(input("Enter angle (degrees): "))
t = float(input("Enter time: "))

# Convert angle to radians
theta_rad = math.radians(theta)

# Calculate position
x = u * math.cos(theta_rad) * t
y = u * math.sin(theta_rad) * t - 0.5 * 9.8 * t**2

# Output
print(" After", t,  "seconds:")
print("Horizontal distance  (X) :", x)
print("Vertical height(Y):",  y)
if y < 0:
    print("Object has already hit the ground.")
else:
    print("Object is still in air.")