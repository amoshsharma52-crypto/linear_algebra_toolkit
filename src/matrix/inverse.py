from src.matrix.determinant import determinant

def inverse(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is Singular and has no inverse")
    
    