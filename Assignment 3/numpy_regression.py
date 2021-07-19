from numpy import *
import matplotlib.pyplot as plt
import sys


# Same power as in matrix.py with the difference that this returns an numpy array
def powers(number_list, first, last):
    return array([[i ** j for j in range(first, last + 1)] for i in number_list])


# Computes a general polynomial at x with coefficients a
def poly(a, x):
    y = 0
    for i in range(len(a)):
        y += a[i] * pow(x, i)
    return y


# Loads data and number of degrees from specified arguments
data = loadtxt(sys.argv[1])
n = int(sys.argv[2])

# Save first column in X and second column in Y
X, Y = [], []
for col in range(len(data)):
    X.append(data[col][0])
    Y.append(data[col][1])

# Perform polynomial regression
Xp = powers(X, 0, n)
Yp = powers(Y, 1, 1)
Xpt = Xp.transpose()
a = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))
a = a[:, 0]
X2 = linspace(min(X), max(X), int((max(X) - min(X)) / 0.2)).tolist()
Y2 = [poly(a, X2[i]) for i in range(len(X2))]

# Plot the polynomial regression with the data points
plt.plot(X, Y, 'ro')
plt.plot(X2, Y2)
plt.show()
