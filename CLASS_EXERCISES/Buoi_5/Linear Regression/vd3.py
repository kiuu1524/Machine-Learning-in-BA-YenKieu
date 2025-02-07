import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# area
x = np.array([[73.5, 75., 76.5, 79., 81.5, 82.5, 84., 85., 86.5, 87.5, 89., 90., 91.5]]).T

# price
y = np.array([[1.49, 1.50, 1.51, 1.54, 1.58, 1.59, 1.60, 1.62, 1.63, 1.64, 1.66, 1.67, 1.68]]).T

# input matrix X
X = np.concatenate([x], axis=1)

def calculateb1b0(x, y):
    # Compute means
    xbar = np.mean(x)
    ybar = np.mean(y)
    x2bar = np.mean(x ** 2)
    xybar = np.mean(x * y)

    # Compute b0 and b1
    b1 = (xbar * ybar - xybar) / (xbar ** 2 - x2bar)
    b0 = ybar - b1 * xbar

    return b1, b0
