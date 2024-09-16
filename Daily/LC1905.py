from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(row, col):
            isSubIsland = grid1[row][col] == 1
            grid2[row][col] = 0
            for dRow, dCol in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                newRow, newCol = row + dRow, col + dCol
                if 0 <= newRow < rows and 0 <= newCol < cols and grid2[newRow][newCol] == 1:
                    if not dfs(newRow, newCol):
                        isSubIsland = False
            return isSubIsland
        rows, cols = len(grid1), len(grid1[0])
        subIslandCount = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1 and dfs(row, col):
                    subIslandCount += 1
        return subIslandCount
