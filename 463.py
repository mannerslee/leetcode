class Solution:
    def islandPerimeter(self, grid):
        count = 0
        neighbour = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count += 1
                    if j > 0 and grid[i][j - 1] == 1:
                        neighbour += 1
                    if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                        neighbour += 1
                    if i > 0 and grid[i - 1][j] == 1:
                        neighbour += 1
                    if i < len(grid) - 1 and grid[i + 1][j] == 1:
                        neighbour += 1
        return count * 4 - neighbour
