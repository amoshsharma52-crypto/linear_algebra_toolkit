from src.matrix.basics import shape
def add(A, B):
    if shape(A) != shape (B):
        raise ValueError("Order of both matrices must be equal")
    
    rows, columns = shape(A)
    result = []

    for row in range(rows):
        new_row = []

        for column in range(columns):
            new_row.append(A[row][column] + B[row][column])
        result.append(new_row)
    return result
    