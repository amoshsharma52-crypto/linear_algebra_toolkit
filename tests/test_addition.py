from src.matrix.addition import add

def test_add():
    A=[[1,3],[2,3]]
    B=[[3,4],[2,5]]
    assert add(A, B) == [[4,7],[4,8]]