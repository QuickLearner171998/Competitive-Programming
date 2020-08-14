def placeNum(board, row, col, num):
    # row clash
    for i in range(len(board)):
        if num == board[row][i]:
            return False

    # col clash
    for i in range(len(board)):
        if num == board[i][col]:
            return False

    # square clash
    import math
    rootn = int(math.sqrt(len(board)))
    start = (row - row % rootn, col - col % rootn)
    for i in range(start[0], start[0] + rootn):
        for j in range(start[1], start[1] + rootn):
            if num == board[i][j]:
                return False
    return True


def solveSuduko(board):
    n = len(board)
    emptyCell = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                row = i
                col = j
                emptyCell = 1
                break
        if emptyCell:
            break
    if emptyCell == 0:
        return (True, board)

    for i in range(1, n + 1):
        if placeNum(board, row, col, i):
            board[row][col] = i
            if solveSuduko(board)[0]:
                return (True, board)
            board[row][col] = 0

    return (False, board)


# driver code
if __name__ == '__main__':
    import math

    t = int(input())
    for k in range(t):
        arr = list(map(int, input().strip().split()))
        n = int(math.sqrt(len(arr)))
        newList = []
        st = 0
        for i in range(n):
            subList = []
            for j in range(st, st + n):
                subList.append(arr[j])
            newList.append(subList)
            st = st + n
        ans = solveSuduko(newList)[1]
        for i in range(n):
            for j in range(n):
                if i == n - 1 and j == n - 1:
                    print(ans[i][j], end="")
                    continue
                print(ans[i][j], end=" ")
        print()
