def submatrix(matrix, row_to_remove, col_to_remove):
    result = []

    for i, row in enumerate(matrix):

        if i == row_to_remove:
            continue

        new_row = row[:col_to_remove] + row[col_to_remove + 1:]

        result.append(new_row)

    return result