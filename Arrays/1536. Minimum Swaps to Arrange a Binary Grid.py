"""Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).
"""


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        trailZ = len(grid) - 1
        ans = 0
        st = 1
        while trailZ:
            f = 0
            # z = [0]* trailZ
            # print(grid)
            for i, row in enumerate(grid):
                # print(row[len(grid) - trailZ:])
                if sum(row[st:]) == 0:
                    # print("IN")
                    # print(row[st :])
                    st += 1
                    ans += i
                    trailZ -= 1
                    grid.pop(i)
                    f = 1
                    break
                # else:
                #     f = 0
            if not f:
                return -1

        return ans
