from src.matrix.basics import shape


def scalar_multiply(x, A):
    rows, columns = shape(A)
    result = []

    for row in range(rows):
        new_row = []

        for column in range(columns):
            new_row.append(x * A[row][column])

        result.append(new_row)

    return result