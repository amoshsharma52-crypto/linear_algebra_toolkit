def cofactors(minor_matrix):
    result = []

    for i, row in enumerate(minor_matrix):

        current_row = []

        for j, value in enumerate(row):

            if (i + j) % 2 == 0:
                current_row.append(value)
            else:
                current_row.append(-value)

        result.append(current_row)

    return result