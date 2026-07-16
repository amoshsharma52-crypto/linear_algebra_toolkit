from src.matrix.submatrix import submatrix

def test_submatrix():
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    assert submatrix(A, 1, 0) == [
        [2, 3],
        [8, 9]
    ]