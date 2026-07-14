from src.matrix.basics import shape

def matrix_multiply (A, B):
    rows_A, cols_A = shape(A)
    rows_B, cols_B = shape(B)
    
    if cols_A != rows_B:
     raise ValueError("Matrices cannot be multiplied")
    
    
    result = []
    
    for i in range(rows_A):
        result_row = []

        for j in range(cols_B):
            total = 0
        
            for k in range(cols_A):
                total = total + A[i][k] * B[k][j]

            result_row.append(total)

        result.append(result_row)
    return result