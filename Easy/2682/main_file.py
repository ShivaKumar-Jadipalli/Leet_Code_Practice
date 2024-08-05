class Solution:
    def circularGameLosers(self, n,k): # [1,2,3,4,5]
        temp_list = [1]
        current_pos = 0 
        increase_by  = k 
        while len(set(temp_list)) ==  len(temp_list):
            temp = increase_by+current_pos # 2
            if  temp < n:
                temp_list.append(temp+1) # 2
            else :
                near_number = temp//n 
                temp_2 = n*near_number # 15
                temp  = temp - temp_2 
                temp_list.append(temp+1)
            increase_by += k # 2
            current_pos = temp  # 4 
        answers = []
        for i in range(1,n+1):
            if i not in temp_list:
                answers.append(i)
        return sorted(answers)
print(Solution().circularGameLosers(5,2))
print(Solution().circularGameLosers(4,4))