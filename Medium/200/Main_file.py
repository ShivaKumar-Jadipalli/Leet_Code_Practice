class Solution:
    def count_island(self,row,column):
        if not (0 <= row < self.max_row and 0 <= column < self.max_column):
            return 0 
        if self.grid[row][column]=="1":
            self.grid[row][column] = "0"
        else:
            return 0 
        self.count_island(row+1,column)
        self.count_island(row-1,column)
        self.count_island(row,column-1)
        self.count_island(row,column+1)
    def numIslands(self, grid):
        answer = 0
        self.grid = grid 
        self.max_row = len(self.grid)
        self.max_column = len(self.grid[0])
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])): 
                if self.grid[row][column] == "1":
                    answer += 1 
                    self.count_island(row,column)
        return answer
    
print(Solution().numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))