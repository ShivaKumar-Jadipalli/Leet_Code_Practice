import pytest
from Best_solution import Solution
def get_link(house):
    test_link = []
    for i in range(2,house):
        start_index = 1
        while start_index+i <= house:
            test_link.append([start_index,start_index+i])
            start_index += 1
    return test_link

def test_candy_1():
    houses = [*range(5,15*10)]
    for house in houses :
        test_links = get_link(house)
        for count , [i,j] in enumerate(test_links):
            test_1 = Solution().countOfPairs(house,i,j)
            assert [test_1[0],test_1[-2:]] == [house*2 , [0,0]]