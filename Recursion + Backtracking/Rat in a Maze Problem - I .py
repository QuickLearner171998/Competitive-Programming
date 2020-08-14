"""Rat in a Maze Problem - I
Consider a rat placed at (0, 0) in a square matrix of order N*N. It has to reach the destination at (n-1, n-1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and cannot be crossed while value 1 at a cell in the matrix represents that it can be travelled through.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line contains an integer N denoting the size of the square matrix. The next line contains N*N space separated values of the matrix m where 0's represents blocked paths and 1 represent valid paths.

Output:
For each test case, the output will be space separated sorted strings denoting all directions, which the rat could take to reach the destination. Print -1 if no such path exists.

User Task:
Your task is to complete the function printPath() which returns a sorted array of strings denoting all the possible paths which the rat can take to reach the destination at (n-1, n-1). If no such path exists the function should return an empty array.

Expected Time Complexity: O((N2)4).
Expected Auxiliary Space: O(L*X), L = length of the path, X = number of paths.


Constraints:
1 <= T <= 100
2 <= N <= 5
0 <= matrix[i][j] <= 1

Example
Input:
3
4
1 0 0 0 1 1 0 1 0 1 0 0 0 1 1 1
4
1 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1
2
1 0 1 0

Output:
DRDDRR
DDRDRR DRDDRR
-1

Explanation:
Testcase 2: The given input is in the form
1 0 0 0
1 1 0 1
1 1 0 0
0 1 1 1
For the above matrix the rat can reach the destination at (3, 3) from (0, 0) by two paths ie DRDDRR and DDRDRR when printed in sorted order we get DDRDRR DRDDRR."""


def validMove(arr, r, c, visited, n):
    if r < 0 or r > n - 1 or c < 0 or c > n - 1 or arr[r][c] == 0 or visited[r][c] == 1:
        return False
    return True


def findPath1(arr, r, c, visited, n, ans, path):
    if r < 0 or r > n - 1 or c < 0 or c > n - 1:
        return path, ans
    if arr[r][c] == 0 or visited[r][c] == 1:
        return path, ans
    if r == n - 1 and c == n - 1:
        ans.append("".join(path))
        return path, ans

    visited[r][c] = 1

    # Top
    if validMove(arr, r - 1, c, visited, n):
        path.append("U")
        path, ans = findPath1(arr, r - 1, c, visited, n, ans, path)
        path.pop()

    # Down
    if validMove(arr, r + 1, c, visited, n):
        path.append("D")
        path, ans = findPath1(arr, r + 1, c, visited, n, ans, path)
        path.pop()

    # Left

    if validMove(arr, r, c - 1, visited, n):
        path.append("L")
        path, ans = findPath1(arr, r, c - 1, visited, n, ans, path)
        path.pop()

    # right
    if validMove(arr, r, c + 1, visited, n):
        path.append("R")
        path, ans = findPath1(arr, r, c + 1, visited, n, ans, path)
        path.pop()

    visited[r][c] = 0

    return path, ans


def findPath(arr, n):
    # code here
    visited = [[0] * n for i in range(n)]
    ans = []
    path, ans = findPath1(arr, 0, 0, visited, n, [], ans)
    # ans = ans[::-1]
    finalAns = ""
    ans.sort()
    for s in ans:
        finalAns += (s + ' ')
    return finalAns[:-1] if len(ans) else -1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])] for j in range(n[0])]
        k = 0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k += 1

        result = findPath(matrix, n[0])
        if result == "":
            print(-1)
        else:
            print(result)
# } Driver Code Ends
