# ============================================================
#  3x3 Matrix Calculator
#  Computes: Determinant and Transpose
#  No external libraries — pure Python lists
# ============================================================


def get_matrix():
    """Prompt the user to enter a 3x3 matrix row by row."""
    print("=" * 40)
    print("     3x3 Matrix Calculator")
    print("=" * 40)
    print("Enter the 9 values of your matrix,")
    print("one number at a time (press Enter after each).\n")

    matrix = []  # Will hold 3 rows, each a list of 3 numbers

    for row in range(3):
        current_row = []
        for col in range(3):
            while True:
                try:
                    value = float(input(f"  Row {row + 1}, Column {col + 1}: "))
                    current_row.append(value)
                    break
                except ValueError:
                    print("  ⚠  Please enter a valid number.")
        matrix.append(current_row)

    return matrix


def print_matrix(matrix, title="Matrix"):
    """Display a matrix in a readable grid format."""
    print(f"\n{title}:")
    for row in matrix:
        # Format each number to 2 decimal places, aligned in columns
        formatted = "  ".join(f"{val:8.2f}" for val in row)
        print(f"  [ {formatted} ]")


def calculate_determinant(m):
    """
    Calculate the determinant of a 3x3 matrix using cofactor expansion
    along the first row.

    For a 3x3 matrix:
        | a  b  c |
        | d  e  f |
        | g  h  i |

    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

    Each term uses a 2x2 minor (the 2x2 matrix left after removing
    the current row and column).
    """
    # Label elements for clarity
    a, b, c = m[0][0], m[0][1], m[0][2]
    d, e, f = m[1][0], m[1][1], m[1][2]
    g, h, i = m[2][0], m[2][1], m[2][2]

    # Compute the three 2x2 minor determinants
    minor_a = (e * i) - (f * h)   # Minor for element a (top-left)
    minor_b = (d * i) - (f * g)   # Minor for element b (top-middle)
    minor_c = (d * h) - (e * g)   # Minor for element c (top-right)

    # Apply cofactor signs (+, -, +) and sum the terms
    determinant = a * minor_a - b * minor_b + c * minor_c

    return determinant


def calculate_transpose(m):
    """
    Calculate the transpose of a 3x3 matrix.

    Transposing swaps rows and columns, so element [i][j] moves to [j][i].
    The first row becomes the first column, the second row becomes the
    second column, and so on.
    """
    transpose = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            transpose[j][i] = m[i][j]  # Swap row and column index

    return transpose


# ── Main program ─────────────────────────────────────────────

# Step 1: Get the matrix from the user
matrix = get_matrix()

# Step 2: Display what was entered
print_matrix(matrix, title="Your Matrix")

# Step 3: Calculate and display the determinant
det = calculate_determinant(matrix)
print(f"\nDeterminant: {det:.4f}")

# A determinant of 0 means the matrix has no inverse — useful to flag
if det == 0:
    print("  (Note: det = 0, so this matrix is singular and has no inverse.)")

# Step 4: Calculate and display the transpose
transpose = calculate_transpose(matrix)
print_matrix(transpose, title="Transpose")

print("\nDone!")
