import numpy as np
from scipy.linalg import solve_banded

# Number of steps
N = 44  # We want p_44

# Set up the coefficients for the banded matrix based on the recurrence relation
# The recurrence relation is p[n+1] - 2 * p[n-2] + p[n] = 1
# This implies we need a tridiagonal matrix setup

# Define the banded matrix coefficients
# The main diagonal (center row), lower diagonal, and upper diagonal
lower_diag = [-2] * (N - 1)
main_diag = [1] * N
upper_diag = [1] * (N - 1)

# Assemble the matrix in banded form (diagonals)
# For `solve_banded`, diagonals are given from the top row to the bottom row of the banded matrix
ab = np.zeros((3, N))  # 3 rows for the diagonals
ab[0, 1:] = upper_diag  # upper diagonal
ab[1, :] = main_diag    # main diagonal
ab[2, :-1] = lower_diag  # lower diagonal

# Right-hand side vector (RHS) for the equation Ax = b
# The RHS is 1 for each element because of the "+1" in the recurrence relation
b = np.ones(N)

# Solve the banded system
p_values = solve_banded((1, 1), ab, b)

# Extract the desired probability p[44]
p_44 = p_values[-1]  # p[44] is the last element in p_values since we solve up to 44

# Print the result, rounded to three decimals
print(f"Probability p_44: {p_44:.3f}")
