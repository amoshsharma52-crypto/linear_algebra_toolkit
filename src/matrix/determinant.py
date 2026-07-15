from src.matrix.basics import shape

def determinant(A):
    rows_A, cols_A = shape(A)

    if cols_A != rows_A:
        raise ValueError("Determinants cannot be calculated on non-square matrices")

    if rows_A == 1:
        return A[0][0]

    if rows_A == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    det = 0

    for col in range(cols_A):
        sign = (-1) ** col

        minor = []

        for row in A[1:]:
            minor.append(row[:col] + row[col + 1:])

        det += sign * A[0][col] * determinant(minor)

    return det