from src.matrix.submatrix import submatrix
from src.matrix.determinant import determinant

def minors(matrix):
    result = []

    for i, row in enumerate(matrix):

        current_row = []

        for j, _ in enumerate(row):

            sub = submatrix(matrix, i, j)

            minor = determinant(sub)

            current_row.append(minor)

        result.append(current_row)

    return result