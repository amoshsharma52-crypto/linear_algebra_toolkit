from src.matrix.determinant import determinant
import pytest
def test_determinant():
        A=[[1,-2,3],[3,1,2],[0,1,2]]
        assert determinant(A)== 21

def test_determinant_error():
    A = [[1, 2, 3], [2, 4, 6]]

    with pytest.raises(ValueError):
        determinant(A)