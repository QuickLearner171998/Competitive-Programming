"""
200. Number of Islands
Medium

7264

229

Add to List

Share
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

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

"""


class Solution:
    
    
    def dfs(self, grid, visited, i, j, rows, cols):
        # check whetehr i and j in bounds
        if i<0 or i>=rows or j<0 or j>=cols:
            return 
        
        if grid[i][j]!="1":
            return 
        # if already visited return
        if grid[i][j]=="1":
            if visited[i][j]:
                return 
            visited[i][j] = 1
        #go in 4 dirns
        self.dfs(grid, visited, i-1, j, rows, cols)
        self.dfs(grid, visited, i+1, j, rows, cols)
        self.dfs(grid, visited, i, j-1, rows, cols)
        self.dfs(grid, visited, i, j+1, rows, cols)
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows==0:
            return 0
        cols = len(grid[0])
        if cols==0:
            return 0
        
        visited = [[0 for i in range(cols)] for j in range(rows)]
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    if visited[i][j] == 0:
                        ans+=1
                        self.dfs(grid, visited, i, j, rows, cols)
                        
        return ans