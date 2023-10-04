import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Gradient Descent function for Multiple Linear Regression
def gradient_descent(X, y, learning_rate=0.01, epochs=1000):
    m = len(y)  # Number of training examples
    theta = np.zeros(X.shape[1])  # Initialize coefficients
    bias = 0.0  # Initialize intercept term
    
    for _ in range(epochs):
        predictions = np.dot(X, theta) + bias
        residuals = y - predictions
        
        # Gradient computation
        gradient_theta = (-2/m) * np.dot(X.T, residuals)
        gradient_bias = (-2/m) * np.sum(residuals)
        
        # Update coefficients and intercept
        theta -= learning_rate * gradient_theta
        bias -= learning_rate * gradient_bias

    return theta, bias

# Load the Boston housing dataset
data = pd.read_csv('boston.csv')

# Select features for linear regression
X = data[['AGE', 'TAX']].values
y = data['MEDV'].values

# Standardize features for better convergence
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Compute coefficients and bias using gradient descent
theta, bias = gradient_descent(X, y)

# Predict using the learned model
predictions = np.dot(X, theta) + bias

# Compute the mean squared error (MSE)
mse = np.mean((y - predictions) ** 2)

print(f"Mean Squared Error: {mse:.2f}")
