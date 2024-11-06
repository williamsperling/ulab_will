# File: even_sum.py
import numpy as np

def sum_even_numbers(numbers):
    """
    Returns the sum of all even numbers in a given list or array
    Inputs: 
    Outputs:
    
    """
    
    sum = np.sum(num for num in numbers if num % 2 == 0) #condition not a variable
    return sum