import pytest
from main_file import Solution

@pytest.mark.parametrize("given_input,expected_output",[([5,3,4,1,1],13),([6,5,3,9,2,7],22),([3,2,5,5,2,3],18),([2,4,5,2,5,5,2,1,1,3],23),([1,2,2,2,6,1,4,6,4],20)])

def test_candy(given_input,expected_output):
    assert Solution().maximumSumOfHeights(given_input) == expected_output