#Zach Pedersen, Rylan Casanova
#This is our work!
#Prof Citro
#CST-305

# Imports
import numpy as np
import matplotlib.pyplot as plt
import time
# Registers 3D projection [unused otherwise]
from mpl_toolkits.mplot3d import Axes3D

# Define lorenz function
# Perform lorenz calculations
def lorenz(x, y, z, sigma, r, b):
    x_prime = sigma * (y - x)
    y_prime = r * x - y - x * z
    z_prime = x * y - b * z
    return x_prime, y_prime, z_prime


# Parameters: r
# Output: Plots Lorenz [x,y,z], x(t), y(t), and z(t)
# Create empty arrays for x, y and z
def main(r, s, b):
    dt = 0.01  # Step size
    num_iterations = 10000
    xs = np.empty(num_iterations + 1)
    ys = np.empty(num_iterations + 1)
    zs = np.empty(num_iterations + 1)

    # Initial Values
    xs[0] = 10
    ys[0] = 8
    zs[0] = 1

    # Iterates number of desired iterations over 'time'
    for i in range(num_iterations):
        x_prime, y_prime, z_prime = lorenz(xs[i], ys[i], zs[i], s, r, b)
        xs[i + 1] = xs[i] + (x_prime * dt)
        ys[i + 1] = ys[i] + (y_prime * dt)
        zs[i + 1] = zs[i] + (z_prime * dt)

    # Plot Lorenz
    # Set fig equal to a figure
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Plot x, y, and z with line width 0.5
    # Set labels
    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_zlabel("z-axis")
    ax.set_title("Lorenz")

    plt.show()  # Show Lorenz plot

    ts = np.linspace(0, 100.01, 10001)  # Set array for time based on dt step size
    plt.title("x(t) [Speed] - r: " + str(r))  # Set title for x(t) plot based on r
    plt.xlabel("t - Time")  # Sets x label - time
    plt.ylabel("x - Speed")  # Sets y label - x
    plt.plot(ts, xs)  # Plots x(t)
    plt.show()  # Show plot
    plt.title("y(t) [Operations] - r: " + str(r))  # Set title for y(t) plot based on r
    plt.xlabel("t - Time")  # Sets x label - time
    plt.ylabel("y - Operations")  # Sets y label - y
    plt.plot(ts, ys)  # Plots y(t)
    plt.show()  # Show plot
    plt.title("z(t) [Errors] - r: " + str(r))  # Set title for z(t) plot based on r
    plt.xlabel("t")  # Sets x label - y
    plt.ylabel("z - Errors")  # Sets y label - z
    plt.plot(ts, zs)  # Plot z(t)
    plt.show()  # Show plot

    show = 0
    while int(show) >= 0:
        p = "Enter an integer t to search (0 - {}).\nInput -1 to quit.\n".format(num_iterations)
        show = input(p)
        if int(show) >= 0:
            print("x(t) Speed: t", show, " = ", xs[int(show)])
            print("y(t) Operations: t", show, " = ", ys[int(show)])
            print("z(t) Errors: t", show, " = ", zs[int(show)])


# Prompt user to enter value and displays default values
# Default is 28, 10, and 2.66 in that order
prompt1 = "Enter a value for rho. (1, 10, 28) default.\nThis value represents the complexity of a process.\n"
rho = input(prompt1)
prompt2 = "Enter a value for sigma. (10) default.\nThis value would represent the throughput of a process.\n"
sig = input(prompt2)
prompt3 = "Enter a value for beta. (8/3) default.\nThis value would represent how important the failed operation is to other parts of the process\n"
bta = input(prompt3)

# Run Lorenz on different values of Rho --> 1, 10, 28
# Run Lorenz simulation with inputs
main(float(rho), float(sig), float(bta))
