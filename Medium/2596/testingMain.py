import pytest
from main_file import Solution

@pytest.mark.parametrize("given_input,expected_output",[([[8,3,6],[5,0,1],[2,7,4]],False),([[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]],True),([[0,3,6],[5,8,1],[2,7,4]],False)])
                         
def test_candy(given_input,expected_output):
    assert Solution().checkValidGrid(given_input) == expected_output