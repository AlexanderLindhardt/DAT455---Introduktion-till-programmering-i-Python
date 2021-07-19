from matrix import *
import matplotlib.pyplot as plt
import sys

# Load data from file specified in arguments
data = loadtxt(sys.argv[1])

# Save first column in X and second column in Y
X, Y = [], []
for col in range(len(data)):
    X.append(data[col][0])
    Y.append(data[col][1])

# Perform linear regression
Xp = powers(X, 0, 1)
Yp = powers(Y, 1, 1)
Xpt = transpose(Xp)
[[b], [m]] = matmul(invert(matmul(Xpt, Xp)), matmul(Xpt, Yp))
Y2 = [b + m * X[i] for i in range(len(X))]

# Plot the line with the data points
plt.plot(X, Y, 'ro')
plt.plot(X, Y2)
plt.show()
