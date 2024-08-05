import numpy as np 
class Solution:
    def modifiedMatrix(self, matrix):
        matrix = np.rot90(np.array(matrix))
        answer_matrix = matrix.copy()
        for count_row , row in enumerate(matrix):
            negative , max_value , position = False , 0 , []
            for count_col , col in enumerate(row):
                if col>max_value:
                    max_value=col 
                if col == -1:
                    negative = True 
                    position.append([count_row,count_col])
            if negative == True:
                for x in position:
                    answer_matrix[x[0]][x[1]]= max_value
        return np.rot90(answer_matrix,k=-1)
answer = Solution().modifiedMatrix([[1,2,-1],[4,-1,
6],[7,8,9]])
print(answer)