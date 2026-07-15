from src.matrix.inverse import inverse

def test_inverse():
    A = [[2, 1], [5, 3]]

    assert inverse(A) == [[3, -1], [-5, 2]]