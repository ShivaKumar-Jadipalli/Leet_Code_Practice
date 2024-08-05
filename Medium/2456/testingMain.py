import pytest
from main_file import Solution

@pytest.mark.parametrize("Creators , Ids , Views ,Answers ",[(["alice","bob","alice","chris"],["one","two","three","four"],[5,10,5,4],[["alice","one"],["bob","two"]]),(["alice","alice","alice"],["a","b","c"],[1,2,2],[["alice","b"]])])
                         
def test_candy(Creators , Ids , Views ,Answers):
    assert Solution().mostPopularCreator(Creators,Ids,Views) == Answers
    