from src.matrix.scalar_multiply import scalar_multiply

def test_scalar_multiply():
    A = [[1,2],[3,4]]
    x = 2
    assert scalar_multiply(x, A)== [[2,4],[6,8]]