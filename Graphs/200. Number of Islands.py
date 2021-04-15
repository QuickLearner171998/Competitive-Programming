"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid[0]), len(grid)
        def dfs(grid, i , j):
            grid[i][j] = "-1"
            neigh = [(i-1, j), (i+1,j), (i, j+1), (i, j-1)]
            for ne in neigh:
                n1, n2 = ne
                if n1>=0 and n1<m and n2>=0 and n2<n:
                    if grid[n1][n2] == '1':
                        dfs(grid, n1, n2)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans+=1
                    dfs(grid, i, j)
        return ans
            