def transpose(A):
    rows = len(A)
    cols = len(A[0])
    result = []

    for j in range(cols):
        result.append([0] * rows)

    for i in range(rows):
        for j in range(cols):
          result[j][i] = A[i][j]

    return result