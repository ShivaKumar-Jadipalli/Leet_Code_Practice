class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        N, M = len(grid), len(grid[0])
        cells = [None for _ in range(N * M)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cells[grid[i][j]] = [i, j]
        
        deltas = set([(-2, -1), (-2,1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)])
        if cells[0] != [0,0]:
            return False
        for i in range(1, len(cells)):
            if cells[i] == None:
                return False
            pvx, pvy = cells[i-1]
            cx, cy = cells[i]
            dx, dy = cx - pvx, cy - pvy
            if (dx, dy) not in deltas:
                return False
        return True

        