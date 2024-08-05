import pytest
from main_file import Solution

@pytest.mark.parametrize("dist ,speed , answer ",[([1],[1],1),([4,2,3],[2,1,1],3),([1,3,4],[1,1,1],3),([1,1,2,3],[1,1,1,1],1),([3,2,4],[5,3,2],1),([3,5,7,4,5],[2,3,6,3,2],2),([4,2,8],[2,1,4] ,2)])
                         
def test_candy(dist,speed,answer):
    assert Solution().eliminateMaximum(dist,speed) == answer
    