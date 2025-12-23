import numpy as np
from matrices import solve_linear_system

# Unknowns: i1, i2, i3, i4, v1, v2, v3, v4, v5, v6
# v1 and v6 are known (150 V and 0 V), but we keep them in system as constraints

# Coefficient matrix A
A = np.array([
    [1, -1, -1,  0, 0, 0, 0, 0, 0, 0],       # i1 - i2 - i3 = 0
    [0,  1,  1, -1, 0, 0, 0, 0, 0, 0],       # i2 + i3 - i4 = 0
    [-10, 0, 0, 0, 1, -1, 0, 0, 0, 0],       # v1 - v2 - 10*i1 = 0
    [0, -20, 0, 0, 0, 1, -1, 0, 0, 0],       # v2 - v3 - 20*i2 = 0
    [0, -2,  0, 0, 0, 0, 1, -1, 0, 0],       # v3 - v4 - 2*i2 = 0
    [0, -5,  0, 0, 0, 0, 0, 1, -1, 0],       # v4 - v5 - 5*i2 = 0
    [0,  0, -5, 0, 0, 1, 0, 0, -1, 0],       # v2 - v5 - 5*i3 = 0
    [0,  0,  0, -25, 0, 0, 0, 0, 1, -1],     # v5 - v6 - 25*i4 = 0
    [0,  0,  0,  0, 1, 0, 0, 0, 0, 0],       # v1 = 150
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 1]        # v6 = 0
], dtype=float)

# Constants vector b
b = np.array([
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    150,
    0
], dtype=float)

# Variable names in order
names = ["i1", "i2", "i3", "i4", "v1", "v2", "v3", "v4", "v5", "v6"]

# Solve the system
solution = solve_linear_system(A, b, names)

# Print solution
for name in names:
    print(f"{name} = {solution[name]:.4f}")
