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

def lorenz(x, y, z, sigma, r, b):
    x_prime = sigma * (y - x)  # x' = sigma * (y-x); calculates x'
    y_prime = r * x - y - x * z  # y' = r*x - y -x*z; calculates y'
    z_prime = x * y - b * z  # z' = x*y - b*z; calculates z'
    return x_prime, y_prime, z_prime  # Returns x', y', and z'


# Parameters: r
# Output: Plots Lorenz [x,y,z], x(t), y(t), and z(t)
def main(r, s, b):
    # Initial Conditions
    # Set sigma = s (10)default
    # Set beta = b (8/3)default

    dt = 0.01  # Step size
    num_iterations = 10000  # Define number of iterations

    xs = np.empty(num_iterations + 1)  # Create empty np.array for x
    ys = np.empty(num_iterations + 1)  # Create empty np.array for y
    zs = np.empty(num_iterations + 1)  # Create empty np.array for z

    # Initial Values
    xs[0] = 10  # Speed/Efficiency of process
    ys[0] = 8  # Operations/time
    zs[0] = 1  # Error messages/time

    for i in range(num_iterations):  # Iterates number of desired iterations over 'time'
        x_prime, y_prime, z_prime = lorenz(xs[i], ys[i], zs[i], s, r, b)  # Call Lorenz
        xs[i + 1] = xs[i] + (x_prime * dt)  # Estimate next x-value using x_prime [partial derivative]
        ys[i + 1] = ys[i] + (y_prime * dt)  # Estimate next y-value using y_prime [partial derivative]
        zs[i + 1] = zs[i] + (z_prime * dt)  # Estimate next z-value using z_prime [partial derivative]

    # Plot Lorenz
    fig = plt.figure()  # Set fig equal to a figure
    ax = fig.add_subplot(projection='3d')

    ax.plot(xs, ys, zs, lw=0.5)  # Plot x, y, and z with line width 0.5
    ax.set_xlabel("x-axis")  # Sets x label
    ax.set_ylabel("y-axis")  # Sets y label
    ax.set_zlabel("z-axis")  # Sets z label
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


prompt1 = "Enter a value for rho. (1, 10, 28) default.\nThis value represents the complexity of a process.\n"
rho = input(prompt1)
prompt2 = "Enter a value for sigma. (10) default.\nThis value would represent the throughput of a process.\n"
sig = input(prompt2)
prompt3 = "Enter a value for beta. (8/3) default.\nThis value would represent how important the failed operation is to other parts of the process\n"
bta = input(prompt3)

# Run Lorenz on different values of Rho --> 1, 10, 28
main(float(rho), float(sig), float(bta))  # Run Lorenz simulation with inputs
