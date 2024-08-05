def mark(grid, i, j):
    bfs = [(i, j)]
    grid[i][j] = "0"
    while bfs:
        i, j = bfs.pop(0)
        grid[i][j] = "0"
        if i + 1 < len(grid) and grid[i + 1][j] == "1":
            grid[i + 1][j] = "0"
            bfs.append((i + 1, j))
        if j + 1 < len(grid[0]) and grid[i][j + 1] == "1":
            grid[i][j + 1] = "0"
            bfs.append((i, j + 1))
        if i - 1 >= 0 and grid[i - 1][j] == "1":
            grid[i - 1][j] = "0"
            bfs.append((i - 1, j))
        if j - 1 >= 0 and grid[i][j - 1] == "1":
            grid[i][j - 1] = "0"
            bfs.append((i, j - 1))
def numIslands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                mark(grid, i, j)
    return count
print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))