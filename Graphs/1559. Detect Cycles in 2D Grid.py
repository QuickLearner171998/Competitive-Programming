"""1559. Detect Cycles in 2D Grid

Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false"""

class Solution:

    def dfs(self, i, j, grid, visited, pi, pj, n, m):

        def validDir(ni, nj):
            if ni < 0 or ni > m - 1 or nj < 0 or nj > n - 1:
                return 0
            return 1

        def nextSame(i, j, nexti, nextj, grid):
            if grid[i][j] == grid[nexti][nextj]:
                return 1
            return 0

        def notSameParent(pi, pj, nexti, nextj):
            if (pi == nexti) and (pj == nextj):
                return 0
            return 1

        # if validDir(i, j):
        visited[i][j] = 1

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        for d in range(len(dx)):
            nexti = i + dx[d]
            nextj = j + dy[d]

            if validDir(nexti, nextj) and nextSame(i, j, nexti, nextj, grid) and notSameParent(pi, pj, nexti, nextj):

                # print(nexti, nextj)
                if visited[nexti][nextj]:
                    return 1
                c = self.dfs(nexti, nextj, grid, visited, i, j, n, m)
                if c:
                    return 1
        return 0

    def containsCycle(self, grid):
        if len(grid) <2 or len(grid[0])<2:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        f = 0  # 1 if cycle there

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    f = self.dfs(i, j, grid, visited, -1, -1, n, m)
                    if f:
                        return 1
        return 0  # if f else 0
