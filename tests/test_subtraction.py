from src.matrix.subtraction import subtract
def test_subtract():
    A = [[7,2],[3,5]]
    B = [[1,2],[1,2]]
    assert subtract(A, B)==[[6,0],[2,3]]