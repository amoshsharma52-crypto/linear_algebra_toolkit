from src.matrix.basics import shape

def test_shape():
    matrix = [[1, 2],[3, 4],[5, 6]]
    assert shape(matrix) == (3, 2)