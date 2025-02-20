import numpy as np

x = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])



theta_0 = -3
theta_1 = 2
for num in len(x):
    return theta_0 + theta_1*x[num]