from src.matrix.matrix_multiply import matrix_multiply
import pytest

def test_matrix_multiply():
    A = [[1,2],[3,4]]
    B = [[5,6],[7,8]]
    assert matrix_multiply(A, B) == [[19,22],[43,50]]

def test_matrix_multiply_invalid_shape():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4]]

    with pytest.raises(ValueError):
        matrix_multiply(A, B)