#User function Template for python3


#Function to find the maximum possible amount of money we can win.
def optimalStrategyOfGame(arr, n):

    # code here
    dp = [[0]*(n) for _ in range(n)]
    # for i in range(n):
    #     dp[i][i] = arr[i]
    for gap in range(n):
        for j in range(gap, n):
            i= j-gap
            x = 0
            if((i + 2) <= j):
                x = dp[i + 2][j]
            y = 0
            if((i + 1) <= (j - 1)):
                y = dp[i + 1][j - 1]
            z = 0
            if(i <= (j - 2)):
                z = dp[i][j - 2]            
            dp[i][j] = max((arr[i] + min(x, y)), (arr[j] + min(y,z)))
    return dp[0][-1]


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        print(optimalStrategyOfGame(arr,n))

# } Driver Code Ends