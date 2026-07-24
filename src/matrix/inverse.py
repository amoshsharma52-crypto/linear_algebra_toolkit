from src.matrix.determinant import determinant
from src.matrix.minors import minors
from src.matrix.cofactors import cofactors
from src.matrix.transpose import transpose
from src.matrix.scalar_multiply import scalar_multiply

def inverse(matrix):
    det = determinant(matrix)

    if det == 0:
        raise ValueError("Matrix is singular and has no inverse")

    minor_matrix = minors(matrix)
    cofactor_matrix = cofactors(minor_matrix)
    adjugate = transpose(cofactor_matrix)

    return scalar_multiply(adjugate, 1 / det)