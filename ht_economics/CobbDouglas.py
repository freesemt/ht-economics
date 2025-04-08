"""
CobbDouglas.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

class CobbDouglas:
    """
    A class to represent a Cobb-Douglas production function.
    
    Attributes:
    alpha (float): The output elasticity of the first input.
    beta (float): The output elasticity of the second input.
    gamma (float): The output elasticity of the third input.
    """
    
    def __init__(self, alpha, beta, gamma):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
    
    def production(self, x1, x2):
        """
        Calculate the output of the Cobb-Douglas production function.
        
        Parameters:
        x1 (float): The quantity of the first input.
        x2 (float): The quantity of the second input.
        
        Returns:
        float: The output based on the Cobb-Douglas function.
        """
        return self.alpha * (x1 ** self.beta) * (x2 ** self.gamma)

def estimate_cobb_douglas_params(data):
    """
    Estimate the parameters of the Cobb-Douglas production function using nonlinear least squares.
    
    Parameters:
    data (array-like): A 2D array where each row is a sample and columns are inputs and output.
    
    Returns:
    tuple: Estimated parameters (alpha, beta, gamma).
    """
    # Define the Cobb-Douglas function
    def cobb_douglas(params, x1, x2):
        return params[0] * (x1 ** params[1]) * (x2 ** params[2])
    
    # Define the objective function to minimize
    def objective(params):
        x1 = data[:, 0]
        x2 = data[:, 1]
        y = data[:, 2]
        return np.sum((y - cobb_douglas(params, x1, x2)) ** 2)
    
    # Initial guess for parameters
    initial_guess = [1.0, 0.5, 0.5]
    
    # Minimize the objective function
    result = minimize(objective, initial_guess, method='L-BFGS-B')
    
    return result.x
