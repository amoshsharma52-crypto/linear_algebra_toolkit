def cofactors(minor_matrix):
    result = []

    for i, row in enumerate(minor_matrix):

        current_row = []

        for j, value in enumerate(row):
            sign = 1 if (i + j) % 2 == 0 else -1
            current_row.append(sign * value)

        result.append(current_row)

    return result