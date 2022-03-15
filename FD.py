# Finite difference approximations to derivatives
import numpy as np
import matplotlib.pyplot as plt

initial_investigation = False
order_of_accuracy = True

# Define function for f(x) and f'(x)
def f(x):
    return np.arctan(3 * x)

def f_prime(x):
    return 3 / (1 + (3*x)**2)

# Define the forward and central difference routines

def forward_diff(f, dx, x):
    D = (f(x + dx) - f(x))/dx
    return D

def centered_diff(f, dx, x):
    D =(f(x + dx) - f(x -dx))/(dx*2)
    return D


if initial_investigation:

    # Define the points to evaluate the derivative of f
    x0 = np.linspace(-5, 5, 500)

    # Define the different step sizes to use
    step_sizes = [0.04, 0.02, 0.01, 0.005]

    # Define points for plotting and create figure
    x = np.linspace(-5, 5, 500)
    fig, ax = plt.subplots(2, 1, figsize=(8, 8))

    # Plot the error and approximated derivative for the defined step sizes
    for dx in step_sizes:

        
        ax[0].plot(x,centered_diff(f,dx,x0), label =f'dx = {dx}')
        ax[0].set(title = 'Derivative')
        

        ax[1].plot(x,np.abs(f_prime(x)-centered_diff(f,dx,x0)), label =f'dx = {dx}')
        ax[1].set(title = 'Error')

    # plot the actual derivative
    ax[0].plot(x,f_prime(x), label ='Exact')

    ax[0].legend()
    ax[1].legend()

    plt.show()

if order_of_accuracy:
    # Investigate the order of accuracy at the point x0
    x0 = 1 

    # Define the different step sizes to use
    step_sizes = np.logspace(-2,-15, 14, base = 2)


    # Create an empty list to store the error for the centered and forward difference approximations
    err_forward = []
    err_centered = []

    # Compute the error for each stepsize choice and append it to the list err_    

    for dx in step_sizes:
        err_forward.append( np.abs(forward_diff(f, dx, x0)-f_prime(x0)))
        err_centered.append( np.abs(centered_diff(f, dx, x0)-f_prime(x0)))

    # Plot the results
    
    fig, ax =  plt.subplots(1, 1, figsize=(8, 8))
    ax.plot(np.log(step_sizes), np.log(err_forward), 'rx', label = 'forward_diff')
    ax.plot(np.log(step_sizes), np.log(err_centered), 'bx', label = 'centered_diff')
    ax.set(title = 'Error vs dx', xlabel = 'log(dx)', ylabel = 'log(error)')
    ax.legend()
    plt.show()

    # Estimate k by determining the slope of log(error) vs log(dx)

    line_coefs_forward = np.polyfit(np.log(step_sizes), np.log(err_forward),1)
    k_forward = line_coefs_forward[0]
    print(k_forward)

    line_coefs_centered = np.polyfit(np.log(step_sizes), np.log(err_centered),1)
    k_centered = line_coefs_centered[0]
    print(k_centered)