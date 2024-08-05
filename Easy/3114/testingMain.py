import pytest
import main_file as code

@pytest.mark.parametrize("given_input,expected_output",[([[1,3,1],[1,5,1],[4,2,1]],7),([[1,2,3],[4,5,6]],12),([[4,4,4,4,4],[4,4,4,4,4],[4,4,3,4,4],[4,4,4,4,4]],31)])
                         
# def test_candy(given_input,expected_output):
#     assert code.minPathSum(given_input) == expected_output
    
def test_candy_1():
    assert code.minPathSum([[4,4,4,4,4],[4,4,4,4,4],[4,4,3,4,4],[4,4,4,4,4]]) == 31
    
def test_candy_2():
    assert code.minPathSum([[1,2,3],[4,5,6]]) == 12

    
def test_candy_3():
    assert code.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7

    
def test_candy_4():
    assert code.minPathSum([[1,20,3],[1,5,6],[7,8,9]]) == 22

