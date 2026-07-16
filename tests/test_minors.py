from src.matrix.minors import minors

def test_minors():
    A = [
        [1, 2, 3],
        [0, 4, 5],
        [1, 0, 6]
    ]

    assert minors(A) == [
        [24, -5, -4],
        [12, 3, -2],
        [-2, 5, 4]
    ]