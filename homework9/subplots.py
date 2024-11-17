import numpy as np
import matplotlib.pyplot as plt

def plot_side_by_side(x_range):
    """
    Function creates a plot with two subplots side-by-side.
    The left subplot will plot h(x) = cos x, and the right subplot will plot k(x) = sin(x).

    Inputs:
    Can insert x range start and stop values
    """
    x = np.linspace(x_range[0], x_range[1], 500)

    #creates side-by-side figure
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns
    
    #Left subplot: h(x) = cos(x)
    ax[0].plot(x, np.cos(x), label="y = cos(x)", color='red')
    ax[0].set_title("y = cos(x)", fontsize=14)
    ax[0].set_xlabel("x", fontsize=12)
    ax[0].set_ylabel("y", fontsize=12)
    ax[0].grid(True)
    ax[0].legend()
    
    #Right subplot: k(x) = sin(x)
    ax[1].plot(x, np.sin(x), label="y = sin(x)", color='blue')
    ax[1].set_title("y = sin(x)", fontsize=14)
    ax[1].set_xlabel("x", fontsize=12)
    ax[1].set_ylabel("y", fontsize=12)
    ax[1].grid(True)
    ax[1].legend()
    
    fig.suptitle("Side-by-Side Subplots", fontsize=16)
    plt.show()

def plot_on_top(x_range):
    """
    Function creates a plot with two on top of each other
    The left subplot will plot h(x) = cos x, and the right subplot will plot k(x) = sin(x).

    Inputs:
    Can insert x range start and stop values
    """
    x = np.linspace(x_range[0], x_range[1], 500)
    
    #creates one on top of other figure
    fig, ax = plt.subplots(2, 1, figsize=(8, 12))  #2 rows, 1 column
    
    #Top subplot: h(x) = cos(x)
    ax[0].plot(x, np.cos(x), label="y = cos(x)", color='red')
    ax[0].set_title("y = cos(x)", fontsize=14)
    ax[0].set_xlabel("x", fontsize=12)
    ax[0].set_ylabel("y", fontsize=12)
    ax[0].grid(True)
    ax[0].legend()
    
    #Bottom subplot: k(x) = sin(x)
    ax[1].plot(x, np.sin(x), label="y = sin(x)", color='blue')
    ax[1].set_title("y = sin(x)", fontsize=14)
    ax[1].set_xlabel("x", fontsize=12)
    ax[1].set_ylabel("y", fontsize=12)
    ax[1].grid(True)
    ax[1].legend()
    
    fig.suptitle("Vertical Subplots", fontsize=16)
    plt.show()
