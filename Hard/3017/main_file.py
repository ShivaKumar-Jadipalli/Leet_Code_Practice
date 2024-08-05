import numpy as np , pandas as pd
from Best_solution import Solution
def get_link(house):
    test_link = [[1,1]]
    for i in range(2,house):
        start_index = 1
        while start_index+i <= house:
            test_link.append([start_index,start_index+i])
            start_index += 1
    return test_link

answer_list = {'house':[],'links':[],'Results':[],'difference':[],'sum':[],'maximum':[]}
for house in range(5,15) :
    test_links = get_link(house)
    for count , [i,j] in enumerate(test_links):
        test_1 = Solution().countOfPairs(house,i,j)
        if count != 0:
            test_1 = np.array(test_1[1:-2])
            sample = list(test_1 - previous)
            previous = test_1
            answer_list['house'].append(house)
            answer_list["links"].append([i,j])
            answer_list["Results"].append(list(test_1))
            answer_list["difference"].append(abs(i-j))
            answer_list["sum"].append(i+j)
            answer_list["maximum"].append(max(sample))
        else:
            previous = test_1[1:-2]

data = pd.DataFrame(answer_list)
data.to_excel("kabali_da.xlsx",index=False)