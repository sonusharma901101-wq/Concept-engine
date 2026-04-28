import math

def calculate_position(u, theta_rad, t):
    x = u * math.cos(theta_rad) * t
    y = u * math.sin(theta_rad) * t - 0.5 * 9.8 * t**2
    return x, y

def simulate_motion(u, theta):
    theta_rad = math.radians(theta)
    t = 0
    dt = 0.1
    max_y = 0

    print("\n--- Motion Simulation Start ---\n")

    while True:
        x, y = calculate_position(u, theta_rad, t)

        print("t =", round(t,2), "| X =", round(x,2), "| Y =", round(y,2))

        if y > max_y:
            max_y = y

        if y < 0:
            print("\nObject has hit the ground.")
            break

        t += dt

    print("\n--- Final Results ---")
    print("Maximum height:", round(max_y,2))
    print("Range:", round(x,2))


# Main program
u = float(input("Enter initial velocity (u): "))
theta = float(input("Enter angle (degrees): "))

simulate_motion(u, theta)