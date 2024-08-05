class Solution: # we need to keep track of the number as well 
    def checkValidGrid(self, grid):
        if grid[0][0] != 0:
            return False
        self.number = 1
        self.shape = len(grid)
        self.end_number = self.shape**2
        return self.start_rec(grid,0,0)
    def start_rec(self, grid,i,j):
        if self.number == self.end_number:
            return True 
        check_list = ([i-1,j-2],[i-1,j+2],[i+1,j+2],[i+1,j-2],[i+2,j-1],[i+2,j+1],[i-2,j+1],[i-2,j-1])
        for i in check_list:
            if 0<=i[0]<self.shape and 0<=i[1]<self.shape and grid[i[0]][i[1]] == self.number:
                self.number += 1
                return self.start_rec(grid,i[0],i[1])
        return False

print(Solution().checkValidGrid([[8,3,6],[5,0,1],[2,7,4]]))