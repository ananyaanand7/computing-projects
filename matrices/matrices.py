import numpy as np

# Dimensions and Size
def describe(arr):
    """Print the array, its shape, and its dtype."""
    print(arr)
    print()
    print(f"{arr.shape} {arr.dtype}")
    print()


def multiply(a, b):
    """
    Multiply matrices a and b.
    If dimensions are incompatible, print a message and return None.
    """
    if a.shape[1] != b.shape[0]:
        print(f"Cannot multiply: a is {a.shape}, b is {b.shape}")
        return None
    return np.matmul(a, b)  # or a @ b

# Determinant and Inverse
def determinant(a):
    """Return determinant if square; otherwise print message and return None."""
    if a.shape[0] != a.shape[1]:
        print(f"Cannot compute determinant: matrix is not square {a.shape}")
        return None
    return np.linalg.det(a)


def inverse(a):
    """Return inverse if square; otherwise print message and return None."""
    if a.shape[0] != a.shape[1]:
        print(f"Cannot compute inverse: matrix is not square {a.shape}")
        return None
    return np.linalg.inv(a)

# Solving Linear Systems
def check_solution(a, b, x):
    """Verify A*x = b."""
    assert np.allclose(np.dot(a, x), b)

def solve_linear_system(a, b, unknowns):
    """
    Solve A x = b.
    Return dictionary mapping variable names to solution values.
    """
    x = np.linalg.solve(a, b)
    check_solution(a, b, x)

    solution = {}
    for name, value in zip(unknowns, x):
        solution[name] = value

    return solution

def main():
    # Test matrices
    a = np.array([[6, -1], [12, 8], [-5, 4]])
    b = np.array([[4, 0], [0.5, 2]])
    c = np.array([[2, -2], [3, 1]])

    # Describe each matrix
    describe(a)
    describe(b)
    describe(c)

    mats = [("a", a), ("b", b), ("c", c)]

    # Test multiplication for all pairings
    for name1, m1 in mats:
        for name2, m2 in mats:
            print(f"Trying {name1} * {name2}")
            prod = multiply(m1, m2)
            if prod is not None:
                print(prod)
            print()

    # Determinant and inverse tests
    for name, m in mats:
        print(f"Determinant of {name}:")
        det = determinant(m)
        print(det)
        print()

        print(f"Inverse of {name}:")
        inv = inverse(m)
        print(inv)
        print()

    # Linear System Example
    # System:
    # 50 = 5x3 - 7x2
    # 4x2 + 7x3 + 30 = 0
    # x1 - 7x3 = 40 - 3x2 + 5x1

    # Rewrite in standard form A x = b:
    # Equation 1:   0*x1 - 7*x2 + 5*x3 = 50
    # Equation 2:   0*x1 + 4*x2 + 7*x3 = -30
    # Equation 3:   (1 - 5)x1 + 3*x2 - 7*x3 = 40

    A = np.array([
        [0, -7, 5],
        [0, 4, 7],
        [-4, 3, -7]
    ])

    B = np.array([50, -30, 40])

    unknowns = ["x1", "x2", "x3"]

    print("Solution to linear system:")
    sol = solve_linear_system(A, B, unknowns)
    print(sol)
    print()


if __name__ == "__main__":
    main()
