from src.matrix.identity import identity_matrix
def test_identity_matrix():
    assert identity_matrix(3) == [[1,0,0],[0,1,0],[0,0,1]]