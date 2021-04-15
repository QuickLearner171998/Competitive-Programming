"""Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(board, i, j, not_flip):
            q = [(i,j)]
            not_flip.add((i,j))
            while len(q ):
                i, j = q.pop(0)
                neighbours = [(i-1, j), (i+1,j),(i,j+1), (i, j-1)]
                for neigh in neighbours:
                    n1, n2 = neigh
                    if n1 >=0 and n1<=m-1 and n2>=0 and n2<=n-1:
                        if board[n1][n2] == "O" and str(n1)+'_'+str(n2) not in not_flip:
                            q.append((n1, n2))
                            not_flip.add((str(n1)+'_'+str(n2)))

            
        m = len(board)
        n = len(board[0])
        not_flip = set()
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j==0 or i == m-1 or j== n-1:
                    if board[i][j] == 'O':
                        bfs(board, i, j, not_flip)
                        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and (str(i)+'_'+str(j)) not in not_flip:
                    board[i][j] = 'X'
                
                
                        
                        