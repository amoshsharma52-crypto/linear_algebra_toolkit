def shape(matrix):
    if matrix:
        rows = len(matrix)
        columns = len(matrix[0])
        return rows, columns

    return 0, 0