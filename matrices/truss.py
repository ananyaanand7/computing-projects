import numpy as np
from matrices import solve_linear_system

def main():
    # Unknowns:
    # F1, F3, F2, H2, V2, V3
    unknowns = ["F1", "F3", "F2", "H2", "V2", "V3"]

    # Angles
    cos30 = np.cos(np.radians(30))
    sin30 = np.sin(np.radians(30))
    cos60 = np.cos(np.radians(60))
    sin60 = np.sin(np.radians(60))

    # Matrix A
    A = np.array([
        [-cos30,   cos60,   0,     0,     0,     0],
        [-sin30,  -sin60,   0,     0,     0,     0],
        [ cos30,   0,       1,     1,     0,     0],
        [ sin30,   0,       0,     0,     1,     0],
        [ 0,      -cos60,  -1,     0,     0,     0],
        [ 0,       sin60,   0,     0,     0,     1],
    ])

    b = np.array([
        0,
        1000,
        0,
        0,
        0,
        0
    ])

    solution = solve_linear_system(A, b, unknowns)

    # Output: ONLY lines of form key = value
    for var in unknowns:
        print(f"{var} = {solution[var]:.2f}")

if __name__ == "__main__":
    main()
